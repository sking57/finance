import os

from cs50 import SQL
from flask import Flask, flash, jsonify, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.exceptions import default_exceptions
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required, lookup, usd

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Ensure responses aren't cached


@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")


@app.route("/")
@login_required
def index():
    """Show portfolio of stocks"""
    rows = db.execute("SELECT name, symbol, SUM(shares) AS shares FROM portfolio WHERE id=:id GROUP BY symbol",
                      id=session["user_id"])
    rows2 = db.execute("SELECT * FROM users WHERE id=:id", id=session["user_id"])
    price_array = []
    for row in rows:
        quote = lookup(row["symbol"])
        current_price = (quote["price"])
        row["price"] = current_price
        price_array.append(current_price)
    # include current cash value in index table
    current_cash = float(rows2[0]["cash"])
    return render_template("index.html", rows=rows, cash=current_cash, total=float(sum(price_array))+current_cash)


@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    """Buy shares of stock"""
    if request.method == "POST":

        # ensure everything was inputted
        if not request.form.get("shares") or not request.form.get("symbol"):
            return apology("fill out all fields", 400)
        if not request.form.get("shares").isdigit():
            return apology("must input integer", 400)
        shares = float(request.form.get("shares"))
        if not shares >= 1:
            return apology("shares must be positive", 400)

        # look up symbol inputted by user
        quote = lookup(request.form.get("symbol"))
        # ensure valid symbol
        if not quote:
            return apology("invalid symbol", 400)

        # create variables from dict
        name = quote["name"]
        price = quote["price"]
        symbol = quote["symbol"]
        cost = shares*price
        rows = db.execute("SELECT * FROM users WHERE id=:id", id=session["user_id"])
        current_cash = rows[0]["cash"]

        # check if user has sufficient funds for purchase
        if current_cash >= cost:
            # save transaction in history table
            db.execute("INSERT INTO history (id, price, symbol, shares) VALUES (:id, :price, :symbol, :shares)",
                       id=session["user_id"], price=price, symbol=symbol, shares=shares)
            # put stock info in portfolio
            db.execute("INSERT INTO portfolio (id, name, price, symbol, shares, cost) VALUES (:id, :name, :price, :symbol, :shares, :cost)",
                       id=session["user_id"], name=name, price=price, symbol=symbol, shares=shares, cost=cost)
            db.execute("UPDATE users SET cash = cash - :cost WHERE id=:id", cost=cost, id=session["user_id"])
        else:
            return apology("insufficient funds", 403)

        # once table is updated, redirect to index to show html table of current holds
        return redirect("/")

    else:
        return render_template("buy.html")


@app.route("/check", methods=["GET"])
def check():
    username = request.args.get("username")
    if not username:
        return apology("must submit username!", 403)
    existence = db.execute("SELECT * FROM users WHERE username = :username", username=username)
    if existence:
        """Return true if username available, else false, in JSON format"""
        return jsonify(False)
    return jsonify(True)


@app.route("/history")
@login_required
def history():
    """Show history of transactions"""
    rows = db.execute("SELECT * FROM history WHERE id=:id", id=session["user_id"])
    return render_template("history.html", rows=rows)


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = :username",
                          username=request.form.get("username"))

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():
    """Get stock quote."""
    if request.method == "POST":

        # look up symbol inputted by user
        if not request.form.get("symbol"):
            return apology("must input symbol")
        quote = lookup(request.form.get("symbol"))
        # ensure valid symbol
        if not quote:
            return apology("invalid symbol", 400)
        name = quote["name"]
        price = quote["price"]
        symbol = quote["symbol"]

        # if symbol is valid, return data
        return render_template("quoted.html", name=name, price=price, symbol=symbol)

    # user reached quote via GET
    else:
        return render_template("quote.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""
    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        username = request.form.get("username")
        if not username:
            return apology("must provide username", 400)
        # Ensure username is >1 and unique
        rows = db.execute("SELECT * FROM users WHERE username = :username", username=username)
        if rows:
            return apology("username already exists")
        # Ensure password and confirmation were submitted
        elif not request.form.get("password"):
            return apology("must provide password", 400)
        elif not request.form.get("confirmation"):
            return apology("must provide confirmation", 400)
        # personal touch: ensure password length is at least 2
        elif len(request.form.get("password")) < 3:
            return apology("password must be at least 3 characters. Try again!", 400)
        # ensure that password and confirmation are equal
        elif request.form.get("confirmation") != request.form.get("password"):
            return apology("password and confirmation do not match", 400)

        # encrypt password
        hash_ = generate_password_hash(request.form.get("password"))
        # insert new user into database
        id = db.execute("INSERT INTO users (username, hash) VALUES (:username, :hash)", username=username,
                        hash=hash_)
        # store id number to log user in automatically
        session["user_id"] = id

        return redirect("/")

    # user reached register via GET
    else:
        return render_template("register.html")


@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    """Sell shares of stock"""
    if request.method == "POST":

        # ensure everything was inputted
        if not (request.form.get("shares")) or not request.form.get("symbol"):
            return apology("fill out all fields", 400)
        if int(request.form.get("shares")) < 1:
            return apology("shares must be positive", 400)
        shares = float(request.form.get("shares"))
        # look up symbol inputted by user
        quote = lookup(request.form.get("symbol"))
        # ensure valid symbol
        if not quote:
            return apology("invalid symbol", 400)

        # create variables from dict
        name = quote["name"]
        price = quote["price"]
        symbol = quote["symbol"]
        cost = shares*price
        # retrieve value of current cash
        row = db.execute("SELECT * FROM users WHERE id=:id", id=session["user_id"])
        current_cash = row[0]["cash"]

        # retrieve the row from portfolio with the same symbol so we can access information from it
        rows = db.execute("SELECT * FROM portfolio WHERE symbol=:symbol AND id=:id", symbol=symbol, id=session["user_id"])

        # if user has enough shares of the certain stock, add stock to history table and update the cash value of user
        if rows[0]["shares"] > shares:
            # save transaction in history table
            db.execute("INSERT INTO history (id, price, symbol, shares) VALUES (:id, :price, :symbol, :shares)",
                       id=session["user_id"], price=price, symbol=symbol, shares=-1*shares)
            # update information in portfolio and users
            db.execute("UPDATE portfolio SET shares = shares - :shares WHERE symbol=:symbol AND id=:id",
                       shares=shares, symbol=symbol, id=session["user_id"])
            db.execute("UPDATE portfolio SET cost = cost - :cost WHERE symbol=:symbol AND id=:id",
                       cost=cost, symbol=symbol, id=session["user_id"])
            db.execute("UPDATE users SET cash = cash + :cost WHERE id=:id", cost=cost, id=session["user_id"])
        elif rows[0]["shares"] == shares:
            db.execute("DELETE FROM portfolio WHERE symbol=:symbol AND id=:id", symbol=symbol, id=session["user_id"])
        else:
            return apology("insufficient stock holdings", 400)

        # once table is updated, redirect to index to show html table of current holds
        return redirect("/")

    else:
        rows = db.execute("SELECT * FROM portfolio WHERE id=:id", id=session["user_id"])
        return render_template("sell.html", rows=rows)


def errorhandler(e):
    """Handle error"""
    return apology(e.name, e.code)


# listen for errors
for code in default_exceptions:
    app.errorhandler(code)(errorhandler)

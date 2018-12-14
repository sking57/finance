import os
import requests
import xml.etree.ElementTree as ET

from cs50 import SQL
from flask import Flask, flash, jsonify, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.exceptions import default_exceptions
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required, loadRSS, parseXML, savetoCSV

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

# # Custom filter
# app.jinja_env.filters["usd"] = usd

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
    """Show welcome page"""
    return render_template("home.html")


@app.route("/check", methods=["GET"])
def check():
    """Return true if username available, else false, in JSON format"""

    # Get username
    username = request.args.get("username")

    # Check for username
    if not len(username) or db.execute("SELECT 1 FROM users WHERE username = :username", username=username.lower()):
        return jsonify(False)
    else:
        return jsonify(True)


@app.route("/events")
@login_required
def events():
    """Display local events."""

    # Look up future events in Boston.
    # load rss from web to update existing xml file
    loadRSS()

    # parse xml file
    events = parseXML('file.xml')

    # store news items in a csv file
    savetoCSV(events, 'events.csv')

    return render_template("events.html", titles=title, urls=url, descriptions=description, starts=start, ends=end, addresses=address, cities=city, states=state)

    # write API results into file by looking up future boston events through eventful's API

    # # create the file structure
    # data = ET.Element('search')
    # items = ET.SubElement(data, 'events')
    # item1 = ET.SubElement(items, 'event')
    # c1 = ET.SubElement(item1, 'title')
    # c2 = ET.SubElement(item1, 'url')
    # c3 = ET.SubElement(item1, 'description')
    # c4 = ET.SubElement(item1, 'start_time')
    # c5 = ET.SubElement(item1, 'stop_time')
    # c6 = ET.SubElement(item1, 'venue_address')
    # c7 = ET.SubElement(item1, 'city_name')
    # c8 = ET.SubElement(item1, 'region_abbr')
    # item2 = ET.SubElement(items, 'event')
    # c1 = ET.SubElement(item2, 'title')
    # c2 = ET.SubElement(item2, 'url')
    # c3 = ET.SubElement(item2, 'description')
    # c4 = ET.SubElement(item2, 'start_time')
    # c5 = ET.SubElement(item2, 'stop_time')
    # c6 = ET.SubElement(item2, 'venue_address')
    # c7 = ET.SubElement(item2, 'city_name')
    # c8 = ET.SubElement(item2, 'region_abbr')
    # item3 = ET.SubElement(items, 'event')
    # c1 = ET.SubElement(item3, 'title')
    # c2 = ET.SubElement(item3, 'url')
    # c3 = ET.SubElement(item3, 'description')
    # c4 = ET.SubElement(item3, 'start_time')
    # c5 = ET.SubElement(item3, 'stop_time')
    # c6 = ET.SubElement(item3, 'venue_address')
    # c7 = ET.SubElement(item3, 'city_name')
    # c8 = ET.SubElement(item3, 'region_abbr')
    # item4 = ET.SubElement(items, 'event')
    # item5 = ET.SubElement(items, 'event')
    # item6 = ET.SubElement(items, 'event')
    # item7 = ET.SubElement(items, 'event')
    # item8 = ET.SubElement(items, 'event')
    # item9 = ET.SubElement(items, 'event')
    # item10 = ET.SubElement(items, 'event')
    # item1.set('name','item1')
    # item2.set('name','item2')
    # item1.text = whatever the API says
    # item2.text = whatever the API says

    # # create a new XML file with the results
    # mydata = ET.tostring(data)
    # myfile = open("items2.xml", "w")
    # myfile.write(mydata)


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in."""

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
    """Log user out."""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/login")


@app.route("/survey", methods=["GET", "POST"])
@login_required
def survey():
    """Display survey and submit answers to database."""

    # POST
    if request.method == "POST":

        # Validate form submission
        for field in ["name", "time", "WP","scent","romance","island","toy","game","actor","places","joke"]:
            value = request.form.get(field)
            if not value:
                return apology(f"You must specify your {field}.")

        db.execute ("INSERT INTO results (user_id, name, time, WP, scent, romance, island, toy, game, actor, places, joke) VALUES (:user_id, :name, :time, :WP, :scent, :romance, :island, :toy, :game, :actor, :places, :joke)",
                       user_id=session['user_id'], name=request.form.get('name'), time=request.form.get('time'),
                       WP=request.form.get('WP'), scent=request.form.get('scent'), romance=request.form.get('romance'),
                       island=request.form.get('island'), toy=request.form.get('toy'), game=request.form.get('game'),
                       actor=request.form.get('actor'), places=request.form.get('places'), joke=request.form.get('joke'))

        rows_r = db.execute ("SELECT time, WP, scent, romance, island, toy, game, actor, places, joke FROM results WHERE user_id=:user_id ORDER BY id DESC", user_id=session['user_id'])
        # but only the most recent input??
        results = list(rows_r[0].values())
        counter = [0,0,0,0,0,0,0,0,0,0]
        i = 0
        rows_a = db.execute ("SELECT time, WP, scent, romance, island, toys, game, actor, places, jokes FROM Activities")
        for row in rows_a:
            solutions = list(row.values())
            for item in solutions:
                if item == results[solutions.index(item)]:
                    counter[i] += 1
            i += 1
        maxelement = max(counter)
        print(counter)
        print(maxelement)
        activitynumber = counter.index(maxelement)
        print(activitynumber)

        # Display results depending on which activity they are assigned
        if activitynumber == 0:
            # Get personality from SQL
            things = db.execute ("SELECT personality, description FROM Activities WHERE ac )
            print(things)
            # Get description from SQL

            return render_template("results.html")

    # GET information from user
    else:
        return render_template("survey.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user for an account."""

    # POST
    if request.method == "POST":

        # Validate form submission
        if not request.form.get("username"):
            return apology("missing username")
        elif not request.form.get("password"):
            return apology("missing password")
        elif request.form.get("password") != request.form.get("confirmation"):
            return apology("passwords don't match")

        # Add user to database
        id = db.execute("INSERT INTO users (username, hash) VALUES(:username, :hash)",
                        username=request.form.get("username"),
                        hash=generate_password_hash(request.form.get("password")))
        if not id:
            return apology("username taken")

        # Log user in
        session["user_id"] = id

        # Let user know they're registered
        flash("Registered!")
        return redirect("/")

    # GET
    else:
        return render_template("register.html")


def errorhandler(e):
    """Handle error"""
    return apology(e.name, e.code)


# listen for errors
for code in default_exceptions:
    app.errorhandler(code)(errorhandler)
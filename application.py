import os
import requests
import xml.etree.ElementTree as ET
import csv
import re

from cs50 import SQL
from flask import Flask, flash, jsonify, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.exceptions import default_exceptions
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required, loadRSS, parseXML, savetoCSV, striptag

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

    # Load rss from web to update existing xml file with future events in Boston
    loadRSS()

    # Parse xml file
    events = parseXML('file.xml')

    # Store news items in a csv file
    savetoCSV(events, 'events.csv')

    # Write each row of csv file into row of html table in events.html
    results = []
    file = open("events.csv", "r")
    reader = csv.DictReader(file)
    results = list(reader)
    # Strip descriptions of xml tags
    for result in results:
        result["description"] = striptag(result["description"])
    file.close()
    return render_template("events.html", results=results)
    # Write API results into file by looking up future boston events through eventful's API


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
        for field in ["name", "time", "WP", "scent", "romance", "island", "toy", "game", "actor", "places", "joke"]:
            value = request.form.get(field)
            if not value:
                return apology(f"You must specify your {field}.")

        # Add the user's survey results into the "results" SQL table
        db.execute("INSERT INTO results (user_id, name, time, WP, scent, romance, island, toy, game, actor, places, joke) VALUES (:user_id, :name, :time, :WP, :scent, :romance, :island, :toy, :game, :actor, :places, :joke)",
                   user_id=session['user_id'], name=request.form.get('name'), time=request.form.get('time'),
                   WP=request.form.get('WP'), scent=request.form.get('scent'), romance=request.form.get('romance'),
                   island=request.form.get('island'), toy=request.form.get('toy'), game=request.form.get('game'),
                   actor=request.form.get('actor'), places=request.form.get('places'), joke=request.form.get('joke'))

        # Find the activity that the user's results are most similar to
        rows_r = db.execute(
            "SELECT time, WP, scent, romance, island, toy, game, actor, places, joke FROM results WHERE user_id=:user_id ORDER BY id DESC", user_id=session['user_id'])
        results = list(rows_r[0].values())
        counter = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        i = 0
        rows_a = db.execute("SELECT time, WP, scent, romance, island, toys, game, actor, places, jokes FROM Activities")
        for row in rows_a:
            solutions = list(row.values())
            for item in solutions:
                if item == results[solutions.index(item)]:
                    counter[i] += 1
            i += 1
        maxelement = max(counter)
        activitynumber = counter.index(maxelement)

        # Display results depending on which activity they are assigned
        im = []
        extra = []
        # Attach images
        im.insert(0, "https://upload.wikimedia.org/wikipedia/commons/thumb/6/6d/Good_Food_Display_-_NCI_Visuals_Online.jpg/1200px-Good_Food_Display_-_NCI_Visuals_Online.jpg")
        im.insert(1, "http://blakesnow.com/wp-content/uploads/sites/2/2012/08/how-to-eat-well-12-simple-rules-for-healthy-happy-eating1.jpg")
        im.insert(2, "https://assets.visitphilly.com/wp-content/uploads/2018/02/Rothman-Ice-Rink-SkatingCouple-J.Fusco-VP-2200x1237.jpg")
        im.insert(3, "https://s.abcnews.com/images/Blotter/figure-skates-gty-er-180309_16x9_992.jpg")
        im.insert(4, "https://upload.wikimedia.org/wikipedia/commons/thumb/b/b3/Museumofsciencebostonaugust2005.jpg/1200px-Museumofsciencebostonaugust2005.jpg")
        im.insert(5, "https://dhproviders.org/wp-content/uploads/2016/06/montshire2-1024x576-1024x576.jpg")
        im.insert(6, "https://media-cdn.tripadvisor.com/media/photo-s/04/9b/5a/7e/like-a-fairytale.jpg")
        im.insert(7, "http://www.brooklinerec.com/ImageRepository/Path?filePath=%2Fdocuments%5CIntranet%5C74%2Fshelter+1_201412151129240893.JPG")
        im.insert(8, "https://cdn2.i-scmp.com/sites/default/files/styles/980x551/public/images/methode/2018/01/12/cca30dca-f5d3-11e7-8693-80d4e18fb3a2_1280x720_174449.JPG?itok=XBUtodCB")
        im.insert(9, "https://d2v9y0dukr6mq2.cloudfront.net/video/thumbnail/2O0VXeG/close-up-of-happy-business-people-laughing-and-clapping-in-office_e2z9jqowx__F0007.png")
        im.insert(10, "http://www.shadyoaksinn.com/Content/images/localevents_banner.jpg")
        im.insert(11, "http://hi4csr.com/media/57179/local_main.jpg")
        im.insert(12, "https://res.klook.com/images/fl_lossy.progressive,q_65/c_fill,w_1200,h_630,f_auto/w_80,x_15,y_15,g_south_west,l_klook_water/activities/0d30ec5e-Aquarium/SEAAquariumTicketSentosa,Singapore.jpg")
        im.insert(13, "https://www.virginiaaquarium.com/Lists/Slider/Attachments/2/1920x1080_0005_vaq-03_opt.jpg")
        im.insert(14, "https://timedotcom.files.wordpress.com/2015/01/empty-theater.jpg")
        im.insert(15, "https://cdn.vox-cdn.com/thumbor/WlZmwHgESC-GajzWVFT3dqdsiFU=/0x0:960x640/1200x800/filters:focal(458x166:610x318)/cdn.vox-cdn.com/uploads/chorus_image/image/59978055/Alamo_Drafthouse.0.jpg")
        im.insert(16, "https://media.indiedb.com/images/games/1/27/26732/TheUnknownSplashScreen.png")
        im.insert(17, "https://static1.squarespace.com/static/5451c777e4b0d6fb473314a6/5457b6e9e4b0bd88530dda91/58861e8829687f5efc85d196/1485184649598/Surprise+Box.jpg?format=1000w")
        im.insert(18, "https://www.barnesandnoble.com/blog/barnesy/wp-content/uploads/2013/09/bookliar.gif")
        im.insert(19, "https://cdn.mercyhome.org/wp-content/uploads/2015/06/girl-reading-pile-of-books.jpg")
        extra.insert(0, "https://boston.eater.com/maps/best-restaurants-boston-38")
        extra.insert(1, "https://bostonfrogpond.com/winter-programs/pricing-season-passes/")
        extra.insert(2, "https://www.mos.org/explore")
        extra.insert(3, "https://www.brooklinema.gov/Facilities/Facility/Details/Larz-Anderson-Park-87")
        extra.insert(4, "http://www.laughboston.com/")
        extra.insert(5, "/events")
        extra.insert(6, "https://www.neaq.org/")
        extra.insert(7, "https://www.fandango.com/")
        extra.insert(8, "https://www.atlasobscura.com/things-to-do/cambridge-massachusetts")
        extra.insert(9, "https://www.mfwi.edu/MFWI/Recordings/Green%20Eggs%20and%20Ham.pdf")
        for i in range(10):
            if activitynumber == i:
                # Get personality and description from SQL
                info = db.execute("SELECT personality, description FROM Activities WHERE id=%s" % i)
                personality = info[0]['personality']
                description = info[0]['description']
                results = db.execute("SELECT name FROM results WHERE user_id=:user_id ORDER BY id DESC", user_id=session['user_id'])
                name = results[0]['name']

                # Transfer information to the results HTML page
                return render_template("results.html", personality=personality, description=description, im1=im[2*i], im2=im[(2*i)+1], name=name, extra=extra[i])


    # If not POST, return the user to the survey
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
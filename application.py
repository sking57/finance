import cs50
import csv

from flask import Flask, jsonify, redirect, render_template, request

# Configure application
app = Flask(__name__)

# Reload templates when they are changed
app.config["TEMPLATES_AUTO_RELOAD"] = True


@app.after_request
def after_request(response):
    """Disable caching"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/", methods=["GET"])
def get_index():
    return redirect("/form")


@app.route("/form", methods=["GET"])
def get_form():
    return render_template("form.html")


@app.route("/form", methods=["POST"])
def post_form():
    # validate proper usage
    if not request.form.get("firstname") or not request.form.get("lastname") or not request.form.get("scent") or not request.form.get("cheese") or not request.form.get("gradyear"):
        return render_template("error.html", message="You must provide values for all fields!")
    # write the form's value into a new row of the csv file (from lecture notes)
    file = open("survey.csv", "a")
    writer = csv.writer(file)
    writer.writerow((request.form.get("firstname"), request.form.get("lastname"), request.form.get("scent"), request.form.get("cheese"), request.form.get("gradyear")))
    file.close()
    # redirect user to the sheet route
    return redirect("/sheet")


@app.route("/sheet", methods=["GET"])
def get_sheet():
    results = []
    file = open("survey.csv", "r")
    reader = csv.DictReader(file)
    results = list(reader)
    return render_template("registered.html", results=results)
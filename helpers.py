import requests
import urllib.parse
import csv
import xml.etree.ElementTree as ET

from flask import redirect, render_template, request, session
from functools import wraps


def apology(message, code=400):
    """Render message as an apology to user."""
    def escape(s):
        """
        Escape special characters.

        https://github.com/jacebrowning/memegen#special-characters
        """
        for old, new in [("-", "--"), (" ", "-"), ("_", "__"), ("?", "~q"),
                         ("%", "~p"), ("#", "~h"), ("/", "~s"), ("\"", "''")]:
            s = s.replace(old, new)
        return s
    return render_template("apology.html", top=code, bottom=escape(message)), code


def login_required(f):
    """
    Decorate routes to require login.

    http://flask.pocoo.org/docs/1.0/patterns/viewdecorators/
    """
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get("user_id") is None:
            return redirect("/login")
        return f(*args, **kwargs)
    return decorated_function


def loadRSS():
    # load file
    response = requests.get("http://api.eventful.com/rest/events/search?app_key=5z7c7Pw3d6MCSWKf&location=Boston&date=Future")
    # saving the xml file
    with open('file.xml', 'wb') as f:
        f.write(response.content)

# source for below: https://www.geeksforgeeks.org/xml-parsing-python/


def parseXML(xmlfile):
    # parse file
    tree = ET.parse("file.xml")
    root = tree.getroot()
    events = []
    # fill up array with values for each event from API results
    for item in root.findall('./events/event'):
        # empty info dictionary
        info = {}
        for child in item:
            if child.text:
                if child.tag == 'title' or child.tag == 'url' or child.tag == 'description' or child.tag == 'start_time' or child.tag == 'venue_address' or child.tag == 'city_name':
                    info[child.tag] = child.text
        # append info dictionary to events items list
        events.append(info)
    # return news items list
    return events


def savetoCSV(events, filename):

    # specifying the fields for csv file
    fields = ['title', 'url', 'description', 'start_time', 'venue_address', 'city_name', 'region_abbr']

    # writing to csv file
    with open(filename, 'w', encoding='utf8') as csvfile:

        # creating a csv dict writer object
        writer = csv.DictWriter(csvfile, fieldnames=fields)

        # writing headers (field names)
        writer.writeheader()

        # writing data rows
        writer.writerows(events)


def striptag(s):

    # replace all occurances of &#39; with ' (the ASCII translation)
    old = "&#39;"
    new = "'"
    st = s.replace(old, new)

    # convert string to list of words
    s_list = list(st)
    i = 0
    while i < len(s_list):
        # iterate until a left-angle bracket is found
        if s_list[i] == '<':
            while s_list[i] != '>':
                # return everything between the 2 brackets
                s_list.pop(i)
            # pops the right-angle bracket
            s_list.pop(i)
        else:
            i = i+1
    # convert the list back into text
    join_char = ''
    return join_char.join(s_list)


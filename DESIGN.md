The first step of our implementation was duplicating our code from finance in order to have a rough skeleton of a website. We replaced
most of the routes in application.py with our own logic and also replaced most of the html files with our own (with the exception of
login and register code). There were a few components to building our website: creating the survey, developing an algorithm
to match user results with different activities in our database, and retrieving information about local events in Boston using an API
from Eventful. The latter portion is essentially an extra feature of the website that we added as a special touch.

To create our survey we used HTML to display 10 different questions, each of which is a radio button, and then one text question for the user's name.
Each question has 4 different options and the options have a value of 1, 2, 3, and then 4. This value system makes it easier to input the info into
the table and then compare to other information, as we will do later. We then made a table in SQL called "results", which has a different
column for each of the user's inputted answers to the survey, along with a column for user_id and id (which was automatically incremented
but ordered by descending numbers). This id part was necessary so that the same user could take the survey multiple times and we could
just use the results with the highest id number. So, when the user submits the survey, their results are put into this table. Therefore,
the 10 columns of the table for each of the 10 questions each have either a 1, 2, 3, or 4 in them.

To match the user's results with an activity, we decided to continue using SQL. This is considerably easier than using a CSV file and allowed us to
create multiple databases where we could then compare information. We decided to treat each activity like its own response to the survey, so we could
then compare which activity was most similar to the response by the user. We created one table called "Activities" where each of the 10 activities
are listed with the answers from the survey that fit that activity best, along with a description of the personality of someone who would choose
those answers, and a description of the activity.

Now for the algorithm to determine which activity matches this user's results best. We first extracted the user's most recent survey answers
by using db.execute SELECT and choosing only their user_id and ordering from highest to lowest id number (the most recent submission) and called it
"results." Then, we extracted all of the answers to the survey from each activity and called this "rows_a." We then created a counter called "counter"
that is an array of 10 values, all starting at 0. Each 0 corresponds to a question in the survey. We use this to track how many of the answers are
similar between each activity and the user's answers. Each value is referenced with counter[i], and i starts at 0 because this references the first
question in the survey. We then iterated through "rows_a" in order to go through each activity and then iterate through the answer to each question
for each activity. We checked if this activity's answer to the question was the same as the user's answer to the question. If so, we increased the
counter by 1. This is done for all 10 questions for each activity, then we move on to the next activity and i increases by 1, so we move to the second
element in the "counter" array. Once this process is done, we are left with counter, an array of 10 numbers, where each element in the array
shows how many questions the user had in common with each activity. We then used the max and index function to find which activity had
the highest similarity, and therefore it is the winner!

In order to display the results to the user, we used one common html page called "results.html". We used jinja to reference parts of the page that
dynamically update depending on how the user answered the survey and what activity they were matched with. These items are name, personality,
description, extra (the url), and 2 images. Then, in python, we did 10 if statements for each different possible activity. For example, if the activity
number outputted by the algorithm explained above is 0, it means that the assigned activity is "food." So, we extract the necessary information from
this row in the "activities" SQL table, the user's name from the "results" table, provide links to websites and images, and then pass this information
into "results.html". This process is repeated toproduce 10 unique results pages. We decided that this route was more efficient than creating a different
html page for each activity, because this way there is only 1 template and we can just input different information.

After implementing the survey part of the project, we decided our website could go one step further in its functionality. We realized that
the user might not always be fully satisfied with just one suggested acivity; no matter how good our algorithm is, we'll never be psychic.
Some users are lucky enough to get the activity that directs them to the "local events" tab, but we believed that all users should be able to
access this. That is why we decided to also provide users with information about local events on our website. To do this, we considered manually
inputting events, but realized that these things are constantly updating and therefore our website needs to be constantly updating according to these
changes. The solution to this problem was to use an API to get local events from the server of a website like eventful that has this information.
The first step of using Eventful's API was to register for an Eventful account in order to receive an access key. Once this was done,
we were able to request the information on Eventful's site from the server, and the server was able to send the information back (the goal
of APIs). The API link we used was http://api.eventful.com/rest/events/search?app_key=5z7c7Pw3d6MCSWKf&location=Boston&date=Future, which
contained information about our access key, type of information we want from Eventful (the results of an event search), the location of
interest (Boston), and the time of interest (the future). This /events/search is what specified the method we wanted to use. This
function performs the requested search and returns the results as an XML file. In helpers.py, we implemented three functions: the first
gets the XML response by calling the API link and reads this data into an xml file called file.xml; the second parses through this file and creates a
list of dictionaries, one for each event in the XML file, whose key values specify things like title, description, url, date, etc. and returns
this list of dictionaries; the third writes each dictionary into a row of a csv file called events.csv with fieldnames that match up
with key value names for the results dicts (similar to what we did in pset7). In application.py, we then pass each row of this csv file
into the events.html file (we do this in the line of code that returns this html template). This html file has jinja code that iterates
through each dictionary and prints the values of each category into its corresponding column (so all of the values for the title key
go under the title column of the table in separate rows, etc.). Finally, the final function we implemented in helpers serves to clean up
the descriptions we pulled from the XML files by replacing the ASCII value &#39; with what it's alphabetical value is (an apostrophe) and
to also remove the HTML/XML tags from the strings (without this, tags like <strong> and <p> were appearing throughout
the event descriptions in the table, which was ugly and less easy to read). The way it works is that it iterate through each word in the text
and pops out the characters of each word that are between the < and > symbols.


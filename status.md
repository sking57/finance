# Status Report

#### Your name

Nellie Ide

#### Your section leader's name

Toby Satterthwaite

#### Project title

Fun Finder

***

Short answers for the below questions suffice. If you want to alter your plan for your project (and obtain approval for the same), be sure to email your section leader directly!

#### What have you done for your project so far?

We have set up the basic skeleton of the website, like the html files and application.py. The ability to register, log in, and log out
are implemented. Additionally, we have gathered a list of websites that contain information we want to access and have done research
into web scraping and APIs and are starting to form a plan of how to get the data we want.

#### What have you not done for your project yet?

We haven't figured out exactly how we're going to get data from websites and display them on ours. We have to look into the legality
of web scraping. Also, we have to decide what survey questions to ask and figure out an algorithm to use in order to generate a plan
for the user. We also need to design an html page displaying these results. We also need to update our SQL databases (might need one
containing user information and one containing self-inputted information about events)

TODO (some extra notes)
- input all answers into a SQL database
- another SQL database with the activities and have each row correlate with certain answers
- so each activity has an ID just like a user and once the user inputs their answers, we will use a for loop to go through their answers one by one
  and compare them to the answers of the activity options. Every time the answer is the same, a counter will increase by 1.
  When this process is complete for all answers of all activities, the activity with the highest counter will be the one we propose.
- also have a SQL table for info about each activity
- when the activity is selected, link to a new html page (results.html) and possibly pass in info for each activity, like different images, hours, etc.
- for questions like food and museum where there are multiple options within it, we can have one question that determines which of the 4 options they go to

#### What problems, if any, have you encountered?

We can't figure out how to have radio buttons with images instead of words. Also, we aren't sure how to web scrape yet and are
pretty confused about that aspect of things.
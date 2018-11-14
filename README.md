# Proposal

## What will (likely) be the title of your project?

fun finder



## In just a sentence or two, summarize your project. (E.g., "A website that lets you buy and sell stocks.")

A website where you take a survey and it suggests a fun activity for you to do based off your survey answers. Information about the activity will be provided to help you get out there and do it!

## In a paragraph or more, detail your project. What will your software do? What features will it have? How will it be executed?

The first part of our project is to develop a survey using HTML. This survey will have probably around 10 multiple choice questions. These questions will vary - some will be funny and seemingly random, while others will be more serious and clearly related to which activity the person can do.
Our website will have a SQL table that stores the survey results of different possible activities. Each activity may have different survey results that would lead to it, but every possible combination of answers will be accounted for here.
When the user submits the survey, their results will be stored in a SQL table. These results will then be compared to the results that correspond to the different possible activities we have in our database and the closest match will be found with logic in python similar to logic used in datamatch (we will have a conversation with someone who worked on the algorithm of data match soon).

Once this match is found, the second part of the project is to suggest a detailed activity for the user.
We will explain why this activity was chosen for the user based off of their answers by using the survey results that are associated with the activity.
Then, each different activity will have their own HTML page of the website where we will explain the activity using pictures and features of CSS and bootstrap to make it look appealing.
Ideally, this page will include extra information about the activity that is retrieved from a particular website and is updated when the information changes.
For example, this could be show times for a movie theater, a menu from a restaurant, or the hours of an trampoline park, using the API of different websites.



## If planning to combine CS50's final project with another course's final project, with which other course? And which aspect(s) of your proposed project would relate to CS50, and which aspect(s) would relate to the other course?

N/A

## In the world of software, most everything takes longer to implement than you expect. And so it's not uncommon to accomplish less in a fixed amount of time than you hope.

### In a sentence (or list of features), define a GOOD outcome for your final project. I.e., what WILL you accomplish no matter what?

No matter what, we will have a form for the user to submit answers to, we will put this information into a SQL database, and we will use this information to logically decide which activity to give the user. Our recommendations for the user will be provided on a new page, which will include suggestions on what to do, an average of how much money it will cost, and at least a link to the website of places we recommend.

### In a sentence (or list of features), define a BETTER outcome for your final project. I.e., what do you THINK you can accomplish before the final project's deadline?

In addition to the basic functionality, ideally we will be able to figure out how to access information from websites of movie theaters, restaurants, bowling alley’s etc. with their API’s. This way, we won’t have to include links for our users to go to when we recommend activities for them -- we can just give them all the information they would want on our own site, such as movie times and store hours. A similar feature that we would like to add is updating the events based off of what is happening in Cambridge at the moment.
### In a sentence (or list of features), define a BEST outcome for your final project. I.e., what do you HOPE to accomplish before the final project's deadline?

One hope we have is that the project will also include information in its recommendations about HOW to get to the activity, and what the best/most efficient form of transportation to get to the activity. This could mean showing the walking route or how to take the T or suggesting that the user just call an uber. We will need to use google maps API for this, which is something that could be feasible considering something  similar was on a past pset (or so we’re told).
We also hope that our website will live outside of the IDE as its own website. An additional goal is that our website will be very aesthetically pleasing, but this is an outcome that we will only pursue once we get basic functionality down.

## In a paragraph or more, outline your next steps. What new skills will you need to acquire? What topics will you need to research? If working with one of two classmates, who will do what?

We will need to do research on different algorithms that will match people up with activities. This could involve looking at websites such as BuzzFeed that use similar surveys, or reaching out to the creators of datamatch to see how their algorithm works. Nellie will focus on this aspect.
We also will need to research how to access the API of other websites and implement that information in our own website. We will try to understand how the peak app works because that app seems to gather the same type of data we want to from other websites.
We also want to research how we can make our website live outside of the IDE and how to implement that, because it seems silly for our website to only work when flask is open and running on one of our computers. Sarah will focus on these last two aspects.

peak app:
https://itunes.apple.com/us/app/peek-tours-activities/id767696645?mt=8

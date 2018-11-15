# False Alarm

## Questions

2.1. The biggest flaw of this design is that it doesn't separate the drills from the real warnings. These things are drastically different
and should not be anywhere near each other. The distinction should be way more clear. There should at least be a header saying something like
"Drill" for the drills and "real emergency" for the real alarms

2.2. Of course, the human should take some blame for this. If they were taking their job seriously enough, they would not have clicked
the Pacom State Warning over the Drill Pacom State Warning. Clearly, they did not read through their choices enough and jumped to
conclusions when they saw Pacom State Warning. However, as we learn in CS50, NEVER trust humans. They're way too flawed. The person who
did this could've been having a really bad day or maybe was exhausted or maybe was wearing a really bad prescription. Programmers have
to expect the worst of humans, and therefore there should be way more separation between the drill and non-drill in order to save the
human from making this mistake. This is mostly the fault of the lazily-designed UI.

2.3a. I would create an entirely new set of HTML docs: one for drill warnings, and one for real warnings. Before someone can even see the
different types of warnings, a form should be displayed in which they should have to select the type of warning (through a select menu or
button or any other type of input) they want to see and only be shown those. Only when they submit this form can they be redirected to
the form showing the different types of warnings of the category they selected (whether it be drill warnings or real ones).
Essentially, the information needs to be separated by being split to multiple different pages so that the types of warnings don't get confused
and the user doesn't select something they didn't intend to. if I had to keep everything on one page, I would distinguish the warnings
from the drills as much as possible by putting clear headings before the warnings to denote which ones are drills and which are real.

2.3b. I would use CSS to emphasize the real warnings more than the drill warnings. I would do this by making the real warning text bolder,
larger, and maybe even red. As much attention as possible needs to be drawn to the real warnings so that they don't get confused with the
drills. Also, if I had to keep everything on one page, I would separate the warnings from the drills as much as possible, maybe even give
the real warnings a special, bold, red border.

2.3c. To confirm, client-side, that the user selected what they meant to, I would use javascript to print an alert, at submission of the user,
that basically requires the user to confirm that they selected what they meant to. The alert would be clear stating that "you selected to send
a real warning out to the entire state, which will cause a lot of concern. Is this correct?" or "you selected to send a drill alert to the state.
Is it true that you don't want to send a real warning?"

2.4. SQL could be used to store a user id, username, and a hash of the user's password so that every user has to log in and their credentials
have to be verified (checked by backend logic) in order to use the application. To get oneself in the database in the first place, one must
go through a specific and long register process to validate their access to such an important program.

2.5. Well first of all, humans will always be prone to making mistakes, so there are infinitely many trivial things that could go wrong and
lead to utter chaos (user misread the screen due to poor eyesight, fell asleep on keyboard and pressed a bunch of buttons, etc.).
In a programming sense, however, if the user were to turn off javascript in the browser, then no pop-up warning would appear, and the user
could still set off the alarm by accident because they were not stopped to confirm. Additionally, like what happened with the facebook
security issue, an attacker could gain access to the access token of the user if there is a vulnerability in the code. This attacker could
then get into the program and purposefully set off the alarm. Finally, if there are session cookies being used to keep the user logged in
for a while, someone random could get on the computer, not have to log in to this application (because cookies remembers the computer),
and then set off the alarm.

a. The links provided were helpful, as were lecture notes

b. 45 minutes

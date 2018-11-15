# View as

## Questions

9.1. Access tokens are pieces of data that store credential information about users, including their login information and the access they have
to different websites' APIs. They are used to make these requests, and authorize these specific applications to access the users' information.
With the increasing use of APIs, access tokens are becoming quite popular.

9.2. There were perhaps bugs in the View as code that didn't protect the confidentiality that access tokens are supposed to have. The View As
feature is designed to let you see what your profile looks like in the eyes of the public/your friends. However, there was a bug in the code
that incorrectly allowed people to post videos while in the View As mode. When uploading a video here, access tokens were generated that
gave access to the mobile facebook app, and, incorrectly, an access token for the user you looked up was generated rather than your own access
token. This access token was then available on the HTML of the page for attackers to find.

9.3. Facebook logged people out because it had to reset access tokens for the millions of people that were attacked and, in addition, the millions of people that had
used the View As featuer before. Once people logged back in, they received a new access code.

9.4 Session cookies store secure authentication information both server-side and client side, while access tokens are stateless and
therefore the server keeps no record of who is loggen in. Instead, every request to the server is joined by an access token and its authenticity
is then verfied by the server.

## Debrief
a. I found the links in the specs very helpful and also I used this website: https://dzone.com/articles/cookies-vs-tokens-the-definitive-guide

b. 45 minutes
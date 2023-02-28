# The_Reddit_Api

Assignment Description:
The Reddit API (20 points)
Reddit is a popular social media service used by many students and the occasional instructor. Content
such as links, text posts, images and videos can be submitted to the site under different user-created
subsections of the site (known as ‘subreddits’). Each piece of posted content is known as a ‘topic’ and
has its own webpage on the site. Each topic can be voted on and discussed by the community in a series
of replies on its particular page.
Reddit also provides an API, Application Programming Interface, to users. An API allows a computer
program to interact with an application (or website) instead of a user interacting with it directly.
An API, especially an API for a website, is often designed to be language-agnostic. That is, it can be
used by programs written in many different languages. Helper code (as part of a library) is then written
in a particular language to serve as a bridge between the API and code written in that language. Reddit
has an API which can be used in Python through the use of a special library called PRAW.
To begin this assignment, you must install the praw library into Thonny, using the same steps as done
for the libraries needed for Assignment 2.
PRAW lets us access the Reddit API and do such things as list the topics in a subreddit, list the replies
for a topic, and even make new replies to posts, all from within our Python code. To use PRAW, you must
first create a new Reddit account at https://www.reddit.com. Do not use an existing account.
Your choice of Reddit username is entirely up to you and does not have to include your real name or
any personal information, but as part of your username you must include the word ‘bot’.
After creating an account, we must obtain some extra information in order to use the API. Visit https:
//www.reddit.com/prefs/apps and click the ‘are you a developer? create an app...’ button in the middle
of the page. Select the ‘script’ radio button, and enter a name (could be anything). For the redirect
URI, use ‘http://localhost:8080’. Click the button to create the app, and the page will refresh. Make a
note of the text next to ‘secret’ (we will call this the client secret), and also the text under ‘personal use
script’ (we will call this the client ID).
After obtaining the information, create a file called praw.ini in a new folder in which you will store your
files for this assignment. Include the following in this file. After each equals sign, include the relevant
piece of information, including the username and password for your new Reddit account and the client
ID and secret. The User Agent should be of the form “<your OS>:<client ID>:1.0 (by /u/<your reddit
username>)”. The information stored in this file will let PRAW connect to the Reddit API using your new
account credentials.


Bot:

This bot currently pulls the top 25 comments from subreddit 'test' and for each instance of the word 'joke' responds
with a joke using the Chuck Norris API.

To Run:

- Install python modules: os, time, praw, requests
- Add config.py file containing the following credentials (obtained from reddit account and created script app credentials)

username = ""
password = ""
client_id = ""
client_secret = ""

run from command line with - python r_bot.py

Notifier:

Uses file containing usernames to send a private message to a reddit user

example useage: python notifier.py usernames.txt "Test comment" "Test comment body"

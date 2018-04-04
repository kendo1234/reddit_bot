import praw
import config
import time
import os
import requests


def bot_login():
    #Log in using reddit credentials
    print("Logging in...")
    r = praw.Reddit(username=config.username,
                    password=config.password,
                    client_id=config.client_id,
                    client_secret=config.client_secret,
                    user_agent="reddit_bot by Ken /u/kendomustdie")
    print("Logged in!")

    return r


def run_bot(r, comments_replied_to):
    print("Obtaining 25 comments...")
# Takes obtained comments and for every instance of the word 'joke', uses the icndb API to post a chuck norris joke in reply
    for comment in r.subreddit('test').comments(limit=10):
        if "!joke" in comment.body and comment.id not in comments_replied_to and comment.author != r.user.me():
            print("String with \"!joke\" found in comment " + comment.id)

            comment_reply = "You requested a Chuck Norris joke! Here it is:\n\n"
            # Using the API to get the joke
            joke = requests.get('http://api.icndb.com/jokes/random').json()['value']['joke']

            comment_reply += ">" + joke

            comment_reply += "\n\nThis joke came from [ICNDb.com](http://icndb.com)."

            comment.reply(comment_reply)
            print("Replied to comment " + comment.id)

            comments_replied_to.append(comment.id)
            #writes the comment id's replied to in a text file
            with open("comments_replied_to.txt", "a") as f:
                f.write(comment.id + "\n")

    print("Sleeping for 10 seconds...")
    # Sleep for 10 seconds after each attempt to grab comments...
    time.sleep(10)

# Creates a text file to write obtained and replied to comments
def get_saved_comments():
    if not os.path.isfile("comments_replied_to.txt"):
        comments_replied_to = []
    else:
        with open("comments_replied_to.txt", "r") as f:
            comments_replied_to = f.read()
            comments_replied_to = comments_replied_to.split("\n")
            comments_replied_to = filter(None, comments_replied_to)

    return comments_replied_to


r = bot_login()
comments_replied_to = get_saved_comments()
print(comments_replied_to)

while True:
    run_bot(r, comments_replied_to)

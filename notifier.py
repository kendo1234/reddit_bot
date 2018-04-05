import praw
import config
import sys
import time

#Login function
def authenticate():
    # Log in using reddit credentials
    print("Logging in...")
    reddit = praw.Reddit(username=config.username,
                         password=config.password,
                         client_id=config.client_id,
                         client_secret=config.client_secret,
                         user_agent="reddit_notifier_bot by Ken /u/kendomustdie")
    print("Authenticated as {}".format(reddit.user.me()))

    return reddit

#Look for file usernames.txt
def get_usernames(filename):
    try:
        with open(filename, "r") as f:
            usernames = f.read()
            usernames = usernames.split("\n")
            usernames = filter(None, usernames)
    except IOError:
        print("Error: File " + filename + " was not found in the current directory")
        quit()

    return usernames

#Send reddit PM based on arguments passed in at runtime, catch the exception if user not found
def send_message(r, username, subject, body):
    try:
        r.redditor(username).message(subject, body)
    except praw.exceptions.APIException as e:
        if "USER_DOESNT_EXIST" in e.args[0]:
            print("redditor " + username + " not found, did not send a message.")
            return

    print("Sent message to " + username + "!")

#Arguments to pass in when running
if len(sys.argv) != 4:
    print("usage: notifier.py file \"subject\" \"body\"")

filename = sys.argv[1]
subject = sys.argv[2]
body = sys.argv[3]

reddit = authenticate()
usernames = get_usernames(filename)

for username in usernames:
    send_message(reddit, username, subject, body)
    #Sleep after each send to avoid spamming
    time.sleep(5)

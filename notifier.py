import praw
import config
import sys

def authenticate():
    #Log in using reddit credentials
    print("Logging in...")
    reddit = praw.Reddit(username=config.username,
                    password=config.password,
                    client_id=config.client_id,
                    client_secret=config.client_secret,
                    user_agent="reddit_notifier_bot by Ken /u/kendomustdie")
    print("Authenticated as {}".format(reddit.user.me()))

    return reddit

def get_usernames(filename):
    try:
        with open(filename, "r") as f:
            usernames = f.read()
            usernames = usernames.split("\n")
            usernames = filter(None, usernames)
    except IOError:
        print("Error: File " + filename + " was not found int he current directory")
        quit()

        return usernames

if not len(sys.argv) == 4:
    print("usage: notifier_bot.py file \"subject\" \"body\"")

    filename = sys.argv[1]
    subject = sys.argv[2]
    body = sys.argv[3]

reddit = authenticate()
usernames = get_usernames(filename)
print(usernames)



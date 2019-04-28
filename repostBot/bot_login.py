import praw
import os

def bot_login():
    reddit = praw.Reddit(client_id = os.environ.get("client_id"),
                client_secret = os.environ.get("client_secret"),
                user_agent = 'PRAW API tutorial Python Script',
                username = os.environ.get("reddit_username"),
                password = os.environ.get("reddit_password"))   
                
    print("logged in!")

    return reddit

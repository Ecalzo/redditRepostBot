import praw
import os
from boto.s3.connection import S3Connection

def bot_login():
    reddit = praw.Reddit(client_id = os.environ["client_id"],
                client_secret = os.environ["client_secret"],
                user_agent = 'PRAW API tutorial Python Script',
                username = os.environ["reddit_username"],
                password = os.environ["reddit_password"])   
                
    print("logged in!")

    return reddit

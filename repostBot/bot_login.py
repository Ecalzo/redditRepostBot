import praw
import os
from boto.s3.connection import S3Connection

def bot_login():
    reddit = praw.Reddit(client_id = S3Connection(os.environ["client_id"]),
                client_secret = S3Connection(os.environ["client_secret"]),
                user_agent = 'PRAW API tutorial Python Script',
                username = S3Connection(os.environ["reddit_username"]),
                password = S3Connection(os.environ["reddit_password"]))   
                
    print("logged in!")

    return reddit

import time
import praw
import pandas as pd
import bot_login
from datetime import datetime
import pymongo
import mongo_setup

def get_post(sub='pics'):
    '''
    Gets Post data
    Append this output to a list
    '''
    reddit = bot_login.bot_login()
    # Get current time and format:
    current_time = datetime.now().strftime("%m-%d-%Y")
    # dictionary to store the fetched info
    redditInfo = {}
    # obtaining the top post info and passing it to a dict
    # I use limit=2 to skirt past the stickied post
    for submission in reddit.subreddit(sub).hot(limit=2):
        redditInfo['title'] = submission.title
        redditInfo['url'] = submission.url
        redditInfo['subreddit'] = submission.subreddit
        redditInfo['time'] = current_time

    # return the dictionary (to be appended to a list)
    return redditInfo


def submit_post(post_dict):
    '''
    Posts scraped post to the subreddit in the dictionary
    Does not handle non-link (text) posts yet 
    '''
    # this will repost the fetched post and return the post id for later tracking
    submitted = post_dict['subreddit'].submit(title=post_dict['title'], url=post_dict['url'])
    # Append to a list tracking these items
    return submitted
    

def scrape_post_collect():
    # for test purposes, we will try this ten times
    # TODO: change to while true: to run indefinitely
    for _ in range(0,10):
        try:
            print("Getting post")
            # get a top post from r/pics
            post_info = get_post()
            # log for debugging
            print(post_info) 
            # sleep and repost in 24 hours
            time.sleep(86400)
            # resubmit the post
            post_id = submit_post(post_info)
            # append post_id and post_info to a dictionary for later parsing
            print("preparing to append to MongoDB")
            # Creating post dictionary
            post = {}
            # Appending to post in format {post_id:{post_info}}
            post[post_id] = post_info
            # Initialize MongoDB instance
            collection = mongo_setup.mongo_login()
            # insert post into MongoDB Collection
            collection.insert_one(post)
            print("posted something new!")
        except:
            print("failed")
    
# Initialize the main function
if __name__ == "__main__":
    scrape_post_collect()
        
    

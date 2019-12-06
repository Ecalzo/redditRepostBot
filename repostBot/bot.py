import time
import praw
import pandas as pd
import bot_login
from datetime import datetime
import pymongo
import logging
import mongo_setup
import random

logging.basicConfig(filename='main.log',
                    level=logging.INFO,
                    filemode='a',
                    format='%(name)s - %(levelname)s - %(message)s')


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
    randomInt = random.randint(3, 40)
    # obtaining the top post info and passing it to a dict
    # Use the top of the week and go a few posts down
    for submission in reddit.subreddit(sub).top('week', limit=randomInt):
        redditInfo['title'] = submission.title
        redditInfo['url'] = submission.url
        redditInfo['subreddit'] = submission.subreddit
        redditInfo['time'] = current_time
    # Append the overall user karma at this point in time
    # subroutine to clean the user karma
    # (remove objects incompatible with Mongo)
    karma = reddit.user.karma()
    cleaned_karma = {}
    for key, value in karma.items():
        # extract subreddit display name as str
        new_key = key.display_name
        # write to cleaned karma dictionary
        cleaned_karma[new_key] = value
    redditInfo['karma'] = cleaned_karma
    # return the dictionary (to be appended to a list)
    return redditInfo


def submit_post(post_dict):
    '''
    Posts scraped post to the subreddit in the dictionary
    Does not handle non-link (text) posts yet
    '''
    # this will repost the fetched post and return the post id for tracking
    submitted = post_dict['subreddit'].submit(title=post_dict['title'],
                                              url=post_dict['url'])
    # Append to a list tracking these items
    return submitted


def scrape_post_collect():
    # example subreddits - could make these argparse flags
    subreddits = ['pics', 'me_irl', 'dankmemes', 'eyebleach']
    while True:  # better to just schedule this with cron
        for sub in subreddits:
            try:
                print("Getting post")
                # get a top post from r/pics
                post_info = get_post(sub)
                # log for debugging
                logging.info('{} {}'.format(post_info['title'],
                                            post_info['url']))
                print('sleeping... ')
                logging.info('sleeping...')
                # sleep and repost in 24 hours
                time.sleep(12000)
                # resubmit the post
                print('Awake! posting to Reddit!')
                submitted = submit_post(post_info)
                # convert to integer value, not post object
                post_id = submitted.id
                # Convert subreddit name to string to store in MongoDB
                post_info['subreddit'] = post_info['subreddit'].display_name
                print("preparing to append to MongoDB")
                # Creating post dictionary
                post = {}
                # Appending to post in format { post_id: { post_info } }
                post[post_id] = post_info
                # Initialize MongoDB instance and push info
                try:
                    # insert post into MongoDB Collection
                    print('attempting to initalize and push to mongoDB')
                    mongo_setup.mongo_login_and_insert(post)
                except Exception as e:
                    print('could not initialize MongoDB')
                    logging.exception('An Exception Occured')
                print("posted something new at: ", datetime.now())
            except Exception as e:
                print("failed at: ", datetime.now())
                print(e)
                logging.exception('An Exception Occured')


# Initialize the main function
if __name__ == "__main__":
    scrape_post_collect()

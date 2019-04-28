import time
import praw
import pandas as pd
import bot_login

def get_post(sub='pics'):
    '''
    Gets Post data
    Append this output to a list
    '''
    reddit = bot_login.bot_login()
                
    # dictionary to store the fetched info
    redditInfo = {}
    # obtaining the top post info and passing it to a dict
    for submission in reddit.subreddit(sub).hot(limit=2):
        redditInfo['title'] = submission.title
        redditInfo['url'] = submission.url
        redditInfo['subreddit'] = submission.subreddit

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
    posts = {}
    # for test purposes, we will try this four times
    for _ in range(0,1):
        try:
            # get a top post from r/pics
            post_info = get_post()
            # log for debugging
            print(post_info) 
            # sleep and repost in 24 hours
            time.sleep(60)
            # resubmit the post
            post_id = submit_post(post_info)
            # append post_id and post_info to a dictionary for later parsing
            posts[post_id] = post_info
        except:
            print("failed")
    
    df = pd.DataFrame(posts)
    df.to_csv('output.csv')
    print("output to output.csv")

# Initialize the main function
if __name__ == "__main__":
    scrape_post_collect()
        
    

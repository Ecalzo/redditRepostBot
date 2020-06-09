## RepostBot
reddit Bot hosted via Heroku that reposts from r/pics for some sweet sweet karma

## Why?
This bot is built out of a desire to learn the ins and outs of building and deploying a bot securely 

In addition, I wanted to see how easily an account can rack up Reddit "karma" points by simply taking a popular picture and reposting it, a practice commonly called out by reddit users, but often after they have received thousands of (albeit worthless) points.

## Roadmap:
To build on this, I want to leverage Python's Flask library and the Plotly (or plot.js tbd) JS library to build a small web app that tracks the realtime progress and growth (or failure) of this bot. I would also like to extend this bot's capabilities past /r/pics, making it significantly more interesting and dynamic 

## Updates:
* Update 4/30/2019: Bot is in trial period, GitHub code has been updated to push collected post data to MongoDB, however, this repo is not tied to Heroku and the updated bot will be deployed once the trial period has finished. 
* Update 6/8/2019: Some functionality has been added to the bot. It currently cycles through a few subreddits and a random choice function has been included to avoid reposting the same post, decreasing the potential of being detected by an automod. The bot also pushes metadata to a MongoDB database that will eventually be used to build out some real-time visualizations/tracker.

## TODO/ideas:
* Currently, the thing about this program that I dislike the most, is the implementation of the `time.sleep()` function.
* Ideas for scheduling this thing instead and passing metadata:
    * Airflow (2 tasks per subreddit, collect + repost)
    * Cron or similar -> save metadata to pickle files while not running
        * OR Utilize MongoDB
* Would also like to add some CI/CD with circleCI for dag deployment

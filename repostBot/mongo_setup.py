from pymongo import MongoClient
import os

def mongo_login():
    mongo_user = os.getenv("mongo_user")
    mongo_pw = os.getenv("mongo_pw")

    client_url = "mongodb+srv://{}:{}@evancluster-cgyva.mongodb.net/test?retryWrites=true".format(mongo_user,mongo_pw)

    client = MongoClient(client_url)
    db = client.redditBotDB
    collection = db.redditBotCollection
    
    return collection

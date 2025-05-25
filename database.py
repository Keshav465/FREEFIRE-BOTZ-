import os
from pymongo import MongoClient

client = MongoClient(os.getenv("MONGO_URI"))
db = client.like_bot
likes_collection = db.likes

def has_liked_today(uid, date):
    return likes_collection.find_one({"uid": uid, "date": date}) is not None

def save_like(uid, region, date, likes_given):
    likes_collection.insert_one({
        "uid": uid,
        "region": region,
        "date": date,
        "likes_given": likes_given
    })

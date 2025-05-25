import os
from pymongo import MongoClient
pip install python-dotenv pymongo


client = MongoClient(os.getenv("mongodb+srv://keshavrajlkr8:5XQbQFRIn89xQRi4@cluster0.e8tfylk.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"))
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

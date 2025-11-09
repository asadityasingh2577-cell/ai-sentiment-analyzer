from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()

MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017")
DB_NAME = os.getenv("DB_NAME", "sentiment_db")
COLLECTION_NAME = os.getenv("COLLECTION_NAME", "reviews")

client = MongoClient(MONGO_URI)
db = client[DB_NAME]
collection = db[COLLECTION_NAME]

def insert_review(text, sentiment, score):
    collection.insert_one({
        "text": text,
        "sentiment": sentiment,
        "score": score
    })

def get_all_reviews():
    return list(collection.find({}, {"_id": 0}))

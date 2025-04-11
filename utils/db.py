from pymongo import MongoClient
from config.config import MONGODB_URI, DB_NAME
from datetime import datetime

try:
    client = MongoClient(MONGODB_URI)
    db = client[DB_NAME]
except Exception as e:
    raise Exception(f"Failed to connect to MongoDB: {str(e)}")

def store_result(username, topic, marks, mistakes):
    try:
        db.results.insert_one({
            "username": username,
            "topic": topic,
            "marks": marks,
            "mistakes": mistakes,
            "date": datetime.now().strftime("%Y-%m-%d")
        })
    except Exception as e:
        raise Exception(f"Error storing result: {str(e)}")

def get_user_results(username):
    try:
        return list(db.results.find({"username": username}))
    except Exception as e:
        raise Exception(f"Error fetching results: {str(e)}")
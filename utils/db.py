# from pymongo import MongoClient
# from config.config import MONGODB_URI, DB_NAME
# from datetime import datetime

# try:
#     client = MongoClient(MONGODB_URI)
#     db = client[DB_NAME]
# except Exception as e:
#     raise Exception(f"Failed to connect to MongoDB: {str(e)}")

# def store_result(username, topic, marks, mistakes):
#     try:
#         db.results.insert_one({
#             "username": username,
#             "topic": topic,
#             "marks": marks,
#             "mistakes": mistakes,
#             "date": datetime.now().strftime("%Y-%m-%d")
#         })
#     except Exception as e:
#         raise Exception(f"Error storing result: {str(e)}")

# def get_user_results(username):
#     try:
#         return list(db.results.find({"username": username}))
#     except Exception as e:
#         raise Exception(f"Error fetching results: {str(e)}")









import streamlit as st
import os
from pymongo import MongoClient
from datetime import datetime

MONGODB_URI = st.secrets["mongo"]["uri"]
DB_NAME = st.secrets["mongo"]["db"]

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
        print("✅ Stored result.")
    except Exception as e:
        raise Exception(f"Error storing result: {str(e)}")

def get_user_results(username):
    try:
        results = list(db.results.find({"username": username}))
        print(f"✅ Fetched {len(results)} results.")
        return results
    except Exception as e:
        raise Exception(f"Error fetching results: {str(e)}")

# Run test
store_result("testuser", "math", 7, ["Q1", "Q3"])
print(get_user_results("testuser"))

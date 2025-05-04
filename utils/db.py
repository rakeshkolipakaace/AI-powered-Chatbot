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




from pymongo import MongoClient
from config.config import MONGODB_URI, DB_NAME
from datetime import datetime
import bcrypt

try:
    client = MongoClient(MONGODB_URI)
    db = client[DB_NAME]
    db.users.create_index("username", unique=True)
except Exception as e:
    raise Exception(f"Failed to connect to MongoDB: {str(e)}")

def create_user(username, password):
    try:
        if db.users.find_one({"username": username}):
            raise ValueError("Username already exists.")
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        db.users.insert_one({
            "username": username,
            "password": hashed_password,
            "created_at": datetime.now().strftime("%Y-%m-%d")
        })
    except Exception as e:
        raise Exception(f"Error creating user: {str(e)}")

def verify_user(username, password):
    try:
        user = db.users.find_one({"username": username})
        if not user:
            return False
        return bcrypt.checkpw(password.encode('utf-8'), user["password"])
    except Exception as e:
        raise Exception(f"Error verifying user: {str(e)}")

def store_result(username, topic, marks, mistakes):
    try:
        if not db.users.find_one({"username": username}):
            raise Exception("User does not exist.")
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
        if not db.users.find_one({"username": username}):
            raise Exception("User does not exist.")
        return list(db.results.find({"username": username}))
    except Exception as e:
        raise Exception(f"Error fetching results: {str(e)}")
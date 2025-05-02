import bcrypt
from pymongo import MongoClient
from config.config import MONGODB_URI, DB_NAME

try:
    client = MongoClient(MONGODB_URI)
    db = client[DB_NAME]  
except Exception as e:
    raise Exception(f"Failed to connect to MongoDB: {str(e)}")

def register_user(username, password):
    if db.users.find_one({"username": username}):
        raise ValueError("Username already exists.")
    hashed_pw = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    db.users.insert_one({"username": username, "password": hashed_pw})

def login_user(username, password):
    user = db.users.find_one({"username": username})
    if user and bcrypt.checkpw(password.encode('utf-8'), user["password"]):
        return True
    return False

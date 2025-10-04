from pymongo import MongoClient

def get_db():
    # Replace "localhost" and "27017" with your MongoDB configuration if needed
    client = MongoClient("mongodb://localhost:27017")
    return client['battery_management']

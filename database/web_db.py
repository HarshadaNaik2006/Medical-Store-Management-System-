from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")

# Separate database for the Flask application
db = client["medical_store_localhost"]

# Collections
medicines_collection = db["medicines"]
customers_collection = db["customers"]
suppliers_collection = db["suppliers"]
bills_collection = db["bills"]
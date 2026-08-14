from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")

db = client["medical_store"]

customer_collection = db["customers"]

supplier_collection = db["suppliers"]

medicine_collection = db["medicines"]

bill_collection = db["bills"]

print("MongoDB Connected Successfully!")


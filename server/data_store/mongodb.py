# app/data_store/mongodb.py
from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["database_name"]

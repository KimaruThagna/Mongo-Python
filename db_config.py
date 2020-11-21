from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')
db = client['mongo-python']
print("Database created........")
collection = db['car_locations']
print("Colletion created........")
from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')
db = client['mongo-python']
# list collections
#db.list_collection_names()
print("Database created........")
collection = db['car_locations']
# drop collections
#collection.drop()

# issue commands
#result = db.command("serverStatus") or dbstats
print("Colletion created........")
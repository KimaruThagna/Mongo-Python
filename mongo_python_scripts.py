from db_config import client, collection
from pymongo import DESCENDING,ASCENDING
cars = [ {'name': 'Audi', 'price': 52642},
    {'name': 'Mercedes', 'price': 57127},
    {'name': 'Skoda', 'price': 9000},
    {'name': 'Volvo', 'price': 29000},
    {'name': 'Bentley', 'price': 350000},
    {'name': 'Citroen', 'price': 21000},
    {'name': 'Hummer', 'price': 41400},
    {'name': 'Volkswagen', 'price': 21600} ]


def multiple_data_insert():
    collection.insert_many(cars)
    return 'Success. multiple inserts committed'

def multiple_data_retrieve():
    return collection.find()

def count_retrieved_data():
    return collection.find().count()

def expensive_cars(value):
    return collection.find({'price':{'$gt':value}})

def cheap_cars(value):
    return collection.find({'price':{'$lt':value}})
#pymongo projections
def select_subfields():
    return collection.find({},{'_id':1,'name':1})

def sort_documents(bool):
    if bool:
        return collection.sort('price',DESCENDING)
    else:
        return collection.sort('price',ASCENDING)

def collection_limit_output():
    return collection.find().skip(2).limit(3) # skip the first 2 documents, limit results to 3 documents

def sum_aggregator():
    agr = [{'$group': {'_id': 1, 'all': {'$sum': '$price'}}}]

    return list(collection.aggregate(agr))

def filtered_sum_aggregator():
    agr = [{'$match': {'$or': [{'name': "Audi"}, {'name': "Volvo"}]}},
           {'$group': {'_id': 1, 'sum2cars': {'$sum': "$price"}}}]

    return list(collection.aggregate(agr))
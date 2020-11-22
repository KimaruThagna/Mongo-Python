from db_config import client, collection
from pymongo import DESCENDING,ASCENDING, ReturnDocument
cars = [ {'name': 'Audi', 'price': 52642},
    {'name': 'Mercedes', 'price': 57127},
    {'name': 'Skoda', 'price': 9000},
    {'name': 'Volvo', 'price': 29000},
    {'name': 'Bentley', 'price': 350000},
    {'name': 'Citroen', 'price': 21000},
    {'name': 'Hummer', 'price': 41400},
    {'name': 'Volkswagen', 'price': 21600} ]

# inserting a single document
#collection.insert()
def delete_all():
    collection.drop()

def delete_one(car):
    collection.delete_one({'name':car})

def delete_some(filter):# supply filter as a dictionary
    collection.delete_many(filter)


def multiple_data_insert():
    collection.insert_many(cars)
    return 'Success. multiple inserts committed'
# db.collection.find_one() retrieves the first document in the  collection
def multiple_data_retrieve():
    return collection.find().pretty()

def single_retrieve(id):
    return collection.find({"_id":id})

def find_and_update(id):
    return collection.find_one_and_update({'_id':id},
                                   {'$inc':{'price':0.554}},
                                    upsert=True, # if it doesnt exist, create it. Should be having all relevant fields in the update though
                                    projection={'name':True,'price':False},# determine which fields you want to see
                                   return_document=ReturnDocument.AFTER) # return the updated version of a document

def single_update(id):
    collection.update({'_id':id},{'$inc':{"price":25.55},
                                  '$set':{"name":'Fancy new car'}
                                  })
# each appends multiple values in the array field
def update_with_array(id):
    collection.update({'_id':id},
                      {'$push':
                           { 'extras':{'$each':['sun roof', 'driver partition','keyless start'],'$sort':ASCENDING}
                           }
                       })

def pop_from_array(id):
    collection.update({'_id':id}, {'$pop':{'extras':-1 # remove the first element from array
                                           }
                                   })
def update_or_insert(id):
    pass

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
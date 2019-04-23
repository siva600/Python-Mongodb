import pymongo
import datetime
import pprint


def conn():
    connection = None
    try:
        connection = pymongo.MongoClient('mongodb://localhost:27017')
    except pymongo.errors.ConnectionFailure as e:
        print("Could not Connect to mongodb")
    return connection


print(conn().database_names())
db = conn()['mydatabase']
collection = db['customers']
print(collection)
doc = {"name":"Alberto","surname":"Negron","twitter":"@Altons"}

collection.insert(doc)



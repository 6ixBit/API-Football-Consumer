import pymongo
from pymongo import mongo_client
import dns


#Setup database instance
my_client = pymongo.MongoClient("mongodb+srv://admin:nYZzNHx1X2wbi9vc@zeus-uu6gn.mongodb.net/test?retryWrites=true&w=majority")


#DB setup
db = my_client['Zeus']

#Collection
collection = db["PL_19-20"]


post = {
    "name": "jack",
    "age" : 40,
    "place": "Russia"
}

collection.insert_one(post)
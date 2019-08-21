import pymongo


#Setup database instance
my_client = pymongo.MongoClient("mongodb://localhost:27017/")

#DB creation
mydb = my_client["player_db"]

#Collections
mycol = mydb["PL_19-20"]

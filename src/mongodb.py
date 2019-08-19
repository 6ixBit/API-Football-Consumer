import pymongo
import requests

#API Access
rapid_key = "9fde00920fmsh2b95942b59e9d3ep10ab71jsn1b9295c2d6d8"

url_1 = "https://api-football-v1.p.rapidapi.com/v2/teams/league/524" #Get team_ids

#Connect to API
connect = requests.get(url_1, headers={
    'x-rapidapi-host': "api-football-v1.p.rapidapi.com",
    'x-rapidapi-key': rapid_key})

#Setup database instance
my_client = pymongo.MongoClient("mongodb://localhost:27017/")

#DB creation
mydb = my_client["player_db"]

#Collections
mycol = mydb["PL_19-20"]



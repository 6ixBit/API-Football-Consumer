import pymongo
import requests
from pprint import pprint

#API Access
rapid_key = "9fde00920fmsh2b95942b59e9d3ep10ab71jsn1b9295c2d6d8"

url_1 = "https://api-football-v1.p.rapidapi.com/v2/teams/league/524" #Get team_ids
url_2 = "https://api-football-v1.p.rapidapi.com/v2/players/team/"
url_2_param = ""


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

#List to hold team IDs
team_ids = []

teams_json = connect.json() #JSON INSTANCE

#Traverse JSON
for key, value in teams_json.items():
    level_1 = value['teams']


count = 0
for a in level_1:
    get_ids = level_1[count]['team_id']
    team_ids.append(get_ids)
    count += 1

#Traverse and Grab player stats for each team_id
for b in team_ids:
    url_2_param = b                                        #Set param for URL
    url_2_final = url_2 + str(url_2_param) + "/" + "2019-2020"

    # Connect to API
    connect_2 = requests.get(url_2_final, headers={
        'x-rapidapi-host': "api-football-v1.p.rapidapi.com",
        'x-rapidapi-key': rapid_key})

    stats_json = connect_2.json()

    for c in stats_json.items():
        pprint(c)


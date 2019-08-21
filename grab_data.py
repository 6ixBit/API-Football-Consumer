import requests
from pprint import pprint
import classes
import pymongo

#API Access
rapid_key = ""

url_1 = "https://api-football-v1.p.rapidapi.com/v2/teams/league/524" #Get team_ids
url_2 = "https://api-football-v1.p.rapidapi.com/v2/players/team/"
url_2_param = ""


#Connect to API
connect = requests.get(url_1, headers={
    'x-rapidapi-host': "api-football-v1.p.rapidapi.com",
    'x-rapidapi-key': rapid_key})


#List to hold team IDs
team_ids = []

teams_json = connect.json() #JSON INSTANCE

#Instances for each class
player_i = classes.Player_info()
player_s = classes.Player_shots()
player_g = classes.Player_goals()
player_p = classes.Player_passing()
player_t = classes.Player_tackles()
player_d = classes.Player_duels()
player_drib = classes.PLayer_dribbles()
player_f = classes.Player_fouls()
player_c = classes.Player_cards()
player_pen = classes.Player_penalties()
player_games = classes.Player_games()
player_subs = classes.Player_subs()

#Dictionary to host player data
player_dict = {
    player_i.player_name: [player_i.team_name, player_i.first_name, player_i.last_name, player_i.mins_played, #General player info
                           player_i.rating, player_i.league, player_i.position, player_i.age, player_i.birth_date,
                           player_i.season, player_i.nationality, player_i.height, player_i.weight,
                           player_s.total_shots, player_s.shots_on_target,                                           #Shots
                           player_g.goals, player_g.assists, player_g.goals_conceded,                                #Goals
                           player_p.total_passes, player_p.pass_accuracy, player_p.key_passes,                       #Passing
                           player_t.total_tackles, player_t.interceptions, player_t.blocks,                          #Blocks
                           player_d.total_duels, player_d.duels_won,                                                 #Duels
                           player_drib.dribble_attempts, player_drib.dribbles_successful,                            #Dribbles
                           player_f.fouls_drawn, player_f.fouls_committed,                                           #Fouls
                           player_c.yellow_cards, player_c.red_cards,                                                #Cards
                           player_pen.penalties_won, player_pen.penalties_committed, player_pen.penalties_success,   #Pens
                           player_pen.penalties_missed, player_pen.penalties_saved,
                           player_games.appearences, player_games.minutes_played, player_games.starts,               #Games
                           player_subs.bench, player_subs.subbed_in, player_subs.subbed_out                          #Subs
                           ]
}


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
    counter = 0

    url_2_param = b                                        #Set param for URL
    url_2_final = url_2 + str(url_2_param) + "/" + "2019-2020"

    # Connect to API
    connect_2 = requests.get(url_2_final, headers={
        'x-rapidapi-host': "api-football-v1.p.rapidapi.com",
        'x-rapidapi-key': rapid_key})

    stats_json = connect_2.json()
    for key, value in stats_json.items(): #Loop through JSON items
        level_2 = value['players']
        for x in level_2:
            if x['league'] == "Premier League": #Filter out over competitions
                #Player info
                player_i.player_name = level_2[counter]['player_name']
                player_i.team_name = level_2[counter]['team_name']
                player_i.first_name = level_2[counter]['firstname']
                player_i.last_name = level_2[counter]['lastname']
                player_i.mins_played = level_2[counter]['games']['minutes_played']
                player_i.team_name = level_2[counter]['team_name']
                player_i.league = level_2[counter]['league']
                player_i.position = level_2[counter]['position']
                player_i.age = level_2[counter]['age']
                player_i.birth_date = level_2[counter]['birth_date']
                player_i.season = level_2[counter]['season']
                player_i.nationality = level_2[counter]['nationality']
                player_i.height = level_2[counter]['height']
                player_i.weight = level_2[counter]['weight']

                #Player shots
                player_s.total_shots = level_2[counter]['shots']['total']
                player_s.shots_on_target = level_2[counter]['shots']['on']

                #Goals
                player_g.goals = level_2[counter]['goals']['total']
                player_g.assists = level_2[counter]['goals']['assists']
                player_g.goals_conceded = level_2[counter]['goals']['conceded']

                #Passes
                player_p.total_passes = level_2[counter]['passes']['total']
                player_p.key_passes = level_2[counter]['passes']['key']
                player_p.pass_accuracy = level_2[counter]['passes']['accuracy']

                #Tackles
                player_t.total_tackles = level_2[counter]['tackles']['total']
                player_t.blocks = level_2[counter]['tackles']['blocks']
                player_t.interceptions = level_2[counter]['tackles']['interceptions']

                #Duels
                player_d.total_duels = level_2[counter]['duels']['total']
                player_d.duels_won = level_2[counter]['duels']['won']

                #Dribbles
                player_drib.dribble_attempts = level_2[counter]['dribbles']['attempts']
                player_drib.dribbles_successful = level_2[counter]['dribbles']['success']

                #Fouls
                player_f.fouls_committed = level_2[counter]['fouls']['committed']
                player_f.fouls_drawn = level_2[counter]['fouls']['drawn']

                #Cards
                player_c.yellow_cards = level_2[counter]['cards']['yellow']
                player_c.red_cards = level_2[counter]['cards']['red']

                #Penalties
                player_pen.penalties_won = level_2[counter]['penalty']['won']
                player_pen.penalties_committed = level_2[counter]['penalty']['commited']
                player_pen.penalties_success = level_2[counter]['penalty']['success']
                player_pen.penalties_missed = level_2[counter]['penalty']['missed']
                player_pen.penalties_saved = level_2[counter]['penalty']['saved']

                #Games
                player_games.starts = level_2[counter]['games']['lineups']
                player_games.appearences = level_2[counter]['games']['appearences']

                #Subs
                player_subs.bench = level_2[counter]['substitutes']['bench']
                player_subs.subbed_in = level_2[counter]['substitutes']['in']
                player_subs.subbed_out = level_2[counter]['substitutes']['out']

                #Fill dictionary with all player stats
                player_dict.update({
                           player_i.player_name: [player_i.team_name, player_i.first_name, player_i.last_name, player_i.mins_played, #General player info
                           player_i.rating, player_i.league, player_i.position, player_i.age, player_i.birth_date,
                           player_i.season, player_i.nationality, player_i.height, player_i.weight,
                           player_s.total_shots, player_s.shots_on_target,                                           #Shots
                           player_g.goals, player_g.assists, player_g.goals_conceded,                                #Goals
                           player_p.total_passes, player_p.pass_accuracy, player_p.key_passes,                       #Passing
                           player_t.total_tackles, player_t.interceptions, player_t.blocks,                          #Blocks
                           player_d.total_duels, player_d.duels_won,                                                 #Duels
                           player_drib.dribble_attempts, player_drib.dribbles_successful,                            #Dribbles
                           player_f.fouls_drawn, player_f.fouls_committed,                                           #Fouls
                           player_c.yellow_cards, player_c.red_cards,                                                #Cards
                           player_pen.penalties_won, player_pen.penalties_committed, player_pen.penalties_success,   #Pens
                           player_pen.penalties_missed, player_pen.penalties_saved,
                           player_games.appearences, player_games.minutes_played, player_games.starts,               #Games
                           player_subs.bench, player_subs.subbed_in, player_subs.subbed_out                          #Subs
                           ]})

                counter += 1




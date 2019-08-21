class Player_info:
    def __init__(self, first_name="", last_name="", player_name='', rating=0.0,
                 mins_played=0, team_name="", league="", position="", age=0, birth_date="", season="", nationality="",
                 height="", weight="",
                 ):
        self.first_name = first_name
        self.last_name = last_name
        self.player_name = player_name
        self.rating = rating
        self.mins_played = mins_played
        self.team_name = team_name
        self.league = league
        self.position = position
        self.age = age
        self.birth_date = birth_date
        self.season = season
        self.nationality = nationality
        self.height = height
        self.weight = weight


class Player_shots:
    def __init__(self, total_shots=0, shots_on_target=0):
        self.total_shots = total_shots
        self.shots_on_target = shots_on_target


class Player_goals:
    def __init__(self, goals=0, goals_conceded=0, assists=0):
        self.goals = goals
        self.goals_conceded = goals_conceded
        self.assists = assists


class Player_passing:
    def __init__(self, total_passes=0, key_passes=0, pass_accuracy=0):
        self.total_passes = total_passes
        self.key_passes = key_passes
        self.pass_accuracy = pass_accuracy


class Player_tackles:
    def __init__(self, total_tackles=0, blocks=0, interceptions=0):
        self.total_tackles = total_tackles
        self.blocks = blocks
        self.interceptions = interceptions


class Player_duels:
    def __init__(self, total_duels=0, duels_won=0):
        self.total_duels = total_duels
        self.duels_won = duels_won


class PLayer_dribbles:
    def __init__(self, dribble_attempts=0, dribbles_successful=0):
        self.dribble_attempts = dribble_attempts
        self.dribbles_successful = dribbles_successful


class Player_fouls:
    def __init__(self, fouls_drawn=0, fouls_committed=0):
        self.fouls_drawn = fouls_drawn
        self.fouls_committed = fouls_committed


class Player_cards:
    def __init__(self, yellow_cards=0, red_cards=0):
        self.yellow_cards = yellow_cards
        self.red_cards = red_cards


class Player_penalties:
    def __init__(self, penalties_won=0, penalties_committed=0, penalties_success=0,  penalties_missed=0, penalties_saved=0):
        self.penalties_won = penalties_won
        self.penalties_committed = penalties_committed
        self.penalties_success = penalties_success
        self.penalties_missed = penalties_missed
        self.penalties_saved = penalties_saved


class Player_games:
    def __init__(self, appearences=0, minutes_played=0, starts=0):
        self.appearences = appearences
        self.minutes_played = minutes_played
        self.starts = starts


class Player_subs:
    def __init__(self, subbed_in=0, subbed_out=0, bench=0):
        self.subbed_in = subbed_in
        self.subbed_out = subbed_out
        self.bench = bench

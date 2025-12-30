import json

state2 = dict()
state2['players'] = dict()
state = {
    "current_turn": 1,
    "players": {
        1: {
            "username": "player1",
            "position": 1,
            "money": 1500,
            "properties": [],
            "in_jail": False,
            "jail_turns": 0,
            "get_out_of_jail_cards": 0
        },
        2: {
            "username": "player2",
            "position": 1,
            "money": 1500,
            "properties": [],
            "in_jail": False,
            "jail_turns": 0,
            "get_out_of_jail_cards": 0
        },
        3: {
            "username": "player3",
            "position": 1,
            "money": 1500,
            "properties": [],
            "in_jail": False,
            "jail_turns": 0,
            "get_out_of_jail_cards": 0
        },
        4: {
            "username": "player4",
            "position": 1,
            "money": 1500,
            "properties": [],
            "in_jail": False,
            "jail_turns": 0,
            "get_out_of_jail_cards": 0
        }
    }
}
with open('player_data.json', 'w') as f:
    json.dump(state, f, indent=4)
with open('player_data.json', 'r') as f:
    state = json.load(f)
player_dict = dict()
players = state["players"]

for i in players:
    state2['players'][int(i)] = players[i]
current_turn = state["current_turn"]
state2["current_turn"] = current_turn
state = state2
print(state)
players = state["players"]
with open('current-game.json', 'r') as w:
    dict_username = json.load(w)
import json

state = {
    "current_turn": 1,
    "players": {
        1: {
            "username": "player1",
            "position": 1,
            "money": 1000,
            "properties": [],
            "in_jail": [],
            "jail_turns": 0,
            "get_out_of_jail_cards": 0

        },

        2: {
            "username": "player1",
            "position": 1,
            "money": 1000,
            "properties": [],
            "in_jail": [],
            "jail_turns": 0,
            "get_out_of_jail_cards": 0},

        3: {
            "username": "player3",
            "position": 1,
            "money": 1000,
            "properties": [],
            "in_jail": [],
            "jail_turns": 0,
            "get_out_of_jail_cards": 0
        },
        4: {
            "username": "player4",
            "position": 1,
            "money": 1000,
            "properties": [],
            "in_jail": [],
            "jail_turns": 0,
            "get_out_of_jail_cards": 0
        }
    }
    , "lst":
        {"already_tried_getting_out": [],
         "dices_after_prison": [],
         "should_skip": [],
         "lst_picked_same": [],
         "lst_just_got_out_of_jail": []
         }
}


def loading_game():
    name_of_save = input('enter the game you want to load:')



    state2 = dict()
    state2['players'] = dict()
    state = {
        "current_turn": 1,
        "players": {
            1: {
                "username": "player1",
                "position": 1,
                "money": 1000,
                "properties": [],
                "in_jail": [],
                "jail_turns": 0,
                "get_out_of_jail_cards": 0

            },

            2: {
                "username": "player1",
                "position": 1,
                "money": 1000,
                "properties": [],
                "in_jail": [],
                "jail_turns": 0,
                "get_out_of_jail_cards": 0 },



                3: {
                "username": "player3",
                "position": 1,
                "money": 1000,
                "properties": [],
                "in_jail": [],
                "jail_turns": 0,
                "get_out_of_jail_cards": 0
            },
            4: {
                "username": "player4",
                "position": 1,
                "money": 1000,
                "properties": [],
                "in_jail": [],
                "jail_turns": 0,
                "get_out_of_jail_cards": 0
            }
        }
        , "lst":
            {"already_tried_getting_out": [],
            "dices_after_prison": [],
            "should_skip": [],
            "lst_picked_same": [],
            "lst_just_got_out_of_jail": []
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
    state2["lst"] = state["lst"]
    state = state2
    players = state["players"]

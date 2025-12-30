import random
import json
from map import move_player
with open("current-game.json", "r") as f:
    username_dict = json.load(f)


def informations(id, username, position=0, in_jail=False, jail_turns=0, money=1500, properties=None):
    if properties is None:
        properties = []
    return {
        "id": id,
        "username": username,
        "position": position,
        "in_jail": in_jail,
        "jail_turns": jail_turns,
        "money": money,
        "properties": properties
    }


def leaderboard(players):
    print("\n                        ====== Leaderboard ======   ")
    print(
        f"{'id |':<3} {'username |':<10} {'position |':<4} {'jail_situation |':<8} {'jail_turns |':<10} {'money  |':<8} {'Properties'}")
    print("-" * 70)
    for informarion in players:
        jail_situation = "in jail" if informarion["in_jail"] else "free"
        all_properties = ", ".join(informarion["properties"]) if informarion["properties"] else "-"
        print(
            f"{informarion['id']:<4} {informarion['username']:<10} {informarion['position']:<10} {jail_situation:<16} {informarion['jail_turns']:<12} {informarion['money']:<8} {all_properties}")


p1 = informations(id=1, username=username_dict["1"], position=10, in_jail=False, jail_turns=2, money=2000,
                  properties=["Park Place", "Boardwalk"])
p2 = informations(2, username_dict["2"], position=5, in_jail=True, jail_turns=2, money=1200, properties=["Baltic Ave"])
p3 = informations(3, username_dict["3"], position=15, in_jail=False, jail_turns=0, money=1800)
p4 = informations(4, username_dict["4"], position=15, in_jail=False, jail_turns=0, money=1800)
players = [p1, p2, p3, p4]

leaderboard(players)


def save_game():
    with open("current-game.json", "r") as f:
        username_dict = json.load(f)
    dict_save = []
    for i in range(4):
        save = informations(i + 1, username_dict[str(i + 1)], position=0, in_jail=False, jail_turns=0, money=1500,
                            properties=None)
        dict_save.append(save)
    with open("leaderboard.json", "w") as f:
        json.dump(dict_save, f, indent=4)


chance_card = ["get out of jail free", "go directory to jail", "pay 15$ to the bank", "move to GO and get 200$"
               , "get 150$ from the bank", "pay 20$ to the bank",
               "give the next player 80$", "Give the next person $50", "pay 100$ to the bank", "skip next player", 'move to board walk']
community_chest = ["receive 200$ form bank", "get 50$ from next previous", "give the next player 100$",
                   "sell one of your houses", "move to free parking", "receive 50$ form bank",
                   "give the next player 150$"]
chance_card = ["give the next person $50"]
cards = {"p1": [], "p2": [], "p3": [], "p4": []}
card_keys = list(cards.keys())
card_values = list(cards.values())


def random_chance_card(player, players):
    random_card = random.choice(chance_card)
    print('you entered in chance square! this is the card which you got!')
    print(random_card)
    if random_card == "get out of jail free" and "get out of jail free" not in card_values[player - 1]:
        card_values[player - 1].append(random_card)
        player_key = f"p{player}"
        cards[player_key].append(random_card)
        players[player]['get_out_of_jail_cards'] += 1
    elif random_card == "pay 15$ to the bank":
        players[player]['money'] -= 15
    elif random_card == "go directory to jail":
        players[player]['in_jail'] = True
    elif random_card == "move to GO and get 200$":
        players[player]['position'] = 1
        return 'GO'
    elif random_card == "skip next player":
        return 'skip'
    elif random_card == "get 150$ from the bank":
        players[player]['money'] += 150
    elif random_card == "pay 20$ to the bank":
        players[player]['money'] -= 20
    elif random_card == "give the next player 80$":
        return 'nextp80'

    elif random_card == "give the next person $50":
        return 'nextp50'
    elif random_card == "pay 100$ to the bank":
        players[player]['money'] -= 100
    elif random_card == 'move to board walk':
        return 'boardwalk'


def random_community_chest(player, players):
    random_card = random.choice(community_chest)
    print('you entered in chance square! this is the card which you got!')
    print(random_card)
    if random_card == "receive 200$ form bank":
        players[player]['money'] += 200
    #elif random_card == "sell one of your houses":



def jail():
    if player_num == 31:
        print(f'player{player_num} went to jail')
        player_num = 11


def free_jail(i):
    if "get out of jail free" in card_values[i - 1]:
        player_num = 11


def in_jail():
    print("choose an option:")
    print(f"1-payment of 50$")
    print(f"2-use card")
    print(f"3-try for a double")
    jail_choices = int(input("selected option:"))
    return jail_choices


save_game()

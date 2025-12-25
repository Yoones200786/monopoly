import random
import json
from board_setup import board, color_groups, railroad_positions, utility_positions, monopoly_data
from gholami import sell_house, sell_hotel, handle_bankruptcy
with open ("current-game.json","r") as f:
    username_dict = json.load(f)


def informations(id,username,position=0,in_jail=False,jail_turns=0,money=1500,properties=None):
    if properties is None:
        properties = []
    return{
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
    print(f"{'id |':<3} {'username |':<10} {'position |':<4} {'jail_situation |':<8} {'jail_turns |':<10} {'money  |':<8} {'Properties'}")
    print("-"*70)
    for informarion in players:
        jail_situation = "in jail" if informarion["in_jail"] else "free"
        all_properties = ", ".join(informarion["properties"]) if informarion["properties"] else "-"
        print(f"{informarion['id']:<4} {informarion['username']:<10} {informarion['position']:<10} {jail_situation:<16} {informarion['jail_turns']:<12} {informarion['money']:<8} {all_properties}")


p1=informations(id=1, username=username_dict["1"], position=10, in_jail=False, jail_turns=2, money=2000, properties=["Park Place", "Boardwalk"])
p2 = informations(2, username_dict["2"], position=5, in_jail=True, jail_turns=2, money=1200, properties=["Baltic Ave"])
p3 = informations(3, username_dict["3"], position=15, in_jail=False, jail_turns=0, money=1800)
p4 = informations(4, username_dict["4"], position=15, in_jail=False, jail_turns=0, money=1800)
players=[p1,p2,p3,p4]

leaderboard(players)

def save_game():
    with open ("current-game.json","r") as f:
        username_dict = json.load(f)
    dict_save = []
    for i in range(4):
        save=informations(i+1,username_dict[str(i+1)],position=0,in_jail=False,jail_turns=0,money=1500,properties=None)
        dict_save.append(save)
    with open("leaderboard.json", "w") as f:
            
        json.dump(dict_save,f, indent = 4)

chance_card=["get out of jail free","go directory to jail","pay 15$ to the bank","move to GO and get 150$","you win a home in pacific avenue street","get 150$ from the bank","pay 20$ to the bank","give the next player 80$","Give the next person $50","pay 15$ to the bank"]
community_chest=["receive 200$ form bank","get 50$ from next previous","give the next player 100$","sell one of your houses","move to free parking","receive 50$ form bank","give the next player 150$"]
cards={"p1":[],"p2":[],"p3":[],"p4":[]}
card_keys=list(cards.keys())
card_values=list(cards.values())

def random_chance_card(i):
    random_card=random.choice(chance_card)
    if random_card=="get out of jail free" and "get out of jail free" not in card_values[i-1]:
        card_values[i-1].append(random_card)
        player_key=f"p{i}"
        cards[player_key].append(random_card)
    if random_card=="go directory to jail":
        print(f'player{player_num} went to jail')
        player_num=11

 
    else:
        return random_card
def random_community_chest(i):
    return random.choice(community_chest)

def jail():
    if player_num==31:
        print(f'player{player_num} went to jail')
        player_num=11

def free_jail(i):
    if "get out of jail free" in card_values[i-1]:
        player_num=11
        

# Send player to jail
def send_to_jail(player):
    player["position"] = 11
    player["in_jail"] = True
    player["jail_turns"] = 0
    print(f'{player["username"]} went to jail')

# Manage jail options
def handle_jail(player, player_cards, chance_card):
    print(f'\n{player["username"]} is in jail')

    while True:
        print("\nChoose an option:")
        print("1 - Pay 50$")
        print("2 - Use get out of jail free card")
        print("3 - Try for a double")

        try:
            choice = int(input("Selected option: "))
            if choice not in (1, 2, 3):
                print("Invalid choice. Try again.")
                continue
        except ValueError:
            print("Please enter a number.")
            continue

        # Pay 50$ to leave    
        if choice == 1:
            if player["money"] < 50:
                print("Not enough money")
                continue

            player["money"] -= 50
            player["in_jail"] = False
            player["jail_turns"] = 0
            print("You paid 50$ and got out of jail")
            break

        # Use get out of jail card    
        elif choice == 2:
            if "get out of jail free" not in player_cards:
                print("You don't have a get out of jail free card")
                continue


            player_cards.remove("get out of jail free")


            chance_card.append("get out of jail free")

            player["in_jail"] = False
            player["jail_turns"] = 0
            print("You used a card and got out of jail")
            break

        # Try for a double    
        elif choice == 3:
            d1 = random.randint(1, 6)
            d2 = random.randint(1, 6)
            print(f"Dice rolled: {d1}, {d2}")

            if d1 == d2:
                player["in_jail"] = False
                player["jail_turns"] = 0
                player["position"] = (player["position"] + d1 + d2) % 40
                print("Double! You are free and move forward")
                break
            else:
                player["jail_turns"] += 1
                print("Not a double")
                # After 3 turns, pay or sell
                if player["jail_turns"] >= 3:
                    if player["money"] < 50:
                        print("Not enough money after 3 turns")


                        while player["money"] < 50:
                            print("You need to sell houses/hotels to get enough money.")
                            print("1 - Sell a house")
                            print("2 - Sell a hotel")
                            print("3 - Declare bankruptcy")
                            choice = input("Select option: ")
                            # Sell house
                            if choice == "1":
                                sell_house(player_id, position, players)
                            # Sell hotel
                            elif choice == "2":
                                sell_hotel(player_id, position, players)
                            elif choice == "3":
                                handle_bankruptcy(players, player_id, creditor_id=None)
                                break
                            else:
                                print("Invalid choice.")
                            # Check again if the player has enough money
                            if player["money"] >= 50:
                                break  # If the player has enough money, exit the loop

                    player["money"] -= 50
                    player["in_jail"] = False
                    player["jail_turns"] = 0
                    print("3 turns passed, paid 50$ and got out")
                    break


save_game()
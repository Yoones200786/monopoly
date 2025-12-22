import random
informations={
    1: {
      "id": 1,
      "username": "player1",
      "position": 0,
      "money": 1500,
      "properties": [],
      "in_jail": False,
      "jail_turns": 0,
      "get_out_of_jail_cards": 0
    },
    2: {
      "id": 2,
      "username": "player2",
      "position": 0,
      "money": 1500,
      "properties": [],
      "in_jail": False,
      "jail_turns": 0,
      "get_out_of_jail_cards": 0
    },
    3: {
      "id": 3,
      "username": "player3",
      "position": 0,
      "money": 1500,
      "properties": [],
      "in_jail": False,
      "jail_turns": 0,
      "get_out_of_jail_cards": 0
    },4: {
      "id": 4,
      "username": "player4",
      "position": 0,
      "money": 1500,
      "properties": [],
      "in_jail": False,
      "jail_turns": 0,
      "get_out_of_jail_cards": 0
    }
}

def information():
    return informations


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
        

def in_jail(i):
    print("choose an option:")
    print(f"'1'-payment of 50$")
    print(f"'2'-use card")
    print(f"'3'-try for a double")
    jail_choices=int(input("selected option:"))
    return jail_choices
jail_choice=in_jail()
if jail_choice==1:
    pass
elif jail_choice==2:
    if "get out of jail free" in card_values():
        pass
    else:
        print("card not found")
elif jail_choice==3:
    pass


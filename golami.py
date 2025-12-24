from board_setup import board, color_groups, railroad_positions, utility_positions

state = {
    "current_turn": 1,
    "players": {
        1: {
            "username": "player1",
            "position": 0,
            "money": 1500,
            "properties": [],
            "in_jail": False,
            "jail_turns": 0,
            "get_out_of_jail_cards": 0
        },
        2: {
            "username": "player2",
            "position": 0,
            "money": 1500,
            "properties": [],
            "in_jail": False,
            "jail_turns": 0,
            "get_out_of_jail_cards": 0
        },
        3: {
            "username": "player3",
            "position": 0,
            "money": 1500,
            "properties": [],
            "in_jail": False,
            "jail_turns": 0,
            "get_out_of_jail_cards": 0
        },
        4: {
            "username": "player4",
            "position": 0,
            "money": 1500,
            "properties": [],
            "in_jail": False,
            "jail_turns": 0,
            "get_out_of_jail_cards": 0
        }
    }
}




def has_monopoly(player_id, color):
    for pos in color_groups[color]:
        if board[pos]["owner"] != player_id:
            return False,"player has not all this color"
    return True,"player has this color"


def count_railroads(player_id):
    return sum(1 for pos in railroad_positions if board[pos]["owner"] == player_id),"player has x railroad"


def count_utilities(player_id):
    return sum(1 for pos in utility_positions if board[pos]["owner"] == player_id)    #"player has y utility."


def calculate_rent(position, current_player_id, dice_sum=0):
    space = board[position]
    if space["type"] not in ["property", "railroad", "utility", "tax"]:
        return 0          #"this house is not rent"
    if space["type"] == :

    if space.get("owner") is None or space["owner"] == current_player_id or space.get("mortgaged", False):
        return 0           #"property is gero and is not rent"
    if space["type"] == "property":
        houses = space.get("houses", 0)
        rent_list = space["rent"]
        base_rent = rent_list[0]
        if houses == 0 and has_monopoly(space["owner"], space["color"]):
            return base_rent * 2         #"for enhesar rent will be doble"
        return rent_list[houses]           #"Rent calculated with z houses"  return rent_list[houses if houses <= 5 else 5]  I do'nt undrestand if statement here?
    elif space["type"] == "railroad":
        num = count_railroads(space["owner"])
        if num == 0:
            return 0            #"owner has not railroad"
        rent_list = space["rent"]
        return rent_list[num - 1]            #"Rent calculated with b railroads"
    elif space["type"] == "utility":
        num = count_utilities(space["owner"])
        if num == 0:
            return 0           #"owner has not utilites"
        multiplier = space["rent_multiplier"][num - 1]
        return dice_sum * multiplier      #"Rent of utilites calculated with  dice_sum"
    return 0          #elseif owner has not any utilites


def buy_property(player_id, position, players):
    space = board[position]
    if space["type"] in ["property", "railroad", "utility"] and space.get("owner") is None:
        price = space["buy_price"]
        if players[player_id]["money"] >= price:
            players[player_id]["money"] -= price
            space["owner"] = player_id
            players[player_id]["properties"].append(space["name"])
            return True, price,"property has buyed with {price}$"
    return False        #"this property is not buy_able"


def mortgage_property(player_id, position, players):
    space = board[position]
    if space["type"] in ["property", "railroad", "utility"] and \
       space["owner"] == player_id and not space.get("mortgaged", False) and \
       space.get("houses", 0) == 0:
        mortgage_value = space["buy_price"] // 2
        players[player_id]["money"] += mortgage_value
        space["mortgaged"] = True
        return True, mortgage_value,"money recive and property mortgage"
    return False, 0,"sharait gero gozari bargharar nist"


def unmortgage_property(player_id, position, players):
    space = board[position]
    if space["type"] in ["property", "railroad", "utility"] and \
       space["owner"] == player_id and space.get("mortgaged", False):
        cost = int((space["buy_price"] // 2) * 1.1)
        if players[player_id]["money"] >= cost:
            players[player_id]["money"] -= cost
            space["mortgaged"] = False
            return True, cost,"property azad shod ba cost$"
    return False, 0,"has not money for azad sazi gero"



def build_house(player_id, position, players):
    space = board[position]
    if space["type"] != "property":
        return False, "thie khaneh is not melk"
    if space["owner"] != player_id:
        return False, "this property is not for player"
    if space.get("mortgaged", False):
        return False, "melk is gero"
    if space.get("houses", 0) >= 4:
        return False, "max mogaz khaneh is 4"
    cost = space["house_cost"]
    if players[player_id]["money"] < cost:
        return False, "not enough money"
    players[player_id]["money"] -= cost
    space["houses"] = space.get("houses", 0) + 1
    return True, f"one house made: {cost}"


def can_build_hotel(player_id, position, players):
    space = board[position]
    if space["type"] != "property":
        return False,"this khaneh is not property"
    if space["owner"] != player_id:
        return False,"this property is not for player"
    if space.get("mortgaged", False):
        return False
    if space.get("houses", 0) < 4:
        return False
    return True



def is_land_buyable(player_id, position, players):
    space = board[position]
    if space["type"] in ["property", "railroad", "utility"] and space.get("owner") is None:
        if state[player_id]["players"][player_id]['money'] >= space["buy_price"]:
            return True


def can_build_house(player_id, position, players):
    idx_color_space = []
    count_houses_in_every_color = []
    space = board[position]
    color_of_space = space['color']
    if has_monopoly(player_id, space["color"]):
        if state[player_id]["players"][player_id]['money'] > space["house_cost"]:
            for i in color_groups[color_of_space]:
                idx_color_space.append(i)
            for i in idx_color_space:
                num_house = board[i].get('houses', 0)
                count_houses_in_every_color.append(num_house)
            if space.get("houses", 0) == min(count_houses_in_every_color) and space.get('houses') < 4 and space.get('hotel', 0) == 0:
                return True
    return False

def build_hotel(player_id, position, players):
    space = board[position]
    if space.get('houses', 0) == 4:
        if players[player_id]['money'] >= space['hotel_cost']:
            players[player_id]['money'] -= space['hotel_cost']
            space['houses'] = 0
            space['hotel'] = 1



print(board)



from board_setup import board, color_groups, railroad_positions, utility_positions
def has_monopoly(player_id, color):
    for pos in color_groups[color]:
        if board[pos]["owner"] != player_id:
            return False,"player has not all this color"
    return True,"player has this color"  
def count_railroads(player_id):
    return sum(1 for pos in railroad_positions if board[pos]["owner"] == player_id),"player has x railroad"
def count_utilities(player_id):
    return sum(1 for pos in utility_positions if board[pos]["owner"] == player_id),"player has y utility."
def calculate_rent(position, current_player_id, dice_sum=0):
    space = board[position]
    if space["type"] not in ["property", "railroad", "utility"]:
        return 0,"this house is not rent"
    if space.get("owner") is None or space["owner"] == current_player_id or space.get("mortgaged", False):
        return 0,"property is gero and is not rent"
    if space["type"] == "property":
        houses = space.get("houses", 0) 
        rent_list = space["rent"]
        base_rent = rent_list[0]
        if houses == 0 and has_monopoly(space["owner"], space["color"]):
            return base_rent * 2,"for enhesar rent will be doble"
        return rent_list[houses if houses <= 5 else 5],"Rent calculated with z houses"
    elif space["type"] == "railroad":
        num = count_railroads(space["owner"])
        if num == 0:
            return 0,"owner has not railroad"
        rent_list = space["rent"]
        return rent_list[num - 1],"Rent calculated with b railroads"
    elif space["type"] == "utility":
        num = count_utilities(space["owner"])
        if num == 0:
            return 0,"owner has not utilites"
        multiplier = space["rent_multiplier"][num - 1]
        return dice_sum * multiplier,"Rent of utilites calculated with  dice_sum"
    return 0,"elseif owner has not any utilites"
def buy_property(player_id, position, players):
    space = board[position]
    if space["type"] in ["property", "railroad", "utility"] and space.get("owner") is None:
        price = space["buy_price"]
        if players[player_id]["money"] >= price:
            players[player_id]["money"] -= price
            space["owner"] = player_id
            return True, price,"property has buyed with {price}$"
    return False, 0,"this property is not buy_able"
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
def is_property_buyable(position):
    space = board[position]
    if space["type"] not in ["property", "railroad", "utility"]:
        return False,"this khaneh is not buyable"
    if space.get("owner") is None:
        return True,"this khaneh is buyable"
    return False,"This house has already been purchased."
def is_property_buyable(position):
    space = board[position]
    if space["type"] not in ["property", "railroad", "utility"]:
        return False, "this khaneh is not buyanle"
    if space.get("owner") is None:
        return True, "this khaneh is buyable"
    return False, "this khaneh befor buyed"
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
def can_build_hotel(player_id, position):
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




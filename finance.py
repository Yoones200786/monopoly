from board_setup import board, color_groups, railroad_positions, utility_positions
def has_monopoly(player_id, color):
    for pos in color_groups[color]:
        if board[pos]["owner"] != player_id:
            return False
    return True  
def count_railroads(player_id):
    return sum(1 for pos in railroad_positions if board[pos]["owner"] == player_id)
def count_utilities(player_id):
    return sum(1 for pos in utility_positions if board[pos]["owner"] == player_id)
def calculate_rent(position, current_player_id, dice_sum=0):
    space = board[position]
    if space["type"] not in ["property", "railroad", "utility"]:
        return 0
    if space.get("owner") is None or space["owner"] == current_player_id or space.get("mortgaged", False):
        return 0
    if space["type"] == "property":
        houses = space.get("houses", 0) 
        rent_list = space["rent"]
        base_rent = rent_list[0]
        if houses == 0 and has_monopoly(space["owner"], space["color"]):
            return base_rent * 2
        return rent_list[houses if houses <= 5 else 5]
    elif space["type"] == "railroad":
        num = count_railroads(space["owner"])
        if num == 0:
            return 0
        rent_list = space["rent"]
        return rent_list[num - 1]
    elif space["type"] == "utility":
        num = count_utilities(space["owner"])
        if num == 0:
            return 0
        multiplier = space["rent_multiplier"][num - 1]
        return dice_sum * multiplier
    return 0
def buy_property(player_id, position, players):
    space = board[position]
    if space["type"] in ["property", "railroad", "utility"] and space.get("owner") is None:
        price = space["buy_price"]
        if players[player_id]["money"] >= price:
            players[player_id]["money"] -= price
            space["owner"] = player_id
            return True, price
    return False, 0
def mortgage_property(player_id, position, players):
    space = board[position]
    if space["type"] in ["property", "railroad", "utility"] and \
       space["owner"] == player_id and not space.get("mortgaged", False) and \
       space.get("houses", 0) == 0:
        mortgage_value = space["buy_price"] // 2
        players[player_id]["money"] += mortgage_value
        space["mortgaged"] = True
        return True, mortgage_value
    return False, 0
def unmortgage_property(player_id, position, players):
    space = board[position]
    if space["type"] in ["property", "railroad", "utility"] and \
       space["owner"] == player_id and space.get("mortgaged", False):
        cost = int((space["buy_price"] // 2) * 1.1)  
        if players[player_id]["money"] >= cost:
            players[player_id]["money"] -= cost
            space["mortgaged"] = False
            return True, cost
    return False, 0
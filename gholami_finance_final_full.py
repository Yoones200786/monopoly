from board_setup import board, color_groups, railroad_positions, utility_positions
def has_monopoly(player_id, color):
    for pos in color_groups[color]:
        if board[pos]["owner"] != player_id:
            return False, "player does not own all properties of this color"
    return True, "player owns all properties of this color"
def count_railroads(player_id):
    return sum(1 for pos in railroad_positions if board[pos]["owner"] == player_id), "railroads counted"
def count_utilities(player_id):
    return sum(1 for pos in utility_positions if board[pos]["owner"] == player_id), "utilities counted"
def calculate_rent(position, current_player_id, dice_sum=0):
    space = board[position]
    if space["type"] not in ["property", "railroad", "utility", "tax"]:
        return 0, "no rent on this space"
    if space["type"] == "tax":
        return space["amount"], "tax charged"
    if (space.get("owner") is None or space["owner"] == current_player_id or space.get("mortgaged", False)):
        return 0, "no rent charged"
    owner = space["owner"]
    if space["type"] == "property":
        houses = space.get("houses", 0)
        rent_list = space["rent"]
        if houses == 0 and has_monopoly(owner, space["color"])[0]:
            return rent_list[0] * 2, "monopoly rent applied"
        return rent_list[min(houses, 5)], f"rent with {houses} houses"
    if space["type"] == "railroad":
        num = count_railroads(owner)[0]
        if num == 0:
            return 0, "no railroads owned"
        return space["rent"][num - 1], f"rent with {num} railroads"
    if space["type"] == "utility":
        num = count_utilities(owner)[0]
        if num == 0:
            return 0, "no utilities owned"
        multiplier = space["rent_multiplier"][num - 1]
        return dice_sum * multiplier, "utility rent calculated"
    return 0, "rent calculation error"
def buy_property(player_id, position, players):
    space = board[position]
    if space["type"] in ["property", "railroad", "utility"] and space.get("owner") is None:
        price = space["buy_price"]
        if players[player_id]["money"] >= price:
            players[player_id]["money"] -= price
            space["owner"] = player_id
            return True, price, "property purchased"
    return False, 0, "property not purchasable"
def mortgage_property(player_id, position, players):
    space = board[position]

    if (
        space["type"] in ["property", "railroad", "utility"]
        and space["owner"] == player_id
        and not space.get("mortgaged", False)
        and space.get("houses", 0) == 0
    ):
        mortgage_value = space["buy_price"] // 2
        players[player_id]["money"] += mortgage_value
        space["mortgaged"] = True
        return True, mortgage_value, "property mortgaged"
    return False, 0, "mortgage conditions not met"
def unmortgage_property(player_id, position, players):
    space = board[position]
    if (
        space["type"] in ["property", "railroad", "utility"]
        and space["owner"] == player_id
        and space.get("mortgaged", False)
    ):
        cost = int((space["buy_price"] // 2) * 1.1)
        if players[player_id]["money"] >= cost:
            players[player_id]["money"] -= cost
            space["mortgaged"] = False
            return True, cost, "property unmortgaged"
    return False, 0, "not enough money to unmortgage"

def is_property_buyable(position):
    space = board[position]
    if space["type"] in ["property", "railroad", "utility"] and space.get("owner") is None:
        return True, "property is buyable"
    return False, "property already owned"

def build_house(player_id, position, players):
    space = board[position]
    if space["type"] != "property":
        return False, "not a property"
    if space["owner"] != player_id or space.get("mortgaged", False):
        return False, "property not owned or mortgaged"
    if not has_monopoly(player_id, space["color"])[0]:
        return False, "no monopoly"
    if not check_even_houses(space["color"])[0]:
        return False, "houses not evenly distributed"
    if space.get("houses", 0) >= 4:
        return False, "maximum houses reached"
    cost = space["house_cost"]
    if players[player_id]["money"] < cost:
        return False, "not enough money"
    players[player_id]["money"] -= cost
    space["houses"] = space.get("houses", 0) + 1
    return True, f"house built for {cost}$"

def check_even_houses(color):
    positions = color_groups[color]
    levels = [board[pos].get("houses", 0) for pos in positions]
    if max(levels) - min(levels) > 1:
        return False, "houses not even"
    return True, "houses evenly distributed"
def can_build_hotel(player_id, position):
    space = board[position]
    if space["type"] != "property":
        return False, "not a property"
    if space["owner"] != player_id or space.get("mortgaged", False):
        return False, "invalid ownership or mortgaged"
    if not has_monopoly(player_id, space["color"])[0]:
        return False, "no monopoly"
    for pos in color_groups[space["color"]]:
        if board[pos].get("houses", 0) != 4:
            return False, "all properties must have 4 houses"
    return True, "hotel can be built"

def build_hotel(player_id, position, players):
    can_build, _ = can_build_hotel(player_id, position)
    if not can_build:
        return False, "cannot build hotel"
    space = board[position]
    cost = space["hotel_cost"]
    if players[player_id]["money"] < cost:
        return False, "not enough money"
    players[player_id]["money"] -= cost
    space["houses"] = 5
    return True, f"hotel built for {cost}$"

def sell_house(player_id, position, players):
    space = board[position]
    if space["type"] != "property" or space["owner"] != player_id:
        return False, "not owner or not property"
    if space.get("houses", 0) <= 0:
        return False, "no houses to sell"
    if not check_even_houses(space["color"])[0]:
        return False, "houses not evenly distributed"
    refund = space["house_cost"] // 2
    players[player_id]["money"] += refund
    space["houses"] -= 1
    return True, f"house sold for {refund}$"

def sell_hotel(player_id, position, players):
    space = board[position]
    if space["type"] != "property" or space["owner"] != player_id or space.get("houses") != 5:
        return False, "no hotel to sell"
    refund = space["hotel_cost"] // 2
    players[player_id]["money"] += refund
    space["houses"] = 4
    return True, f"hotel sold for {refund}$"

def handle_bankruptcy(players, player_id, creditor_id=None):
    player = players[player_id]
    if player["money"] >= 0:
        return False, "player is not bankrupt"
    player["bankrupt"] = True
    for pos in range(len(board)):
        space = board[pos]
        if space.get("owner") == player_id:
            space["owner"] = creditor_id
            space["mortgaged"] = False
            space["houses"] = 0
    if creditor_id is not None:
        players[creditor_id]["money"] += max(0, -player["money"])
    player["money"] = 0
    return True, f"player {player_id} declared bankrupt"

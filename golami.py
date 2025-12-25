from board_setup import board, color_groups, railroad_positions, utility_positions
from load_save import state
from load_save import players


def has_monopoly(player_id, color):
    for pos in color_groups[color]:
        if board[pos]["owner"] != player_id:
            return False  # "player has not all this color"
    return True  # "player has this color"


def count_railroads(player_id):
    return sum(1 for pos in railroad_positions if board[pos - 1]["owner"] == player_id)


def count_utilities(player_id):
    return sum(1 for pos in utility_positions if board[pos - 1]["owner"] == player_id)  #"player has y utility."


def show_info_of_current_space(position):
    space = board[position - 1]
    msg = f'you are currently in {space['type']} square with name of {space["name"]}'
    if space['type'] == 'property':
        msg += f' in color {space['color']}'
    print(msg)


def calculate_rent(position, current_player_id, dice_sum=0):
    space = board[position - 1]
    if space["type"] not in ["property", "railroad", "utility", "tax"]:
        return 0  # "this house is not rent"
    if space["type"] == 'tax':
        print('you landed on a tax square!')
        return space["amount"]

    if space.get("owner") == "" or space["owner"] == current_player_id or space.get("mortgaged", False):
        return 0
    if space["type"] == "property":
        houses = space.get("houses", 0)
        rent_list = space["rent"]
        base_rent = rent_list[0]
        if houses == 0 and has_monopoly(space["owner"], space["color"]):
            return base_rent * 2    # for monopoly rent will be double
        return rent_list[houses]    # Rent calculated with z houses
    elif space["type"] == "railroad":
        num = count_railroads(space["owner"])
        if num == 0:
            return 0  # owner has not railroad
        rent_list = space["rent"]
        return rent_list[num - 1]  # Rent calculated with b railroads
    elif space["type"] == "utility":
        num = count_utilities(space["owner"])
        if num == 0:
            return 0  # owner has not utilites
        multiplier = space["rent_multiplier"][num - 1]
        return dice_sum * multiplier  # "Rent of utilites calculated with  dice_sum"
    return 0  # elseif owner has not any utilites


def buy_property(player_id, position, players):
    space = board[position - 1]
    suitable_info = []
    if space["type"] in ["property", "railroad", "utility"] and space.get("owner") == "":
        price = space["buy_price"]
        if players[player_id]["money"] >= price:
            players[player_id]["money"] -= price
            space["owner"] = player_id
        if space['type'] == "property":
            houses = space.get("houses", 0)
            color = space["color"]
            hotel = space.get("hotel", 0)
            suitable_info = [color, houses, hotel]
        else:
            suitable_info = [space['type']]
        players[player_id]["properties"].append({f'square {position}': suitable_info})
        print('bought successfully!')
        return True
    return False  #"this property is not buy_able"


def giving_money_to_player(player_id, position, players, rent):
    space = board[position - 1]
    if space["type"] in ["property", "railroad", "utility"]:
        owner = space['owner']
        print(owner)
        players[owner]['money'] += rent
        print(f'player {owner} got {rent}$ from your rent!')


def mortgage_property(player_id, position, players):
    space = board[position]
    if space["type"] in ["property", "railroad", "utility"] and \
            space["owner"] == player_id and not space.get("mortgaged", False) and \
            space.get("houses", 0) == 0:
        mortgage_value = space["buy_price"] // 2
        players[player_id]["money"] += mortgage_value
        space["mortgaged"] = True
        return True, mortgage_value, "money recive and property mortgage"
    return False, 0, "sharait gero gozari bargharar nist"


def unmortgage_property(player_id, position, players):
    space = board[position]
    if space["type"] in ["property", "railroad", "utility"] and \
            space["owner"] == player_id and space.get("mortgaged", False):
        cost = int((space["buy_price"] // 2) * 1.1)
        if players[player_id]["money"] >= cost:
            players[player_id]["money"] -= cost
            space["mortgaged"] = False
            return True, cost, "property azad shod ba cost$"
    return False, 0, "has not money for azad sazi gero"


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
    space = board[position - 1]
    if space["type"] != "property":
        return False  # "this khaneh is not property"
    if space["owner"] != player_id:
        return False  # "this property is not for player"
    if space.get("mortgaged", False):
        return False
    if space.get("houses", 0) < 4:
        return False
    return True


def is_land_buyable(player_id, position, players):
    space = board[position - 1]
    if space["type"] == "property" and space.get("owner") == "":
        if players[player_id]['money'] >= space["buy_price"]:
            return True
    return False


def can_build_house(player_id, position, players):
    space = board[position - 1]
    if space["type"] == "property":
        idx_color_space = []
        count_houses_in_every_color = []
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


def can_buy_railroad(player_id, position, players):
    space = board[position - 1]
    if space["type"] == "railroad":
        if space["owner"] == "":
            if players[player_id]['money'] >= space["buy_price"]:
                return True
    return False


def can_buy_utilities(player_id, position, players):
    space = board[position - 1]
    if space["type"] == "utility":
        if space["owner"] == "":
            return True
    return False


def build_hotel(player_id, position, players):
    space = board[position - 1]
    if space.get('houses', 0) == 4:
        if players[player_id]['money'] >= space['hotel_cost']:
            players[player_id]['money'] -= space['hotel_cost']
            space['houses'] = 0
            space['hotel'] = 1


def handle_bankruptcy():
    print('not complete')


def check_even_houses(color):
    positions = color_groups[color]
    levels = [board[pos].get("houses", 0) for pos in positions]
    if max(levels) - min(levels) > 1:
        return False  # houses not even
    return True  # houses evenly distributed


def sell_hotel(player_id, position, players):
    space = board[position - 1]
    refund = space["hotel_cost"] // 2
    players[player_id]["money"] += refund
    space["houses"] = 4
    space["hotel"] = 0
    print(f"hotel sold for {refund}$")


def sell_house(player_id, position, players):
    space = board[position - 1]
    if space["type"] != "property" or space["owner"] != player_id:
        return False  # not owner or not property
    if space.get("houses", 0) <= 0:
        return False  # no houses to sell
    if not check_even_houses(space["color"]):
        return False,  # houses not evenly distributed
    refund = space["house_cost"] // 2
    players[player_id]["money"] += refund
    space["houses"] -= 1
    print(f"house sold for {refund}$")


def find_available_houses(player_id):
    available_houses = []
    pos_houses = []
    for checker in range(40):
        space = board[checker - 1]
        if space["type"] == "property":
            if space["owner"] == player_id:
                if space.get("houses", 0) > 0:
                    available_houses.append(f'square {(checker+1)} with {space.get('houses', 0)} houses')
                    pos_houses.append(checker+1)
    return available_houses, pos_houses
def find_available_hotel(player_id):
    available_hotels = []
    pos_hotels = []
    for checker in range(40):
        space = board[checker - 1]
        if space["type"] == "property":
            if space["owner"] == player_id:
                if space.get("hotel", 0) == 1:
                    available_hotels.append(f'square {(checker + 1)} with {space.get('hotel')} hotel')
                    pos_hotels.append(checker + 1)
    return available_hotels, pos_hotels


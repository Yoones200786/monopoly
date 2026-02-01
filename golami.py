from board_setup import board, color_groups, railroad_positions, utility_positions
#print(board) برای دیباگ است و حالا غیر فعال شده است.

def has_monopoly(player_id, color):
    for pos in color_groups[color]:
        if board[pos - 1]["owner"] != player_id:
            return False  # "player has not all this color"
    return True  # "player has this color"


def count_railroads(player_id):
    return sum(1 for pos in railroad_positions if board[pos - 1]["owner"] == player_id)


def add_house_to_properties(player_id, position, players):
    for i in players[player_id]["properties"]:
        for j in i:
            if j == f"square {position}":
                i[j][1] += 1
def add_mortgage_to_properties(player_id, position, players):
    space = board[position - 1]
    for i in players[player_id]["properties"]:
        for j in i:
            if j == f"square {position}":
                if space['type'] == 'property':
                    i[j][3] = True
                elif space['type'] in ["railroad", "utility"]:
                    i[j][1] = True

def add_unmortgage_to_properties(player_id, position, players):
    space = board[position - 1]
    for i in players[player_id]["properties"]:
        for j in i:
            if j == f"square {position}":
                if space['type'] == 'property':
                    i[j][3] = False
                elif space['type'] in ["railroad", "utility"]:
                    i[j][1] = False
def sell_house_from_properties(player_id,position,players):
    for i in players[player_id]["properties"]:
        for j in i:
            if j == f"square {position}":
                i[j][1] -= 1


def count_utilities(player_id):
    return sum(1 for pos in utility_positions if board[pos - 1]["owner"] == player_id)  #"player has y utility."


def show_info_of_current_space(position):
    space = board[position - 1]
    msg = f'you are currently in {space['type']} square with name of {space["name"]}'
    if space['type'] == 'property':
        msg += f' in color {space['color']}'
    print(msg)


def check_even_houses(color, position, code, player_id, players):
    idx_color_space = []
    space = board[position - 1]
    color_of_space = space['color']
    count_houses_in_every_color = []
    for i in color_groups[color_of_space]:
        idx_color_space.append(i)
    for i in idx_color_space:
        num_house = board[i - 1].get('houses', 0)
        if code == 'buy':
            if board[i - 1].get('hotel', 0) == 1:
                num_house = 4
        count_houses_in_every_color.append(num_house)
    if code == 'buy':
        if space.get("houses", 0) == min(count_houses_in_every_color):
            return True

    if code == 'sell':
        for i in color_groups[color_of_space]:
            if board[i -1].get('hotel', 0) == 1:
                return False
        if space.get("houses", 0) == max(count_houses_in_every_color):
            return True


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
        hotel = space.get('hotel', 0)
        houses = space.get("houses", 0)
        rent_list = space["rent"]
        base_rent = rent_list[0]
        if hotel == 1:
            return rent_list[5]
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
            mortgaged = space.get("mortgaged", False)
            suitable_info = [color, houses, hotel, mortgaged]
        else:
            suitable_info = [space['type'], False]
        players[player_id]["properties"].append({f'square {position}': suitable_info})
        print('bought property successfully!')
        return True
    return False  #"this property is not buy_able"


def giving_money_to_player(player_id, position, players, rent, future_player):
    space = board[position - 1]
    if space["type"] in ["property", "railroad", "utility"]:
        owner = space['owner']
        players[owner]['money'] += rent
        print(f'player {owner} got {rent}$ from your rent!')
    elif space['type'] in ["community_chest", 'chance']:
        players[future_player]['money'] += rent

def mortgage_property(player_id, position, players):
    space = board[position -1]
    if space["type"] in ["property", "railroad", "utility"] and \
            space["owner"] == player_id and not space.get("mortgaged", False) and \
            space.get("houses", 0) == 0\
            and space.get('hotel', 0) == 0:
        mortgage_value = space["buy_price"] // 2
        players[player_id]["money"] += mortgage_value
        print('mortgaged successfully!')
        space["mortgaged"] = True
        add_mortgage_to_properties(player_id, position, players)
        return True, mortgage_value  # "money recive and property mortgage"

    return False, 0  # "sharait gero gozari bargharar nist"


def unmortgage_property(player_id, position, players):
    space = board[position-1]
    if space["type"] in ["property", "railroad", "utility"] and \
            space["owner"] == player_id and space.get("mortgaged", False):
        cost = int((space["buy_price"] // 2) * 1.1)
        if players[player_id]["money"] >= cost:
            print(f'unmortgaged successfully! for cost of {cost}')
            players[player_id]["money"] -= cost
            space["mortgaged"] = False
            add_unmortgage_to_properties(player_id, position, players)

def build_house(player_id, position, players):
    space = board[position - 1]
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
    print('bought house successfully!')
    add_house_to_properties(player_id, position, players)
    return True, f"one house made: {cost}"


def add_hotel_to_properties(player_id, position, players):
    for i in players[player_id]["properties"]:
        for j in i:
            if j == f"square {position}":
                i[j][2] += 1
                i[j][1] = 0


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
    if not check_even_houses(space["color"], position, 'buy',player_id,players):
        return False
    if space.get("hotel", 0) == 1:
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
            if players[player_id]['money'] >= space["house_cost"]:
                for i in color_groups[color_of_space]:
                    idx_color_space.append(i)
                for i in idx_color_space:
                    if board[i - 1].get('mortgaged', False):
                        return False
                    num_house = board[i - 1].get('houses', 0)
                    if board[i - 1].get('hotel', 0) == 1:
                        num_house = 4
                    count_houses_in_every_color.append(num_house)
                if space.get("houses", 0) == min(count_houses_in_every_color) and space.get('houses',0) < 4 and space.get('hotel', 0) == 0:
                    return True
    return False


def can_buy_railroad(player_id, position, players):
    space = board[position - 1]
    if space["type"] == "railroad":
        if players[player_id]['money'] >= space["buy_price"]:
            if space["owner"] == "":
                if players[player_id]['money'] >= space["buy_price"]:
                    return True
    return False


def can_buy_utilities(player_id, position, players):
    space = board[position - 1]
    if space["type"] == "utility":
        if players[player_id]['money'] >= space["buy_price"]:
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
            add_hotel_to_properties(player_id, position, players)
            print('bought hotel successfully!')


def sell_hotel(player_id, position, players):
    space = board[position - 1]
    refund = space["hotel_cost"] // 2
    players[player_id]["money"] += refund
    space["houses"] = 4
    space["hotel"] = 0
    print(f"hotel sold for {refund}$")
    sell_hotel_from_property(player_id, position, players)


def sell_hotel_from_property(player_id, position, players):
    for i in players[player_id]["properties"]:
        for j in i:
            if j == f"square {position}":
                i[j][2] -= 1


def sell_house(player_id, position, players):
    space = board[position - 1]
    if space["type"] != "property" or space["owner"] != player_id:
        return False  # not owner or not property
    if space.get("houses", 0) <= 0:
        return False  # no houses to sell
    if not check_even_houses(space["color"], position, 'sell',player_id, players):
        return False,  # houses not evenly distributed
    refund = space["house_cost"] // 2
    players[player_id]["money"] += refund
    space["houses"] -= 1
    sell_house_from_properties(player_id, position, players)
    print(f"house sold for {refund}$")


def find_available_houses(player_id, players,from_board=True):
    if from_board:
        available_houses = []
        pos_houses = []
        for checker in range(40):
            space = board[checker]
            if space["type"] == "property":
                if space["owner"] == player_id:
                    if space.get("houses", 0) > 0:
                        available_houses.append(f'square {(checker+1)} with {space.get('houses', 0)} houses\n') # we can use this for more information
                        pos_houses.append(checker+1)
        return available_houses, pos_houses



def find_available_hotel(player_id, players):  # if you have hotel you can sell it without worrying its for finding hotels to sell
    available_hotels = []
    pos_hotels = []
    for checker in range(40):
        space = board[checker]
        if space["type"] == "property":
            if space["owner"] == player_id:
                if space.get("hotel", 0) == 1:
                    available_hotels.append(f'square {(checker + 1)} with {space.get('hotel'),0} hotel')
                    pos_hotels.append(str(checker + 1))
    #positions = pos_hotels
    return pos_hotels


def houses_available_for_sale(player_id, players):
    houses_for_sale = []
    positions = find_available_houses(player_id, players)[1]
    for position in positions:
        space = board[position - 1]
        if space.get("hotel", 0) == 0:
            if check_even_houses(space["color"], position, 'sell', player_id, players):
                houses_for_sale.append(str(position))
    return houses_for_sale


def changing_owner(players, removed_player_id, player_in_charge, position):
    for i in range(40):
        space = board[i]
        if space["owner"] == removed_player_id:
            space["owner"] = player_in_charge
            if space['type'] == 'property':
                players[player_in_charge]['properties'].append({f'square {i+1}': [space['color'], 0, 0, True]})
            if space['type'] == 'utility' or space['type'] == 'railroad':
                players[player_in_charge]['properties'].append({f'square {i+1}': [space['type'], True]})

def can_mortgage(player_number, players):
    lst = []
    for i in range(40):
        space = board[i]
        if space["owner"] == player_number:
            if space["type"] in ["property", "railroad", "utility"]:
                if space.get('mortgaged', False) == True:
                    continue
                if space["type"] == "property":
                    for j in color_groups[space['color']]:
                        c_space = board[j - 1]
                        if c_space.get('houses', 0) != 0:
                            break
                        if c_space.get('hotel', 0) != 0:
                            break
                    else:
                        lst.append(str(i+1))
                else:
                    lst.append(str(i+1))
    return lst


def find_mortgage_need(player_id, players):  # if needs to be unmortgaged
    lst = []
    for i in range(40):
        space = board[i]
        if space.get('mortgaged', False) == True:
            cost = int((space["buy_price"] // 2) * 1.1)
            if cost <= players[player_id]["money"]:
                if space['owner'] == player_id:
                    lst.append(str(i+1))
    return lst


def find_all_can_build_houses(player_id, players):  # it's for finding houses that you can buy
    lst = []
    for i in range(40):
        if can_build_house(player_id, i + 1, players):
            lst.append(str(i+1))
    return lst


def find_all_can_build_hotel(player_id, players):  # it's for finding hotels that you can buy
    lst = []
    for i in range(40):
        if can_build_hotel(player_id, i + 1, players):
            lst.append(str(i+1))
    return lst

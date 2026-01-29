import os
monopoly_data = {
    "1": {
        "name": "GO",
        "type": "special",
        "action": "collect",
        "amount": 200
        ,"owner":"gov"
    },
    "2": {
        "name": "Mediterranean Avenue",
        "type": "property",
        "color": "brown",
        "buy_price": 60,
        "rent": [2, 10, 30, 90, 160, 250],
        "house_cost": 50,
        "hotel_cost": 50
        ,"owner":""
    },
    "3": {
        "name": "Community Chest 1",
        "type": "community_chest"
        , "owner": "gov"

    },
    "4": {
        "name": "Baltic Avenue",
        "type": "property",
        "color": "brown",
        "buy_price": 60,
        "rent": [4, 20, 60, 180, 320, 450],
        "house_cost": 50,
        "hotel_cost": 50,
        "owner":""

    },
    "5": {
        "name": "Income Tax",
        "type": "tax",
        "amount": 200
        , "owner": "gov"

    },
    "6": {
        "name": "Reading Railroad",
        "type": "railroad",
        "buy_price": 200,
        "rent": [25, 50, 100, 200]
        , "owner": ""

    },
    "7": {
        "name": "Oriental Avenue",
        "type": "property",
        "color": "light_blue",
        "buy_price": 100,
        "rent": [6, 30, 90, 270, 400, 550],
        "house_cost": 50,
        "hotel_cost": 50
        , "owner": ""
},
    "8": {
        "name": "Chance 1",
        "type": "chance"
        , "owner": "gov"

    },
    "9": {
        "name": "Vermont Avenue",
        "type": "property",
        "color": "light_blue",
        "buy_price": 100,
        "rent": [6, 30, 90, 270, 400, 550],
        "house_cost": 50,
        "hotel_cost": 50
        , "owner": ""
    },

    "10": {
        "name": "Connecticut Avenue",
        "type": "property",
        "color": "light_blue",
        "buy_price": 120,
        "rent": [8, 40, 100, 300, 450, 600],
        "house_cost": 50,
        "hotel_cost": 50
        , "owner": ""},
    "11": {
        "name": "Jail",
        "type": "special",
        "action": "just_visiting"
        , "owner": "gov"

    },
    "12": {
        "name": "St. Charles Place",
        "type": "property",
        "color": "pink",
        "buy_price": 140,
        "rent": [10, 50, 150, 450, 625, 750],
        "house_cost": 100,
        "hotel_cost": 100
        , "owner": ""

    },
    "13": {
        "name": "Electric Company",
        "type": "utility",
        "buy_price": 150,
        "rent_multiplier": [4, 10]
        , "owner": ""

    },
    "14": {
        "name": "States Avenue",
        "type": "property",
        "color": "pink",
        "buy_price": 140,
        "rent": [10, 50, 150, 450, 625, 750],
        "house_cost": 100,
        "hotel_cost": 100
        , "owner": ""

    },
    "15": {
        "name": "Virginia Avenue",
        "type": "property",
        "color": "pink",
        "buy_price": 160,
        "rent": [12, 60, 180, 500, 700, 900],
        "house_cost": 100,
        "hotel_cost": 100
        , "owner": ""

    },
    "16": {
        "name": "Pennsylvania Railroad",
        "type": "railroad",
        "buy_price": 200,
        "rent": [25, 50, 100, 200]
        , "owner": ""

    },
    "17": {
        "name": "St. James Place",
        "type": "property",
        "color": "orange",
        "buy_price": 180,
        "rent": [14, 70, 200, 550, 750, 950],
        "house_cost": 100,
        "hotel_cost": 100
        , "owner": ""

    },
    "18": {
        "name": "Community Chest 2",
        "type": "community_chest"
        , "owner": "gov"

    },
    "19": {
        "name": "Tennessee Avenue",
        "type": "property",
        "color": "orange",
        "buy_price": 180,
        "rent": [14, 70, 200, 550, 750, 950],
        "house_cost": 100,
        "hotel_cost": 100
        , "owner": ""

    },
    "20": {
        "name": "New York Avenue",
        "type": "property",
        "color": "orange",
        "buy_price": 200,
        "rent": [16, 80, 220, 600, 800, 1000],
        "house_cost": 100,
        "hotel_cost": 100
        , "owner": ""

    },
    "21": {
        "name": "Free Parking",
        "type": "special"
        , "owner": "gov"

    },
    "22": {
        "name": "Kentucky Avenue",
        "type": "property",
        "color": "red",
        "buy_price": 220,
        "rent": [18, 90, 250, 700, 875, 1050],
        "house_cost": 150,
        "hotel_cost": 150
        , "owner": ""

    },
    "23": {
        "name": "Chance 2",
        "type": "chance"
        , "owner": "gov"

    },
    "24": {
        "name": "Indiana Avenue",
        "type": "property",
        "color": "red",
        "buy_price": 220,"rent": [18, 90, 250, 700, 875, 1050],
        "house_cost": 150,
        "hotel_cost": 150
        , "owner": ""

    },
    "25": {
        "name": "Illinois Avenue",
        "type": "property",
        "color": "red",
        "buy_price": 240,
        "rent": [20, 100, 300, 750, 925, 1100],
        "house_cost": 150,
        "hotel_cost": 150
        , "owner": ""

    },
    "26": {
        "name": "B&O Railroad",
        "type": "railroad",
        "buy_price": 200,
        "rent": [25, 50, 100, 200]
        , "owner": ""

    },
    "27": {
        "name": "Atlantic Avenue",
        "type": "property",
        "color": "yellow",
        "buy_price": 260,
        "rent": [22, 110, 330, 800, 975, 1150],
        "house_cost": 150,
        "hotel_cost": 150
        , "owner":  ""

    },
    "28": {
        "name": "Ventnor Avenue",
        "type": "property",
        "color": "yellow",
        "buy_price": 260,
        "rent": [22, 110, 330, 800, 975, 1150],
        "house_cost": 150,
        "hotel_cost": 150
        , "owner": ""

    },
    "29": {
        "name": "Water Works",
        "type": "utility",
        "buy_price": 150,
        "rent_multiplier": [4, 10]
        , "owner": ""

    },
    "30": {
        "name": "Marvin Gardens",
        "type": "property",
        "color": "yellow",
        "buy_price": 280,
        "rent": [24, 120, 360, 850, 1025, 1200],
        "house_cost": 150,
        "hotel_cost": 150
        , "owner": ""

    },
    "31": {
        "name": "Go to Jail",
        "type": "special",
        "action": "goto_jail"
        , "owner": "gov"

    },
    "32": {
        "name": "Pacific Avenue",
        "type": "property",
        "color": "green",
        "buy_price": 300,
        "rent": [26, 130, 390, 900, 1100, 1275],
        "house_cost": 200,
        "hotel_cost": 200
        , "owner": ""

    },
    "33": {
        "name": "North Carolina Avenue",
        "type": "property",
        "color": "green",
        "buy_price": 300,
        "rent": [26, 130, 390, 900, 1100, 1275],
        "house_cost": 200,
        "hotel_cost": 200
        , "owner": ""

    },
    "34": {
        "name": "Community Chest 3",
        "type": "community_chest"
        , "owner": "gov"

    },
    "35": {
        "name": "Pennsylvania Avenue",
        "type": "property",
        "color": "green",
        "buy_price": 320,
        "rent": [28, 150, 450, 1000, 1200, 1400],
        "house_cost": 200,
        "hotel_cost": 200
        , "owner": ""

    },
    "36": {
        "name": "Short Line",
        "type": "railroad",
        "buy_price": 200,
        "rent": [25, 50, 100, 200]
        , "owner": ""

    },
    "37": {
        "name": "Chance 3",
        "type": "chance"
        , "owner": "gov"

    },
    "38": {
        "name": "Park Place",
        "type": "property",
        "color": "dark_blue",
        "buy_price": 350,
        "rent": [35, 175, 500, 1100, 1300, 1500],
        "house_cost": 200,
        "hotel_cost": 200
        , "owner": ""
    },
    "39": {
        "name": "Luxury Tax",
        "type": "tax",
        "amount": 100
        , "owner": "gov"
    },
    "40": {
        "name": "Boardwalk",
        "type": "property",
        "color": "dark_blue",
        "buy_price": 400,
        "rent": [50, 200, 600, 1400, 1700, 2000],
        "house_cost": 200,
        "hotel_cost": 200
        , "owner": ""
    }
}
import colorama
import random
import map
import json
import yonesjail as yj
from farahani import mainmenu
lst_pay_bank = []
if __name__ == '__main__':
    re = mainmenu()
    if re == 'new':
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
        with open('current-game.json', 'r') as f:
            players_list = json.load(f)
        for i in range(1, 5):
            state['players'][i]['username'] = players_list[str(i)]
        already_tried_getting_out = []
        dices_after_prison = []
        should_skip = []
        lst_picked_same = []
        lst_just_got_out_of_jail = []
        players_square = dict()
        players = state["players"]
        for i in players:
            players_square[int(i)] = players[i]['position']
        player_num = state['current_turn']
        lst = state["lst"]
        n_lst = list(lst.values())
        already_tried_getting_out = n_lst[0]
        dices_after_prison = n_lst[1]
        should_skip = n_lst[2]
        lst_picked_same = n_lst[3]
        lst_just_got_out_of_jail = n_lst[4]
        with open('state.json', 'w') as f:
            json.dump(state, f, indent=4)
    elif re == 'load':
        try:
            state2 = dict()
            state2['players'] = dict()
            with open('previous_game.json', 'r') as f:
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
            already_tried_getting_out = []
            dices_after_prison = []
            should_skip = []
            lst_picked_same = []
            lst_just_got_out_of_jail = []
            players_square = dict()
            players = state["players"]
            for i in players:
                players_square[int(i)] = players[i]['position']
            player_num = state['current_turn']
            lst = state["lst"]
            n_lst = list(lst.values())
            already_tried_getting_out = n_lst[0]
            dices_after_prison = n_lst[1]
            should_skip = n_lst[2]
            lst_picked_same = n_lst[3]
            lst_just_got_out_of_jail = n_lst[4]
            with open('state.json', 'w') as f:
                json.dump(state, f, indent=4)
        except (FileNotFoundError, json.JSONDecodeError):
            print('No save game found! Plz play new game')
import golami as gm
from sh import random_chance_card, random_community_chest
colorama.init()
def load_game():
    with open('state.json', 'r') as f:
        state = json.load(f)
    state2 = dict()
    state2['players'] = dict()
    players = state["players"]
    for i in players:
        state2['players'][int(i)] = players[i]
    state2["current_turn"] = state["current_turn"]
    state2["lst"] = state["lst"]
    state = state2
    players = state['players']
    for player in players:
        for dictionary in players[player]['properties']:
            for pos in dictionary:
                pos_property = pos.replace('square', '')
                pos_property = pos_property.strip()
                monopoly_data[pos_property]['owner'] = player
                if monopoly_data[pos_property]['type'] == 'property':
                    monopoly_data[pos_property]['houses'] = dictionary[f'square {pos_property}'][1]
                    monopoly_data[pos_property]['hotel'] = dictionary[f'square {pos_property}'][2]
                    monopoly_data[pos_property]['mortgaged'] = dictionary[f'square {pos_property}'][3]
                if monopoly_data[pos_property]['type'] in ['utility', 'railroad']:
                    monopoly_data[pos_property]['mortgaged'] = dictionary[f'square {pos_property}'][1]
    return monopoly_data


def showing_option(player_num, square_num, players, code=True, debt=False):
    if players[player_num]['in_jail']:
        code = False
    orders = ['next']
    order_list = ['next -> move to next player']
    if debt or (players[player_num]['jail_turns'] == 2 and not already_tried_getting_out):
        order_list.remove('next -> move to next player')
    if players[player_num]['in_jail'] and not already_tried_getting_out and not debt:
        order_list.append('jail -> handle jail')
        orders.append('jail')
    if gm.find_all_can_build_houses(player_num, players) and code:
        order_list.append(f"house -> you can build some houses enter command to see list of it!")
        orders.append('house')
    if gm.is_land_buyable(player_num, square_num, players) and code:
        order_list.append(f"land -> you can buy land here with price of {monopoly_data[str(square_num)]['buy_price']} in color {monopoly_data[str(square_num)]['color']}")
        orders.append('land')
    if gm.find_all_can_build_hotel(player_num, players) and code:
        order_list.append(f"hotel -> you can build some houses enter command to see list of it!")
        orders.append('hotel')
    if gm.can_buy_railroad(player_num, square_num, players) and code:
        order_list.append(f"railroad -> you can buy railroad here with price of {monopoly_data[str(square_num)]['buy_price']}")
        orders.append('railroad')
    if gm.can_buy_utilities(player_num, square_num, players) and code:
        order_list.append(f"utility -> you can buy utility here with price of {monopoly_data[str(square_num)]['buy_price']}")
        orders.append('utility')
    if gm.houses_available_for_sale(player_num, players):
        order_list.append('sell_house -> you can sell some of your hotels choose this to see available ones')
        orders.append('sell_house')
    if gm.find_available_hotel(player_num, players):
        order_list.append('sell_hotel -> you can sell some of your houses choose this to see available ones')
        orders.append('sell_hotel')
    if gm.can_mortgage(player_num, players):
        order_list.append('mortgage -> you can mortgage some of your lands choose this to see available ones')
        orders.append('mortgage')
    if gm.find_mortgage_need(player_num, players) and not debt:
        order_list.append('unmortgage -> you can mortgage some of your lands choose this to see available ones')
        orders.append('unmortgage')
    str_orders = '\n'.join(order_list)
    return str_orders, orders


def menu(player_num, square_num, players, rent, code=True, debt=False, auto_next=False,):
    if auto_next and not debt:
        return
    input_is_not_valid = True
    print('/_ _ _ _ _ Choose from following options _ _ _ _ _ /')
    str_orders, orders = showing_option(player_num, square_num, players, code, debt)
    if players[player_num]['in_jail']:
        code = False
    if debt or (players[player_num]['jail_turns'] == 2 and not already_tried_getting_out):
        orders.remove('next')
    if len(orders) == 0:
        print(f'Player {player_num} you are '+colorama.Fore.RED + colorama.Style.BRIGHT+'ELIMINATED!' + colorama.Style.RESET_ALL)
        if square_num in [8, 23, 37, 3, 18, 34]:
            future_player = next_person_move(player_num)
            if not lst_pay_bank:
                gm.changing_owner(players, player_num, future_player, square_num)
        if gm.board[square_num - 1]['type'] == 'property' or gm.board[square_num - 1]['type'] == 'utility' or gm.board[square_num - 1]['type'] == 'railroad':
            players[gm.board[square_num - 1]['owner']]['money'] += players[player_num]['money']
            gm.changing_owner(players, player_num, gm.board[square_num - 1]['owner'], square_num)
        elif gm.board[square_num - 1]['type'] == "community_chest" or gm.board[square_num - 1]['type'] == "chance":
            if not lst_pay_bank:
                players[future_player]['money'] += players[player_num]['money']
        lst_pay_bank.clear()
        map.lose_player(f'p{player_num}', square_num)
        remove_player(player_num)
        return
    while input_is_not_valid:
        next_order = input(str_orders)
        if next_order in orders:
            input_is_not_valid = False
        else:
            print('Option is not possible! Please try again')
    if next_order == 'next':
        if players[player_num]['in_jail'] and not already_tried_getting_out:
            players[player_num]['jail_turns'] += 1
        if not lst_picked_same:
            player_num = next_person_move(player_num)
            if should_skip:
                should_skip.clear()
                player_num = next_person_move(player_num)
                print('i go for next person')
        return player_num
    if next_order == 'house' and code and not debt:
        lst = gm.find_all_can_build_houses(player_num, players)
        while True:
            option = input(f'here is list of lands you can build house on{lst}.enter your favourite option if you changed your mind enter -1')
            if option == '-1':
                return menu(player_num, square_num, players, rent, code, debt)
            elif option in lst:
                gm.build_house(player_num, int(option), players)
                code = False
                return menu(player_num, square_num, players, rent, code, debt)
            else:
                print('Invalid option! Plz try again')
    if next_order == 'hotel' and code and not debt:
        lst = gm.find_all_can_build_hotel(player_num, players)
        if not lst:
            return menu(player_num, square_num, players, rent, code, debt)
        while True:
            option = input(f'here is list of lands you can build hotel on{lst}.enter your favourite option if you changed your mind enter -1')
            if option == '-1':
                return menu(player_num, square_num, players, rent, code, debt)
            elif option in lst:
                gm.build_hotel(player_num, int(option), players)
                code = False
                return menu(player_num, square_num, players, rent, code, debt)
            else:
                print('Invalid option! Plz try again')
    if (next_order == 'railroad' or next_order == 'utility' or next_order == 'land') and code and not debt:
        gm.buy_property(player_num, square_num, players)
        code = False
        return menu(player_num, square_num, players, rent, code, debt, auto_next)
    if next_order == 'sell_hotel':
        hotels = gm.find_available_hotel(player_num, players)
        if not hotels:
            return menu(player_num, square_num, players, rent, code, debt)
        valid_option = True
        while valid_option:
            option = input(f'choose a house to sell:f{hotels},if you changed your mind type -1')
            if option == '-1':
                return menu(player_num, square_num, players, rent, code, debt)
            elif option in hotels:
                pos = int(option)
                gm.sell_hotel(player_num, pos, players)
                return menu(player_num, square_num, players, rent, code, debt)
            else:
                print('Your input is not valid! Plz try again')
        if players[player_num]['money'] >= rent and debt:
            debt = False
            code = True
            auto_next = True
        return menu(player_num, square_num, players, rent, code, debt,auto_next)
    if next_order == 'sell_house':
        houses = gm.houses_available_for_sale(player_num, players)
        if not houses:
            return menu(player_num, square_num, players, rent, code, debt)
        valid_option = True
        while valid_option:
            option = input(f'choose a house to sell:f{houses},if you changed your mind type -1')
            if option == '-1':
                return menu(player_num, square_num, players, rent, code, debt)
            elif option in houses:
                pos = int(option)
                gm.sell_house(player_num, pos, players)
                if players[player_num]['money'] >= rent and debt:
                    debt = False
                    code = True
                    auto_next = True
                return menu(player_num, square_num, players, rent, code, debt, auto_next)
            else:
                print('Your input is not valid! Plz try again')
    if next_order == 'mortgage':
        valid_option = True
        lst = gm.can_mortgage(player_num, players)
        if not lst:
            return menu(player_num, square_num, players, rent, code, debt)
        while valid_option:
            option = input(f'choose a land to mortgage:{lst},if you changed your mind type -1')
            if option == '-1':
                return menu(player_num, square_num, players, rent, code, debt)
            elif option in lst:
                pos = int(option)
                gm.mortgage_property(player_num, pos, players)
                if players[player_num]['money'] >= rent and debt:
                    debt = False
                    code = True
                    auto_next = True
                return menu(player_num, square_num, players, rent, code, debt,auto_next)
            else:
                print('Your input is not valid! Plz try again')
    if next_order == 'unmortgage' and not debt:
        while True:
            lst = gm.find_mortgage_need(player_num, players)
            if not lst:
                return menu(player_num, square_num, players, rent, code, debt)
            option = input(f'choose a land to unmortgage:{lst},if you changed your mind type -1')
            if option == '-1':
                return menu(player_num, square_num, players, rent, code, debt)
            elif option in lst:
                pos = int(option)
                gm.unmortgage_property(player_num, pos, players)
                return menu(player_num, square_num, players, rent, code, debt)
            else:
                print('Your input is not valid! Plz try again')
    if next_order == 'jail':
        already_tried_getting_out.append('/')
        result = yj.handle_jail(players, player_num)
        if result:
            if result == 'cancel':
                already_tried_getting_out.clear()
                return menu(player_num, square_num, players, rent, code, debt)
            elif result == 'handle_bankruptcy':
                Result = handle_bankruptcy(player_num, players, 50, square_num)
                if not Result:
                    player_num = next_person_move(player_num)
                    return player_num
                else:
                    return player_num
            else:
                if type(result) == tuple:
                    dices_after_prison.append(result[1])
                    return player_num
                else:
                    return player_num
        else:
            if player_num not in players:
                player_num = next_person_move(player_num)
                pre_player_num = player_num
                return player_num
            else:
                return menu(player_num, square_num, players, rent, code, debt)


def go_to_jail(player_num):
    print(f'Player{player_num} went to JAIL')
    players_square[player_num] = 11
    players[player_num]['in_jail'] = ['/']
    players[player_num]['position'] = 11


def new_turn(player_num, square_num, dice_sum=0):
    if players[player_num]['in_jail']:
        players[player_num]['in_jail'].append('/')
        return player_num, square_num, 0
    tas1 = random.randrange(1, 7)
    tas2 = random.randrange(1, 7)
    if dices_after_prison:
        tas1 = dices_after_prison.pop()
        tas2 = 0
        print('You move on with your dices')
    else:
        print('Dice1:', tas1, 'Dice2:', tas2)
    square_num += tas1 + tas2
    square_num = square_num % 41
    if square_num == 0:
        square_num = 1
    dice_sum = tas1 + tas2
    if tas1 == tas2:
        lst_picked_same.append('/')
    else:
        lst_picked_same.clear()
    players_square[player_num] = square_num
    return player_num, square_num, dice_sum


def next_person_move(player_num):  #  finds out who's turn is next
    player_num += 1
    player_num = player_num % 5
    if player_num == 0:
        L = players_square.keys()
        L = list(L)
        player_num = L[0]
    while player_num not in players_square:
        player_num += 1
        player_num = player_num % 5
        if player_num == 0:
            L = players_square.keys()
            L = list(L)
            player_num = L[0]
    return player_num


def remove_player(player_num):
    players_square.pop(player_num)  # if player does not  have money it gets eliminated
    players.pop(player_num)
    if len(players) == 1:
        print('Game Over')
        print('player won with this result:')
        print(players)
        os.remove('previous_game.json')
        print('exiting..... Bye!!')
        exit()
    return
def handle_bankruptcy(player_num, players, rent, square_num):
    while players[player_num]['money'] < rent:
        print(colorama.Fore.RED + colorama.Style.BRIGHT+'WARNING!'+colorama.Style.RESET_ALL+f'you have debt in amount of {-players[player_num]['money'] + rent}$')
        menu(player_num, square_num, players, rent, True, True)
        if player_num not in players:
            return
    print('Congratulations!you are no longer in debt!')
    players[player_num]['money'] -= rent
    return True


def save_game():
    with open('previous_game.json', 'w') as f:
        json.dump(state, f, indent=4)
    print('exiting......... Bye!')
    exit()
if __name__ == '__main__':
    for i in players:
        map.append_player(f'p{i}', players[i]['position'])
    while True:
        print(players)
        state['current_turn'] = player_num
        already_tried_getting_out.clear()
        print(colorama.Fore.GREEN + colorama.Style.BRIGHT + "---new turn starts!---" + colorama.Style.RESET_ALL)
        print(f"Your turn player {player_num}")
        op = input('do you want to save and exit or exit without saveing manage your properties before rolling dice?(yes/save/exit/or just enter to cancel)')
        square_num = players_square[player_num]
        if op == 'yes':
            lst_picked_same.append('/')
            menu(player_num, square_num, players, 0, False, False)
            lst_picked_same.remove('/')
        elif op == 'save':
            save_game()
        elif op == 'exit':
            break

        print(colorama.Fore.CYAN + '                                SCOREBOARD' + colorama.Style.RESET_ALL)
        print('--------------------------------------------------------------------------------')
        for i in players:
            print(players[i])
            print('--------------------------------------------------------------------------------')
        square_num = players_square[player_num]
        pre_square_num = square_num
        player_num, square_num, dice_sum = new_turn(player_num, square_num)
        if square_num == 31:
            go_to_jail(player_num)
            square_num = 11
        if len(lst_picked_same) == 3:
            lst_picked_same.clear()
            go_to_jail(player_num)
            square_num = 11
        rent = gm.calculate_rent(square_num, player_num, dice_sum)
        future_player = next_person_move(player_num)
        print(f'Player {player_num} in square {square_num}')
        map.move_player(player=f'p{player_num}',position=square_num)
        print(f'You have to pay {rent}$ of rent')
        skip = False
        got_money = False
        if pre_square_num >= square_num and not players[player_num]['in_jail']:
            players[player_num]['money'] += 200
            print('You got 200$ cause you passed GO!')
            got_money = 1
        if square_num in [8, 23, 37]:   # adding random card
            Random = random_chance_card(player_num, players)
            if Random == 'GO':
                square_num = 1
                if got_money != 1:
                    players[player_num]['money'] += 200
            elif Random == 'skip':
                skip = True
                should_skip.append('/')
            elif Random == 'nextp80' or Random == 'nextp50':
                future_player = next_person_move(player_num)
                if Random == 'nextp80':
                   if players[player_num]['money'] < 80:
                       rent += 80
                       handle_bankruptcy(player_num, players, 80, square_num)
                   else:
                       players[player_num]['money'] -= 80
                       players[future_player]['money'] += 80
                else:
                    if players[player_num]['money'] < 50:
                        handle_bankruptcy(player_num, players, 50, square_num)
                        rent += 50
                    else:
                        players[player_num]['money'] -= 50
                        players[future_player]['money'] += 50
            elif Random == 'boardwalk':
                square_num = 40
            elif Random == 'jail':
                go_to_jail(player_num)
            elif Random == 'b15':
                if players[player_num]['money'] >= 15:
                    players[player_num]['money'] -= 15
                else:
                    lst_pay_bank.append('/')
                    handle_bankruptcy(player_num, players, 15, square_num)


        elif square_num in [3, 18, 34]:
            Random = random_community_chest(player_num, players)
            if Random == 'cnext100':
                next_player = next_person_move(player_num)
                if players[player_num]['money'] < 100:
                    rent += 100
                    handle_bankruptcy(player_num, players, 100, square_num)
                else:
                    players[player_num]['money'] -= 100
                    players[next_player]['money'] += 100
            elif Random == "move to free parking":
                square_num = 21
            elif Random == 'cnextp150':
                next_player = next_person_move(player_num)
                if players[player_num]['money'] < 150:
                    rent += 150
                    handle_bankruptcy(player_num, players, 150, square_num)
                else:
                    players[player_num]['money'] -= 150
                    players[next_player]['money'] += 150
            elif Random == 'sell_house':
                lst_houses = gm.houses_available_for_sale(player_num, players)
                if not lst_houses:
                    print('since you dont have any house available for sell you will continue!')
                else:
                    option = input(f'{lst_houses}choose one of your houses to sell')
                    while option not in lst_houses:
                        print('invalid input! try again')
                        option = input(f'{lst_houses}choose one of your houses to sell')
                    option = int(option)
                    gm.sell_house(player_num, option, players)
            elif Random == 'skip':
                skip = True
                should_skip.append('/')
            elif Random == 'b100':
                if players[player_num]['money'] >= 100:
                    players[player_num]['money'] -= 100
                else:
                    lst_pay_bank.append('/')
                    handle_bankruptcy(player_num, players, 100, square_num)

        if player_num not in players:
            player_num = next_person_move(player_num)
            continue
        if len(players[player_num]['in_jail']) == 1: # if its first time player enters jail, his turn ends and he can't do anything
            lst_picked_same.clear()
            print("You just entered jail and you can't do any thing!")
            if should_skip:
                player_num = next_person_move(player_num)
                should_skip.clear()
            player_num = next_person_move(player_num)
            map.move_player(player=f'p{player_num}', position=square_num)
            continue
        if player_num in players:
            if players[player_num]['money'] < rent:
                handle_bankruptcy(player_num, players, rent, square_num)
            else:
                if rent > 0:
                    players[player_num]['money'] -= rent
                    gm.giving_money_to_player(player_num, square_num, players, rent, future_player)
            if player_num in players:
                players[player_num]['position'] = square_num
                print('Your current state is:   propertiesInfo:(color, houses, hotel, mortgaged)/utility, mortgaged/rail, mortgaged')
                print(players[player_num])
                gm.show_info_of_current_space(square_num)
                player_num = menu(player_num, square_num, players, rent,  True, False, False)
            else:
                player_num = next_person_move(player_num)
        else:
            if should_skip:
                player_num = next_person_move(player_num)
                should_skip.clear()
            player_num = next_person_move(player_num)


import tkinter as tk
import colorama
colorama.init()

import random
import golami as gm
from board_setup import monopoly_data
from load_save import state
window = tk.Tk()
"""
player_num = 1
players_square = dict()
for i in range(1, 5):
    players_square[i] = 1
"""

players_square = dict()
players = state["players"]
player = 1
for i in players:
    players_square[i] = players[i]['position']
player_num = state['current_turn']




def showing_option(player_num, square_num, players):
    orders = ['next']
    order_list = ['next -> move to next player']
    if gm.can_build_house(player_num, square_num, players):
        order_list.append(f"house -> you can build home here with price of {monopoly_data[str(square_num)]['house_cost']} in color {monopoly_data[str(square_num)]['color']}")
        orders.append('house')
    if gm.is_land_buyable(player_num, square_num, players):
        order_list.append(f"land -> you can buy land here with price of {monopoly_data[str(square_num)]['buy_price']} in color {monopoly_data[str(square_num)]['color']}")
        orders.append('land')
    if gm.can_build_hotel(player_num, square_num, players):
        order_list.append(f"hotel -> you can build home here with price of {monopoly_data[str(square_num)]['hotel_cost']} in color {monopoly_data[str(square_num)]['color']}")
        orders.append('hotel')
    if gm.can_buy_railroad(player_num, square_num, players):
        order_list.append(f"railroad -> you can buy railroad here with price of {monopoly_data[str(square_num)]['buy_price']}")
        orders.append('railroad')
    if gm.can_buy_utilities(player_num, square_num, players):
        order_list.append(f"utility -> you can buy utility here with price of {monopoly_data[str(square_num)]['buy_price']}")
        orders.append('utility')
    if gm.find_available_houses(player_num, players)[1]:
        order_list.append('sell_house -> you can sell some of your hotels choose this to see available ones')
        orders.append('sell_house')
    if gm.find_available_hotel(player_num, players)[1]:
        order_list.append('sell_hotel -> you can sell some of your houses choose this to see available ones')
        orders.append('sell hotel')
    str_orders = '\n'.join(order_list)
    return str_orders, orders

def sell_functions():
    print()
def go_to_jail(player_num):
    print(f'player{player_num} went to jail')
    players_square[player_num] = 11


def new_turn(player_num, square_num, dice_sum=0, picked_same=0):
    if picked_same == 3:
        picked_same = 0
        go_to_jail(player_num)
        print(f'player{player_num} went to jail')
        return player_num, 11, dice_sum, picked_same
    tas1 = random.randrange(1, 7)
    tas2 = random.randrange(1, 7)
    print('tas1:',tas1,'tas2:',tas2)
    square_num += tas1 + tas2
    square_num = square_num % 41
    if square_num == 0:
        square_num = 1
    dice_sum = tas1 + tas2
    if tas1 == tas2:
        print('jackpot!')
        picked_same += 1
        player_num, square_num, dice_sum, picked_same = new_turn(player_num, square_num, dice_sum, picked_same )

    else:
        picked_same = 1
        players_square[player_num] = square_num
    return player_num, square_num, (tas1 + tas2), picked_same

def next_person_move(player_num):  #  finds out who's turn is next
    player_num += 1
    while player_num not in players_square:
        player_num += 1
        player_num = player_num % (len(players_square) + 1)
        if player_num == 0:
            player_num = list(players_square.keys())[0]  # goes back to first of loop then goes into new turn
    return player_num


def remove_player(player_num):
    players_square.pop(player_num)  # if player does not  have money it gets eliminated
    players.pop(player_num)



while True:
    print(colorama.Fore.GREEN + colorama.Style.BRIGHT + "---new turn starts!---" + colorama.Style.RESET_ALL)
    square_num = players_square[player_num]
    pre_square_num = square_num
    player_num, square_num, dice_sum, picked_same = new_turn(player_num, square_num)
    rent = gm.calculate_rent(square_num, player_num, dice_sum)
    print(f'player {player_num} in square {square_num}')
    print(f'you have to pay {rent}$ of rent')
    if pre_square_num >= square_num:
        players[player_num]['money'] += 200
        print('you got 200$ cause you passed GO!')
    if players[player_num]['money'] < rent:
        gm.handle_bankruptcy()
    else:
        if rent > 0:
            players[player_num]['money'] -= rent
            gm.giving_money_to_player(player_num, square_num, players, rent)
    players[player_num]['position'] = square_num
    print('your current state is:    propertiesInfo:(color, houses, hotel)/utility/rail')
    print(players[player_num])
    gm.show_info_of_current_space(square_num)
    input_is_not_valid = True
    print('/_ _ _ _ _ choose from following options _ _ _ _ _ /')
    str_orders, orders = showing_option(player_num, square_num, players)
    print(player_num,'//////////////////////////////')
    while input_is_not_valid:
        next_order = input(str_orders)
        if next_order in orders:
            input_is_not_valid = False
        else:
            print('option is not possible! please try again')
    can_do_another_move = True
    while can_do_another_move:
        if next_order == 'next':
            player_num = next_person_move(player_num)
            can_do_another_move = False
        if next_order == 'house' :
            gm.build_house(player_num, square_num, players)
            player_num = next_person_move(player_num)
            can_do_another_move = False
        if next_order == 'hotel':
            gm.build_hotel(player_num, square_num, players)
            player_num = next_person_move(player_num)
            can_do_another_move = False
        if next_order == 'railroad' or next_order == 'utility' or next_order == 'land':
            gm.buy_property(player_num, square_num, players)
            player_num = next_person_move(player_num)
            can_do_another_move = False
        if next_order == 'sell_hotel':
            hotels = gm.find_available_hotel(player_num, players)
            can_do_another_move = True
        if next_order == 'sell_house':
            can_do_another_move = True
            houses = gm.houses_available_for_sale(player_num, players)
            option = input(f'choose a house to sell:f{houses}')
            pos = int(option) - 1
            gm.sell_house(player_num, pos, players)

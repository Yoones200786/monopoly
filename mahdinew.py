import random
import golami as gm
from board_setup import monopoly_data
from load_save import state
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
    orders = []
    order_list = ['next -> move to next player']
    if gm.can_build_house(player_num, square_num, players):
        order_list.append(f"""house -> you can build home here with price of {monopoly_data[square_num]['house_cost']}
         in color {monopoly_data[square_num]['color']} in square_num {square_num}\n""")
        orders.append('house')
    if gm.is_land_buyable(player_num, square_num, players):
        order_list.append(f"""land -> you can buy land here with price of {monopoly_data[square_num]['buy_price']}
                 in color {monopoly_data[square_num]['color']} in square_num {square_num}\n""")
        orders.append('land')
    if gm.can_build_hotel(player_num, square_num, players):
        order_list.append(f"""hotel -> you can build home here with price of {monopoly_data[square_num]['hotel_cost']}
                 in color {monopoly_data[square_num]['color']} in square_num {square_num}\n""")
        orders.append('hotel')
    str_option = ''.join(order_list)
    return str_option, orders




def go_to_jail(player_num):
    print(f'player{player_num} went to jail')
    players_square[player_num] = 11




def new_turn(player_num, square_num, picked_same=0):
    if picked_same == 3:
        picked_same = 1
        go_to_jail(player_num)
        print(f'player{player_num} went to jail')
        return
    tas1 = random.randrange(1, 7)
    tas2 = random.randrange(1, 7)
    square_num += tas1 + tas2
    square_num = square_num % 41
    if square_num == 0:
        square_num = 1
    if tas1 == tas2:
        picked_same += 1
        player_num, square_num = new_turn(player_num, square_num, picked_same)

    else:
        picked_same = 1
        players_square[player_num] = square_num
    return player_num, square_num, (tas1 + tas2)

def next_person_move(player_num):
    player_num += 1
    while player_num not in players_square:
        player_num += 1
        player_num = player_num % (len(players_square) + 1)
        if player_num == 0:
            player_num = list(players_square.keys())[0]  # goes back to first of loop then goes into new turn
    return player_num

def removeplayer(player_num):
    players_square.pop(player_num)  # if player does not  have money it gets eliminated



while True:
    print('---new turn starts---')
    square_num = players_square[player_num]
    pre_square_num = square_num
    player_num, square_num, dice_sum = new_turn(player_num, square_num)
    gm.calculate_rent(square_num, player_num, dice_sum)
    if pre_square_num >= square_num:
        players[player_num]['money'] += 200
#    if house can be bought add option of buying in order list (and player have enough money to buy it)
#    we should also add option of buying house or making hotel
#    in this place we can realize that player run out of money and loses we call remove function
    #   all possible messages should be in this
    orders_dict = {'buy': 'buy -> buy current road', 'next': 'next -> next to next person'}
    input_is_not_valid = True
    print(f'player {player_num} in square {square_num}')
    print('/_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ /')
    str_orders, orders = showing_option(player_num, square_num, players)
    while input_is_not_valid:
        next_order = input(showing_option(player_num, square_num, players))
        if next_order in orders:
            input_is_not_valid = False
        else:
            print('option is not possible! please try again')
    if next_order == 'next':
        player_num = next_person_move(player_num)
    if next_order == 'house':
        gm.build_house(player_num, square_num, players)
        player_num = next_person_move(player_num)
    if next_order == 'hotel':
        gm.build_hotel(player_num, square_num, players)
        player_num = next_person_move(player_num)

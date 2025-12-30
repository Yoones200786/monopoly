import colorama
colorama.init()
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


def showing_option(player_num, square_num, players, code=True, debt=False):
    orders = ['next']
    order_list = []
    if not debt:
        order_list = ['next -> move to next player']
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
        orders.append('sell hotel')
    if gm.can_mortgage(player_num, players):
        order_list.append('mortgage -> you can mortgage some of your lands choose this to see available ones')
        orders.append('mortgage')
    if gm.find_mortgage_need(player_num, players):
        order_list.append('unmortgage -> you can mortgage some of your lands choose this to see available ones')
        orders.append('unmortgage')



    str_orders = '\n'.join(order_list)
    return str_orders, orders


def menu(player_num, square_num, players, rent, code=True, debt=False):
    input_is_not_valid = True
    print('/_ _ _ _ _ choose from following options _ _ _ _ _ /')
    str_orders, orders = showing_option(player_num, square_num, players, code, debt)
    if debt:
        orders.remove('next')

    if len(orders) == 0:
        print(f'player {player_num} you are '+colorama.Fore.RED + colorama.Style.BRIGHT+'ELIMINATED!' + colorama.Style.RESET_ALL)
        gm.changing_owner(player_num, square_num)
        remove_player(player_num)
        player_num = next_person_move(player_num)
        return
    while input_is_not_valid:
        next_order = input(str_orders)
        if next_order in orders:
            input_is_not_valid = False
        else:
            print('option is not possible! please try again')
        if next_order == 'next':
            player_num = next_person_move(player_num)
            return player_num
        if next_order == 'house' and code:
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
                    print('invalid option! plz try again')
        if next_order == 'hotel' and code:
            lst = gm.find_all_can_build_hotel(player_num, players)
            while True:
                option = input(f'here is list of lands you can build hotel on{lst}.enter your favourite option if you changed your mind enter -1')
                if option == '-1':
                    return menu(player_num, square_num, players, rent, code, debt)
                elif option in lst:
                    gm.build_hotel(player_num, int(option), players)
                    code = False
                    return menu(player_num, square_num, players, rent, code, debt)
                else:
                    print('invalid option! plz try again')
        if (next_order == 'railroad' or next_order == 'utility' or next_order == 'land') and code:
            gm.buy_property(player_num, square_num, players)
            code = False
            return menu(player_num, square_num, players, rent, code, debt)
        if next_order == 'sell_hotel':
            hotels = gm.find_available_hotel(player_num, players)
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
                    print('your input is not valid! plz try again')
            if players[player_num]['money'] >= rent and debt:
                debt = False
                code = True
            return menu(player_num, square_num, players, rent, code, debt)
        if next_order == 'sell_house':
            houses = gm.houses_available_for_sale(player_num, players)
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
                        print('congratulations!you are no longer in debt!')
                    return menu(player_num, square_num, players, rent, code, debt)
                else:
                    print('your input is not valid! plz try again')
        if next_order == 'mortgage':
            valid_option = True
            lst = gm.can_mortgage(player_num, players)
            while valid_option:
                option = input(f'choose a land to mortgage:{lst},if you changed your mind type -1')
                print(option, lst)
                print(option in lst)
                if option == '-1':
                    return menu(player_num, square_num, players, rent, code, debt)

                elif option in lst:
                    pos = int(option)
                    gm.mortgage_property(player_num, pos, players)
                    if players[player_num]['money'] >= rent and debt:
                        debt = False
                        code = True
                    return menu(player_num, square_num, players, rent, code, debt)
                else:
                    print('your input is not valid! plz try again')
        if next_order == 'unmortgage' and not debt:
            while True:
                lst = gm.find_mortgage_need(player_num, players)
                option = input(f'choose a land to unmortgage:{lst},if you changed your mind type -1')
                if option == '-1':
                    return menu(player_num, square_num, players, rent, code, debt)
                elif option in lst:
                    pos = int(option)
                    print('hi')
                    gm.unmortgage_property(player_num, pos, players)
                    return menu(player_num, square_num, players, rent, code, debt)
                else:
                    print('your input is not valid! plz try again')


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
    if len(players) == 1:
        print('game over')


def handle_bankruptcy(player_num, players, rent):
    while players[player_num]['money'] < rent:
        print(colorama.Fore.RED + colorama.Style.BRIGHT+'WARNING!'+colorama.Style.RESET_ALL+f'you have debt in amount of {-players[player_num]['money'] + rent}$')
        menu(player_num, square_num, players, rent, True, True)
        if player_num not in players:
            return


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
        handle_bankruptcy(player_num, players, rent)

    else:
        if rent > 0:
            players[player_num]['money'] -= rent
            gm.giving_money_to_player(player_num, square_num, players, rent)
    if player_num in players:
        players[player_num]['position'] = square_num
        print('your current state is:    propertiesInfo:(color, houses, hotel)/utility/rail')
        print(players[player_num])
        gm.show_info_of_current_space(square_num)
        player_num = menu(player_num, square_num, players, rent)
    else:
        player_num = next_person_move(player_num)

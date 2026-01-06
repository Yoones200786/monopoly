import colorama
colorama.init()
import random
import golami as gm
import yonesjail as yj
from board_setup import monopoly_data
from load_save import state
from sh import random_chance_card, random_community_chest
import map

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
    if gm.find_mortgage_need(player_num, players):
        order_list.append('unmortgage -> you can mortgage some of your lands choose this to see available ones')
        orders.append('unmortgage')
    str_orders = '\n'.join(order_list)
    return str_orders, orders


def return_already_tried_getting_out():
    return already_tried_getting_out


def menu(player_num, square_num, players, rent, code=True, debt=False, auto_next=False,):
    if auto_next and not debt:
        return
    input_is_not_valid = True
    print('/_ _ _ _ _ choose from following options _ _ _ _ _ /')
    str_orders, orders = showing_option(player_num, square_num, players, code, debt)
    if players[player_num]['in_jail']:
        code = False
    if debt or (players[player_num]['jail_turns'] == 2 and not already_tried_getting_out):
        orders.remove('next')
    if len(orders) == 0:
        print(f'player {player_num} you are '+colorama.Fore.RED + colorama.Style.BRIGHT+'ELIMINATED!' + colorama.Style.RESET_ALL)
        if square_num in [8, 23, 37, 3, 18, 34]:
            future_player = next_person_move(player_num)
        gm.changing_owner(player_num, square_num)
        if gm.board[square_num - 1]['type'] == 'property':
            players[gm.board[square_num - 1]['owner']]['money'] += players[player_num]['money']
        elif gm.board[square_num - 1]['type'] == "community_chest" or gm.board[square_num - 1]['type'] == "chance":
            players[future_player]['money'] += players[player_num]['money']
        remove_player(player_num)
#        player_num = next_person_move(player_num)
#        return player_num
        return
    while input_is_not_valid:
        next_order = input(str_orders)
        if next_order in orders:
            input_is_not_valid = False
        else:
            print('option is not possible! please try again')
    if next_order == 'next':
        if players[player_num]['in_jail'] and not already_tried_getting_out:
            players[player_num]['jail_turns'] += 1
        if not lst_picked_same and not lst_just_got_out_of_jail:
            player_num = next_person_move(player_num)
        if lst_just_got_out_of_jail:
            lst_just_got_out_of_jail.clear()
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
                print('invalid option! plz try again')
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
                print('invalid option! plz try again')
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
                print('your input is not valid! plz try again')
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
                print('your input is not valid! plz try again')
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
                print('your input is not valid! plz try again')
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
                print('your input is not valid! plz try again')
    if next_order == 'jail':
        already_tried_getting_out.append('/')
        result = yj.handle_jail(players, player_num)
        return_already_tried_getting_out()
        if result:
            if result == 'cancel':
                return menu(player_num, square_num, players, rent, code, debt)
            elif result == 'handle_bankruptcy':
                Result = handle_bankruptcy(player_num, players, 50, square_num)
                if not Result:
                    player_num = next_person_move(player_num)
                    return player_num
                else:
                    return player_num

            else:
                lst_just_got_out_of_jail.append('/')
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
    print(f'player{player_num} went to JAIL')
    players_square[player_num] = 11
    players[player_num]['in_jail'].append('/')
    players[player_num]['position'] = 11


def new_turn(player_num, square_num, dice_sum=0):
    if players[player_num]['in_jail']:
        players[player_num]['in_jail'].append('/')
        return player_num, square_num, 0
    tas1 = random.randrange(1, 7)
    tas2 = random.randrange(1, 7)
    #tas1 = 1
    #tas2 = 1
    if dices_after_prison:
        tas1 = dices_after_prison.pop()
        tas2 = 0
        print('you move on with your dices')
    else:
        print('tas1:', tas1, 'tas2:', tas2)
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
    while player_num not in players_square:
        player_num += 1
        player_num = player_num % (len(players_square) + 1)
        if player_num == 0:
            player_num = list(players_square.keys())[0]  # goes back to first of loop then goes into new turn
    return player_num


def remove_player(player_num):
    players_square.pop(player_num)  # if player does not  have money it gets eliminated
    print(players_square)
    players.pop(player_num)
    if len(players) == 1:
        print('game over')


def handle_bankruptcy(player_num, players, rent, square_num):
    while players[player_num]['money'] < rent:
        print(colorama.Fore.RED + colorama.Style.BRIGHT+'WARNING!'+colorama.Style.RESET_ALL+f'you have debt in amount of {-players[player_num]['money'] + rent}$')
        menu(player_num, square_num, players, rent, True, True)
        if player_num not in players:
            return
    print('congratulations!you are no longer in debt!')
    players[player_num]['money'] -= rent
    return True


def load_game():
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
    return monopoly_data


if __name__ == "__main__":
    map.append_player(player="p1",position=1)
    map.append_player(player="p2",position=1)
    map.append_player(player="p3",position=1)
    map.append_player(player="p4",position=1)
    while True:

        state['current_turn'] = player_num
        already_tried_getting_out.clear()
        print(colorama.Fore.GREEN + colorama.Style.BRIGHT + "---new turn starts!---" + colorama.Style.RESET_ALL)
        print(f"your turn player {player_num}")
        op = input('do you want to save or manage your properties before rolling dice?(save/manage/or just enter to cancel)')
        square_num = players_square[player_num]
        if op == 'yes':
            lst_picked_same.append('/')
            menu(player_num, square_num, players, 0, False, False)
            lst_picked_same.remove('/')
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

        print("hdjdkd")



        print(f'player {player_num} in square {square_num}')


        map.move_player(player=f"p{player_num}",position=square_num)
        print(f'you have to pay {rent}$ of rent')
        skip = False
        got_money = False
        if pre_square_num >= square_num and not players[player_num]['in_jail']:
            players[player_num]['money'] += 200
            print('you got 200$ cause you passed GO!')
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
        elif square_num in [3, 18, 34]:  #adding community chest
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
            elif Random == 'skip':
                skip = True
                should_skip.append('/')
        if len(players[player_num]['in_jail']) == 1: # if its first time player enters jail, his turn ends and he can't do anything
            lst_picked_same.clear()
            print("you just entered jail and you can't do any thing!")
            if should_skip:
                player_num = next_person_move(player_num)
                should_skip.clear()
            player_num = next_person_move(player_num)
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
                print('your current state is:    propertiesInfo:(color, houses, hotel)/utility/rail')
                print(players[player_num])
                gm.show_info_of_current_space(square_num)
                if should_skip and not lst_picked_same:
                    player_num = next_person_move(player_num)
                    should_skip.clear()
                player_num = menu(player_num, square_num, players, rent,  True, False, False)
            else:
                player_num = next_person_move(player_num)
        else:
            player_num = next_person_move(player_num)
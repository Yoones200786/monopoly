import random
player_num = 1
players_square = dict()
for i in range(1, 5):
    players_square[i] = 1


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
    return player_num, square_num


def removeplayer(player_num):
    players_square.pop(player_num)  # if player lost remove


player_num = list(players_square.keys())[0]
while True:
    print('---new turn starts---')
    square_num = players_square[player_num]
    player_num, square_num = new_turn(player_num, square_num)
    order_list = ['next']
#    if house can be bought add option of buying in order list (and player have enough money to buy it)
#    we should also add option of buying house or making hotel
#    in this place we can realize that player run out of money and loses we call remove function
    str_options = '  \n'.join(order_list)                              # crating  str of available options
    #   all possible messages should be in this
    orders_dict = {'buy': 'buy -> buy current road', 'next': 'next -> next to next person'}
    input_is_not_valid = True
    print(f'player {player_num} in square {square_num}')
    print('/_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ /')
    while input_is_not_valid:
        #   current msg in input is for example it will be input(str_options)
        next_order = input('choose from following options:\n'
                       'next -> next to next person\n'
                       'buy -> buy current road')
        if next_order in order_list:
            input_is_not_valid = False
        else:
            print('option is not possible! please try again')
    if next_order == 'next':
        player_num += 1
        while player_num not in players_square:
            player_num += 1
            player_num = player_num % (len(players_square) + 1)
            if player_num == 0:
                player_num = list(players_square.keys())[0] # goes back to first of loop then goes into new turn


import random
import golami
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
    players_square.pop(player_num) # if player lost remove

player_num = list(players_square.keys())[0]
while True:
    print(f'starting with the player {player_num}')
    print(new_turn(player_num, players_square[player_num]))
    if input(f'Would you like to move to next person(y/n), previous person was player number {player_num}') == 'y':
        player_num += 1
        while player_num not in players_square:
            player_num += 1
            player_num = player_num % (len(players_square) + 1)
            if player_num == 0:
                player_num = list(players_square.keys())[0]


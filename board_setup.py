from mahdinewdebugforjail import load_game
monopoly_data = load_game()
print(monopoly_data)
board = [None] * 40
for key in monopoly_data:
    pos = int(key) - 1
    board[pos] = monopoly_data[key].copy()


def initialize_board():
    for i in range(40):
        space = board[i]
        if space["type"] in ["property", "railroad", "utility"]:
            space["owner"] = None
            space["mortgaged"] = False
            if space["type"] == "property":
                space["houses"] = 0
color_groups = {
    "brown": [2, 4],
    "light_blue": [7, 9, 10],
    "pink": [12, 14, 15],
    "orange": [17, 19, 20],
    "red": [22, 24, 25],
    "yellow": [27, 28, 30],
    "green": [32, 33, 35],
    "dark_blue": [38, 40],
}
railroad_positions = [6, 16, 26, 36]
utility_positions = [13, 29]

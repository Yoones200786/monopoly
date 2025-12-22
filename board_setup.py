monopoly_data = {
    "1": {
        "name": "GO",
        "type": "special",
        "action": "collect",
        "amount": 200
    },
    "2": {
        "name": "Mediterranean Avenue",
        "type": "property",
        "color": "brown",
        "buy_price": 60,
        "rent": [2, 10, 30, 90, 160, 250],
        "house_cost": 50,
        "hotel_cost": 50
    },
    "3": {
        "name": "Community Chest 1",
        "type": "community_chest"
    },
    "4": {
        "name": "Baltic Avenue",
        "type": "property",
        "color": "brown",
        "buy_price": 60,
        "rent": [4, 20, 60, 180, 320, 450],
        "house_cost": 50,
        "hotel_cost": 50
    },
    "5": {
        "name": "Income Tax",
        "type": "tax",
        "amount": 200
    },
    "6": {
        "name": "Reading Railroad",
        "type": "railroad",
        "buy_price": 200,
        "rent": [25, 50, 100, 200]
    },
    "40": {
        "name": "Boardwalk",
        "type": "property",
        "color": "dark_blue",
        "buy_price": 400,
        "rent": [50, 200, 600, 1400, 1700, 2000],
        "house_cost": 200,
        "hotel_cost": 200
    }
}
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
    "brown": [1, 3],
    "light_blue": [6, 8, 9],
    "pink": [11, 13, 14],
    "orange": [16, 18, 19],
    "red": [21, 23, 24],
    "yellow": [26, 27, 29],
    "green": [31, 32, 34],
    "dark_blue": [37, 39],
}
railroad_positions = [5, 15, 25, 35]
utility_positions = [12, 28]
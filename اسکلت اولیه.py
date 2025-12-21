import json
def load_board(path="data/board.json"):
    with open(path, "r") as f:
        return json.load(f)
def load_players(path="data/players.json"):
    with open(path, "r") as f:
        return json.load(f)
def save_players(players, path="data/players.json"):
    with open(path, "w") as f:
        json.dump(players, f, indent=2)
def find_player(players, player_id):
    for p in players:
        if p["id"] == player_id:
            return p
    return None
def find_property(board, property_id):
    for prop in board:
        if prop["id"] == property_id:
            return prop
    return None
def can_afford(player, amount):
    return player["cash"] >= amount
def transfer_money(players, from_id, to_id, amount):
    pass
def buy_property(players, board, player_id, property_id):
    pass
def calculate_rent(board, property_id, dice_total=None, players=None):
    pass
def pay_rent(players, board, payer_id, property_id, dice_total=None):
    pass
def mortgage_property(players, board, player_id, property_id):
    pass

def lift_mortgage(players, board, player_id, property_id):
    pass
def sell_property(players, board, seller_id, property_id, buyer_id=None, price=None):
    pass
def liquidate_assets(players, board, player_id, required_amount):
    pass
def handle_bankruptcy(players, board, player_id, creditor_id=None):
    pass
def render_scoreboard(players, board):
    pass

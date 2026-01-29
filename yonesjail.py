# Send player to jail
import random
# Manage jail options
def handle_jail(players, player_id):
    player = players[player_id]
    print(f'\n{player["username"]} is in jail')
    while True:
        print("\nChoose an option:")
        print("1 - Pay 50$")
        print("2 - Use get out of jail free card")
        print("3 - Try for a double")
        print("4 - Quit")
        try:
            choice = int(input("Selected option: "))
            if choice not in (1, 2, 3, 4):
                print("Invalid choice. Try again.")
                continue
        except ValueError:
            print("Please enter a number.")
            continue
        # Pay 50$ to leave
        if choice == 1:
            if player["money"] < 50:
                print("Not enough money")
                continue
            player["money"] -= 50
            player["in_jail"].clear()
            player["jail_turns"] = 0
            print("You paid 50$ and got out of jail! you will continue your turn.")
            return True
        # Use get out of jail card
        elif choice == 2:
            if player["get_out_of_jail_cards"] != 1:
                print("You don't have a get out of jail free card")
                continue
            player["in_jail"].clear()
            player['get_out_of_jail_cards'] -= 1
            player["jail_turns"] = 0
            print("You used a card and got out of jail! you will continue your turn.")
            return True
        # Try for a double
        elif choice == 3:
            d1 = random.randint(1, 6)
            d2 = random.randint(1, 6)
            print(f"Dice rolled: {d1}, {d2}")
            if d1 == d2:
                player["in_jail"].clear()
                player["jail_turns"] = 0
                print("Double! You are free and move forward")
                return True, (d1+d2)
            else:
                player["jail_turns"] += 1
                print("Not a double")
                # After 3 turns, pay or sell
                if player["jail_turns"] >= 3:
                    if player["money"] < 50:
                        return 'handle_bankruptcy'
                    else:
                        player["money"] -= 50
                        player["in_jail"].clear()
                        player["jail_turns"] = 0
                        print("3 turns passed, paid 50$ and got out")
                        return True
                else:
                    return False
        elif choice == 4:
            return 'cancel'

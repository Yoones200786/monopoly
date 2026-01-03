# Send player to jail
import random


def send_to_jail(player):
    player["position"] = 11
    player["in_jail"] = True
    player["jail_turns"] = 0
    print(f'{player["username"]} went to jail')

# Manage jail options


def handle_jail(player, player_cards, chance_card):
    print(f'\n{player["username"]} is in jail')

    while True:
        print("\nChoose an option:")
        print("1 - Pay 50$")
        print("2 - Use get out of jail free card")
        print("3 - Try for a double")

        try:
            choice = int(input("Selected option: "))
            if choice not in (1, 2, 3):
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
            player["in_jail"] = False
            player["jail_turns"] = 0
            print("You paid 50$ and got out of jail")
            break

        # Use get out of jail card
        elif choice == 2:
            if "get out of jail free" not in player_cards:
                print("You don't have a get out of jail free card")
                continue


            player_cards.remove("get out of jail free")


            chance_card.append("get out of jail free")

            player["in_jail"] = False
            player["jail_turns"] = 0
            print("You used a card and got out of jail")
            break

        # Try for a double
        elif choice == 3:
            d1 = random.randint(1, 6)
            d2 = random.randint(1, 6)
            print(f"Dice rolled: {d1}, {d2}")

            if d1 == d2:
                player["in_jail"] = False
                player["jail_turns"] = 0
                player["position"] = (player["position"] + d1 + d2) % 40
                print("Double! You are free and move forward")
                break
            else:
                player["jail_turns"] += 1
                print("Not a double")
                # After 3 turns, pay or sell
                if player["jail_turns"] >= 3:
                    if player["money"] < 50:
                        print("Not enough money after 3 turns")


                        while player["money"] < 50:
                            print("You need to sell houses/hotels to get enough money.")
                            print("1 - Sell a house")
                            print("2 - Sell a hotel")
                            print("3 - Declare bankruptcy")
                            choice = input("Select option: ")
                            # Sell house
                            if choice == "1":
                                sell_house(player_id, position, players)
                            # Sell hotel
                            elif choice == "2":
                                sell_hotel(player_id, position, players)
                            elif choice == "3":
                                handle_bankruptcy(players, player_id, creditor_id=None)
                                break
                            else:
                                print("Invalid choice.")
                            # Check again if the player has enough money
                            if player["money"] >= 50:
                                break  # If the player has enough money, exit the loop

                    player["money"] -= 50
                    player["in_jail"] = False
                    player["jail_turns"] = 0
                    print("3 turns passed, paid 50$ and got out")
                    break

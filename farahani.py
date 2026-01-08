import re
import uuid
import bcrypt
import json
from sh import leaderboard
with open("current-game.json","r") as f:
    username_dict = json.load(f)
def mainmenu():
    print("\033[1;32mWelcome to Monopoly!\033[0m\n")
    print("1. New Game")
    print("2. Load Game")
    print("3. Leaderboard")
    print("4. Exit")
    choice = input ("Enter your choice (1-4):")
    if choice =="1":
        return signupmenu()
    elif choice =="2":
        return loadgame()
    elif choice =="3":
        def informations(id,username,position=0,in_jail=False,jail_turns=0,money=1500,properties=None):
            if properties is None:
                properties = []
            return{
                "id": id,
                "username": username,
                "position": position,
                "in_jail": in_jail,
                "jail_turns": jail_turns,
                "money": money,
                "properties": properties
            }
        

        p1=informations(id=1, username=username_dict["1"], position=10, in_jail=False, jail_turns=2, money=2000, properties=["Park Place", "Boardwalk"])
        p2 = informations(2, username_dict["2"], position=5, in_jail=True, jail_turns=2, money=1200, properties=["Baltic Ave"])
        p3 = informations(3, username_dict["3"], position=15, in_jail=False, jail_turns=0, money=1800)
        p4 = informations(4, username_dict["4"], position=15, in_jail=False, jail_turns=0, money=1800)
        players=[p1,p2,p3,p4]
        leaderboard(players)
        return mainmenu()
    elif choice == "4":
        print("Exiting... Goodbye!")
        exit()
    else:
        print("Oops! Please enter a valid number (1-4).\n")
        return mainmenu()


def signupmenu():
    print("1. Signup")
    print("2. Login")
    print("3. Exit")
    choice = input("Enter your choice (1-3):")
    if choice == "1":
        username = input("Enter a username:")
        while usernameisnew(username) == False:
            print("username is already taken, please try again!")
            username = input("Enter a username:")
        email = input("Enter an email:")
        while emailisvalid(email) == False or emailisnew(email) == False:
            print("Please try again!")
            email = input("Enter an email:")
        password = input("Enter a strong password!:")
        while passisvalid(password) == False:
            print("please try again!")
            password = input("Enter a strong password!:")
        user_id = str(uuid.uuid4())
        hashed_password = bcrypt.hashpw(password.encode("utf-8"),bcrypt.gensalt()).decode("utf-8")
        user_data = {
            user_id: {
                "username": username,
                "email": email,
                "password": hashed_password
            }
        }
        try:
            with open("sign-up.json", "r") as f:
                users = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            users = {}
        users.update(user_data)
        with open("sign-up.json", "w") as f:
            json.dump(users, f, indent=4)
        return mainmenu()

    elif choice == "2":
        players = {}
        player_num = 1

        while player_num <= 4:
            print(f"\nPlayer {player_num} login")
            username = input("Enter your username: ")
            password = input("Enter your password: ")

            if check_login(username, password):
                if username in players.values():
                    print("This user already logged in as a player! Try another account.")
                    continue
                players[player_num] = username
                print(f"Player {player_num} logged in successfully")
                player_num += 1
            else:
                print("Invalid username or password")
                print("1. Try again")
                print("2. Exit to signup menu")
                choice2 = input("Enter your choice (1-2): ")
                if choice2 == "2":
                    return mainmenu()

        with open("current-game.json", "w") as f:
            json.dump(players, f, indent=4)
        print('i shall go to newgame')
        return newgame()
    elif choice == "3":
        return mainmenu()
    else:
        print ("Oops! Please enter a valid number (1-3).\n")
        return signupmenu()
def emailisvalid(email):
    email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if re.match(email_pattern, email):
        return True
    else:
        return False
def passisvalid(password):
    if len(password) > 8:
        return True
    else:
        return False
def usernameisnew(username):
    try:
        with open("sign-up.json", "r") as f:
            users = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        users = {}
    for u in users.values():
        if u.get("username") == username:
            return False
    return True
def emailisnew(email):
    try:
        with open("sign-up.json", "r") as f:
            users = json.load(f)
    except (FileNotFoundError,json.JSONDecodeError):
        users = {}
    for u in users.values():
        if u.get("email") == email:
            return False
    return True
def check_login(username,password):
    try:
        with open("sign-up.json", "r") as f:
            users = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return False
    for u in users.values():
        if u.get("username") == username:
            return bcrypt.checkpw(password.encode("utf-8"), u["password"].encode("utf-8"))
    return False
def newgame():
    print('im here')
    return 'new'
def loadgame():
    return 'load'

def leaderboard2():
    def informations(id,username,position=0,in_jail=False,jail_turns=0,money=1500,properties=None):
        if properties is None:
            properties = []
        return{
            "id": id,
            "username": username,
            "position": position,
            "in_jail": in_jail,
            "jail_turns": jail_turns,
            "money": money,
            "properties": properties
        }

    def leaderboard1(players):
        print("\n                        ====== Leaderboard ======   ")
        print(f"{'id |':<3} {'username |':<10} {'position |':<4} {'jail_situation |':<8} {'jail_turns |':<10} {'money  |':<8} {'Properties'}")
        print("-"*70)
        for informarion in players:
            jail_situation = "in jail" if informarion["in_jail"] else "free"
            all_properties = ", ".join(informarion["properties"]) if informarion["properties"] else "-"
            print(f"{informarion['id']:<4} {informarion['username']:<10} {informarion['position']:<10} {jail_situation:<16} {informarion['jail_turns']:<12} {informarion['money']:<8} {all_properties}")

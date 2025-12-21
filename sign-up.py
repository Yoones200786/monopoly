import re
import uuid
import bcrypt
import json
def mainmenu():
    print ("\033[1;32mWelcome to Monopoly!\033[0m\n")
    print ("1. New Game")
    print ("2. Load Game")
    print ("3. Leaderboard")
    print ("4. Exit")
    choice = input ("Enter your choice (1-4):")
    if choice =="1":
        signupmenu()
    elif choice =="2":
        loadgame()
    elif choice =="3":
        leaderboard()
    elif choice =="4":
        print ("Exiting... Goodbye!")
        exit()
    else:
        print ("Oops! Please enter a valid number (1-4).\n")
        mainmenu()
def signupmenu():
    print ("1. Signup")
    print ("2. Login")
    print ("3. Exit")
    choice = input ("Enter your choice (1-4):")
    if choice == "1":
        username = input("Enter a username:")
        while usenameisnew(username) == False:
            print ("username is already taken, please try again!")
            username = input("Enter a username:")
        email = input("Enter an email:")
        while emailisvalid(email) == False or emailisnew(email)== False:
            print ("Please try again!")
            email = input("Enter an email:")
        password = input("Enter a strong password!:")
        while passisvalid(password) == False:
            print ("please try again!")
            password  = input("Enter a strong password!:")
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
        with open ("sign-up.json", "w") as f:
            json.dump(users, f, indent=4)
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
def usenameisnew(username):
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
def loadgame():
    print ("The Functuion is not ready yet!")
def leaderboard():
    print ("The Functuion is not ready yet!")
mainmenu()




   



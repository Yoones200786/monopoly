import re
import uuid
import 
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
def emailisvalid(x):











def loadgame():
    print ("The Functuion is not ready yet!")
def leaderboard():
    print ("The Functuion is not ready yet!")
mainmenu()



   



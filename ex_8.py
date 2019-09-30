"""Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player plays (using input), compare them, print out a message of congratulations to the winner, and ask if the players want to start a new game)

Remember the rules:

Rock beats scissors
Scissors beats paper
Paper beats rock
EXTRA BY ME: OPPONENT RANDOM CHOICE
"""

import random
import sys

player1 = input("Make your choice Rock/Paper/Scissors: ")
choices = ["Rock", "Paper", "Scissors"]
player2 = choices[random.randint(0,2)]

while player1 != "exit":
    player2 = choices[random.randint(0,2)]
    if player1 == player2:
        print("IA:"+player2+" - Tie")
        player1 = input("Better than lose. Make your choice again Rock/Paper/Scissors: ")
    elif player1 == choices[0] and player2 == choices[1]:
        print("IA:"+player2+" - IA Win")
        player1 = input("Bad luck. Make your choice again Rock/Paper/Scissors: ")
    elif player1 == choices[0] and player2 == choices[2]:
        print("IA:"+player2+" - Player Win")
        player1 = input("Great!. Make your choice again Rock/Paper/Scissors: ")
    elif player1 == choices[1] and player2 == choices[0]:
        print("IA:"+player2+" - Player Win")
        player1 = input("Great!. Make your choice again Rock/Paper/Scissors: ")
    elif player1 == choices[1] and player2 == choices[2]:
        print("IA:"+player2+" - IA Win")
        player1 = input("Bad luck. Make your choice again Rock/Paper/Scissors: ")
    elif player1 == choices[2] and player2 == choices[0]:
        print("IA:"+player2+" - IA Win")
        player1 = input("Bad luck. Make your choice again Rock/Paper/Scissors: ")
    elif player1 == choices[2] and player2 == choices[1]:
        print("IA:"+player2+" - Player Win")
        player1 = input("Great!. Make your choice again Rock/Paper/Scissors: ")
    elif player1 == "exit":
        print("Game ended")
        sys.exit()
    else:
        player1 = input("Only Rock/Paper/Scissors: ")

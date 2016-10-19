import sys
import random


player1 = input("Player what is your name? ").upper()
player1_answer = input("do you want to choose rock, paper or scissors? " + player1 + " ").lower()


def robo():
    rps = random.randint(1,3) 

    if rps is 1:
        return("rock")
    elif rps is 2:
        return("scissors")
    elif rps is 3:
        return("paper")
    
roboans = robo()
def compare(ply1, roboans):
    

    if ply1 == roboans:
        return("It's a tie!")
    
    elif ply1 == 'rock':
        if roboans == 'scissors':
            return ("You chose Rock, Rock wins!")
        else:
            return("Robot chose Paper, Paper wins!")
        
    elif ply1 == 'scissors':
        if roboans == 'paper':
            return("You chose Scissors, Scissors win!")
        else:
            return("Robot chose rocks, Rocks wins!")
    elif ply1 == "paper":
        if roboans == "rock":
            return ("You chose paper. paper wins!")
        else:
            return("robot chose Scissors. Scissors win!")
    else:
        return("Invalid input! You did not enter one of the choices, please try again!.")
        sys.exit()

print(compare(player1_answer, roboans))







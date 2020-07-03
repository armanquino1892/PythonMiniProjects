import random
import os
from time import sleep

keepPlaying = True
gameCount = 0
winCount = 0



def R():
    return "ROCK"

def P():
    return "PAPER"

def S():
    return "SCISSOR"

switcher = {
    "R": R,
    "P": P,
    "S": S
}

def get_action(action):
    # Get function from switcher dictionary
    func = switcher.get(action, "nothing")
    # Execute function
    return func()

def screen_clear():
       # for mac and linux(here, os.name is 'posix')
   if os.name == 'posix':
      _ = os.system('clear')
   else:
      # for windows platfrom
      _ = os.system('cls')



while keepPlaying:
    gameCount += 1

    screen_clear()

    print ("Let's Play!")

    # Player Choice
    playerChoice = input("\nRock[R], Paper[P] or Scissors[S]?").upper()
    action = get_action(playerChoice)
    
    # Computer Choice
    computerChoice = random.choice(["ROCK", "PAPER", "SCISSOR"])
    print ("Your choice is " + action)
    print ("Computer choice is " + computerChoice)

    # Compare Player and Computer Action
    if action == computerChoice:
        print("Tie!")
    else:
        playerWin = False
        if action == get_action("R") and computerChoice == get_action("S"):
            playerWin = True
        elif action == get_action("S") and computerChoice == get_action("P"):
            playerWin = True
        elif action == get_action("P") and computerChoice == get_action("R"):
            playerWin = True

        # Game Result
        if playerWin:
            print("You won!")
            winCount += 1
        else:
            print("Computer won!")

    # Continue Game
    while True:
        finishGame = input("Do you want to keep playing? Yes[Y] or No[N]?: ").upper()
        if finishGame == "Y":
            
            keepPlaying
            
        elif finishGame == "N":
            keepPlaying = False
            print ("\nNumbers of played games: " +  str(gameCount))
            print ("You won " + str(winCount) + " times!")
            print ("Thank you for playing!")
        else:
            print ("Please enter Yes[Y] or No[N]")
            continue
        break
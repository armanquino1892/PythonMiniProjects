import random
import time
import sys
import os

def spinning_cursor():
    while True:
        for cursor in '|/-\\':
            yield cursor

def screen_clear():
       # for mac and linux(here, os.name is 'posix')
   if os.name == 'posix':
      _ = os.system('clear')
   else:
      # for windows platfrom
      _ = os.system('cls')

# dice number range from 0-6
def executeRoll():
    spinner = spinning_cursor()
    dice_number = random.randrange(1, 6)
    for _ in range(20):
            sys.stdout.write(next(spinner))
            sys.stdout.flush()
            time.sleep(0.1)
            sys.stdout.write('\b')
    return dice_number

keepRolling = True

while keepRolling:
    screen_clear()
    print ("----Dice Roll Simulator----\n")
    roll = input("Start rolling? Yes[Y] or No[N]: ").upper()

    if roll == "Y":

        result = executeRoll()
        print("Result: ", result)
        reroll = input("Roll Again? Yes[Y] or No[N]: ").upper()

        if reroll == "Y":
            keepRolling
            continue
        else:
            keepRolling = False
        break
    else:
        break


    

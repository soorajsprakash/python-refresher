# --------------------------------------------------------------
# ---------------------- GUESS THE NUMBER ----------------------
# --------------------------- (Scope)---------------------------
# --------------------------------------------------------------

from _12_guessNum_art import logo
import random

print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

randomNum = random.randint(1, 100)
gameMode = input("Choose a difficulty. Type 'easy' or 'hard': ")
if gameMode == "hard":
    choices = 5
    print("You have 5 attempts remaining to guess the number.")
else:
    choices = 10
    print("You have 10 attempts remaining to guess the number.")

while choices > 0:
    userGuess = int(input("Make a guess: "))
    if userGuess == randomNum:
        print(f"You got it. The answer was {randomNum}")
        break
    elif userGuess > randomNum:
        print("Too high.")
    else:
        print("Too low.")
    
    choices -= 1
    print(f"You have {choices} attempts remaining to guess the number.")


if choices == 0:
    print(f"You Lose. The answer was {randomNum}")
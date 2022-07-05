# --------------------------------------------------------------
# ------------------ ROCK, PAPER, SCISSORS ---------------------
# ----------------- (RANDOMISATION & LISTS) --------------------
# --------------------------------------------------------------

import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

gameImages = [rock, paper, scissors]
playerChoice = int(input("What do you choose? Type 0 for ROCK, 1 for PAPER, 2 for SCISSORS.\n"))
if playerChoice < 0 or playerChoice > 2:
    print("INVALID NUMBER,YOU LOOSE!!")
else:
    print(gameImages[playerChoice])
    compChoice = random.randint(0, 2)
    print(f"Computer Chose: {gameImages[compChoice]}")

    if playerChoice == 0 and compChoice == 2:
        print("You Wins!")
    elif playerChoice == 2 and compChoice == 0:
        print("You Lose!")
    elif compChoice > playerChoice:
        print("Computer Wins!")
    elif playerChoice > compChoice:
        print("You Wins!")
    elif playerChoice == compChoice:
        print("DRAW!!")

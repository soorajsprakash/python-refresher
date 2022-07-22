# WILL NEED A REWORK
# --------------------------------------------------------------
# ------------------------- HIGHER-LOWER -----------------------
# --------------------------------------------------------------


from _13_art import logo, vs
from _13_gameData import data
import random
import os

print(logo)

score = 0
amiWinningSon = True
def clear():
    os.system('clear')

aTitle = 'A'
randomQintA = random.choice(range(49))

A = f"Compare {aTitle}: {data[randomQintA]['name']}, a {data[randomQintA]['description']}, from {data[randomQintA]['country']}"

def bFunc(title):
    B = f"Against {title}: {data[randomQintB]['name']}, a {data[randomQintB]['description']}, from {data[randomQintB]['country']}"
    print(B)

while amiWinningSon:
    print(A)
    randomQintB = random.choice(range(49))

    print(vs)

    bFunc('B')

    print("-----------------------------------")
    print(data[randomQintA]['follower_count'])
    print("-----------------------------------")
    print(data[randomQintB]['follower_count'])
    print("-----------------------------------")

    ans = input("Who has more followers? Type 'A' or 'B': ").upper()

    if ans == 'A' and data[randomQintA]['follower_count'] > data[randomQintB]['follower_count'] :
        score += 1
        # clear()
        print(f"You're right. Current score: {score}")
        A = bFunc('A')
        
    elif ans == 'B' and data[randomQintB]['follower_count'] > data[randomQintA]['follower_count'] :
        score += 1
        # clear()
        print(f"You're right. Current score: {score}")
        A = bFunc('A')
        
        
    # elif aFollower == bFollower:
    elif data[randomQintA]['follower_count'] == data[randomQintB]['follower_count']:
        # clear()
        print(f"Draw. Move on.!. Current score: {score}")
        A = bFunc('A')

    else:
        print(f"Sorry that's wrong. Final Score: {score}")
        break


# while True:
    # randomQintA = random.choice(data)
    # randomQintB = random.choice(data)
    # print(f"Compare A: {randomQintA['name']}, a {randomQintA['description']}, from {randomQintA['country']}")
    # print(vs)
    # print(f"Compare B: {randomQintB['name']}, a {randomQintB['description']}, from {randomQintB['country']}")

# def genRandomQ(player):
#     # player = 'A' or 'B'
#     randomQintA = random.choice(data)
#     print()

# print(f"Compare {playList[0]}: {data[randomQintA]['name']}, a {data[randomQintA]['description']}, from {data[randomQintA]['country']}")
# print(f"Compare {playList[1]}: {data[randomQintB]['name']}, a {data[randomQintB]['description']}, from {data[randomQintB]['country']}")

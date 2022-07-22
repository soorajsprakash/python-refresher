# --------------------------------------------------------------
# --------------------- BLACKJACK PROJECT ----------------------
# --------------------------------------------------------------

from blackjack_art import logo
import random


print(logo)
blackjack = 21
ace = 11
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
userCards = []
pcCards = []

# 1. deal function
def dealCard(forWhom):
	forWhom.append(random.choice(cards))

# initial deal
dealCard(userCards)
dealCard(userCards)
dealCard(pcCards)

def printAllDeck():
	print(f"User cards: {userCards}")
	print(f"Computer cards: {pcCards}")

# 3. what's next?
def nextHuh():
	nextRound = input("Press 'y' to get another card, or 'n' to stop: ")
	if nextRound == 'y':
		# print("You chose to continue taking new cards")
		dealCard(userCards)
		brain()
	elif nextRound == 'n':
		# print('Round ended')
		while sum(pcCards) < 17:
			dealCard(pcCards)
		printAllDeck()
		if sum(pcCards) > 21:
			print("You Win")
		else:
			if sum(pcCards) > sum(userCards):
				print("You Lose")
			elif sum(userCards) > sum(pcCards):
				print("You Win")
			if sum(pcCards) == sum(userCards):
				print("DRAW")

# 2. to check for blackjacks
def brain():
	printAllDeck()
	if sum(pcCards) == blackjack:
		print("You Lose")
	elif sum(userCards) == blackjack:
		print("You win")
	else:
		# print('NO BLACKJACKS')
		if sum(userCards) > blackjack:
			if ace not in userCards:
				print('You Lose')
			else:
				printAllDeck()
				userCards.remove(ace)
				userCards.append(1)
				if sum(userCards) > blackjack:
					print("You Lose")
				else:
					nextHuh()
		else:
			nextHuh()

brain()

# ---------------- RULES ----------------

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

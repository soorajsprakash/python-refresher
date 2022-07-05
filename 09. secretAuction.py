# --------------------------------------------------------------
# ---------------------- SECRET AUCTION ------------------------
# -------- (Dictionaries, Nesting & the Secret Auction) --------
# --------------------------------------------------------------

from _09_secretAuctionArt import logo
import os

# to clear interpreter
def clear():
    os.system('clear')

print(logo)
print('Welcome to the secret auction program.')

bidDict = {}
isBidding = True
while isBidding:
    name = input('What is your name?: ')
    bid = int(input('What\s your bid?: $'))
    bidDict[name] = bid
    otherBidders = input('Are there any other bidders? Type "yes" or "no".\n')
    clear()
    if otherBidders == 'no':
        print('No bidders left')
        isBidding = False
print(bidDict)

highestBid = 0
highestBidder = ""
for bidder in bidDict:
    bidAmt = bidDict[bidder]
    if bidAmt > highestBid:
        highestBid = bidAmt
        highestBidder = bidder

print(f"The winner is {highestBidder}, with a bid of ${highestBid}")
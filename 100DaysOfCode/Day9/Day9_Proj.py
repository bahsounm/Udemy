# The Secret Auction Program Instructions
import os
print("Welcome to the secret auction program.")

bidders = {}

while True:
    name = input("What is your name?: ")
    bid = int(input("What's your bid?: "))
    bidders[name] = bid
    other_bidders = input("Are there any other bidders? Type 'yes' or 'no'.")
    if other_bidders == "yes":
        os.system('cls')
    else:
        os.system('cls')
        break

max_bidder = max(bidders, key=bidders.get)
max_bid = bidders[max_bidder]

print(f"The winner is {max_bidder} with a bid of ${max_bid}")




from replit import clear
from art import logo
#HINT: You can call clear() to clear the output in the console.

print(logo)
print("Welcome to the secret auction program.")
bidding_end = False 
current_bids = []
while not bidding_end:
    name = input("What is your name?:")
    bid_value = input("What's your bid?: $")
    bid = {}
    bid["name"] = name
    bid["bid_value"] = int(bid_value)
    current_bids.append(bid)
    further_bids = input("Are there any other bidders? Type 'yes' or 'no'.").lower()
    if further_bids == "no":
        bidding_end = True
    else:
        clear()

final_bid_value = 0
winner = ""
for bid in current_bids:
    if bid["bid_value"] > final_bid_value:
        final_bid_value = bid["bid_value"]
        winner = bid["name"]

print(f"The winner is {winner} with bid value ${final_bid_value}")
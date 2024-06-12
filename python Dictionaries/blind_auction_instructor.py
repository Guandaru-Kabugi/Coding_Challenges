import os
from art import logo

print(logo)
print("Welcome to the bid auction")

bid_dictionary = {}
#bid_dictionary = {}

#print (bid_dictionary)

continue_asking = True

def highest_bidder (bidding_record):
    maximum_bid = 0
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > maximum_bid:
            maximum_bid = bid_amount
            winner = bidder
    print (f"The winner is {winner} and their bid was {maximum_bid}")

while continue_asking:
    name = input("What is your name?\n")
    bid = int(input("What is your bid($)?\n"))
    bid_dictionary [name] = bid
    question = input("Do you have any other bidder? yes or no\n")
    
    if question == 'no'.lower():
        continue_asking= False
        print(bid_dictionary)
        highest_bidder(bidding_record=bid_dictionary)
    elif question == 'yes':
        os.system('cls')


#Key_1 = next(iter(bid_dictionary))

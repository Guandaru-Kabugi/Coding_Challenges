import os
from art import logo

print(logo)
print("Welcome to the bid auction")

bid_dictionary = {}
#bid_dictionary = {}

#print (bid_dictionary)

continue_asking = True
while continue_asking:
    name = input("What is your name?\n")
    bid = int(input("What is your bid($)?\n"))
    bid_dictionary [name] = bid
    question = input("Do you have any other bidder? yes or no\n")
    if question == 'no'.lower():
        continue_asking= False
    elif question == 'yes':
        os.system('cls')
print(bid_dictionary)
Key_1 = next(iter(bid_dictionary))
maximum_bid = bid_dictionary[Key_1]
for name in bid_dictionary:
    bid = bid_dictionary[name]
    if bid > maximum_bid:
        maximum_bid = bid
        winner = name
print (f"The winner is {name} and Their bid was ${maximum_bid}")
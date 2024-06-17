import os

print("Welcome to the bid auction")
name = input("What is your name?\n")
bid = int(input("What is your bid?\n"))
#print(type(bid))

bid_dictionary = {}
bid_dictionary [name] = bid
#bid_dictionary ["Bid"] = bid
print (bid_dictionary)
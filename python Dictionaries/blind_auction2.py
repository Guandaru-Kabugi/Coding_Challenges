import os

print("Welcome to the bid auction")

bid_dictionary = {}
#bid_dictionary = {}

#print (bid_dictionary)

continue_asking = True
while continue_asking:
    name = input("What is your name?\n")
    bid = int(input("What is your bid?\n"))
    bid_dictionary [name] = bid
    question = input("Do you have any other bidder? yes or no\n")
    if question == 'yes'.lower():
        continue_asking = True
    elif question == 'no'.lower():
        continue_asking= False
print(bid_dictionary)
 
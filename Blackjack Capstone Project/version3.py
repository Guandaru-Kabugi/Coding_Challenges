import random
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
playing = input("Do you want to play a game of blackjack? Type 'y' for yes and 'n' for no\n")
My_cards = []
computer_card = []
results = 0
results_comp = 0
if playing == 'y':
    for number in range (2):
        random_card = random.choice(cards)
        My_cards.append(random_card)
    for card in My_cards:
        results+=card
    print(f"Your cards are {My_cards}, current score: {results}")
    for number in range (2):
        random_comp_cards = random.choice(cards)
        computer_card.append(random_card)
    for card in computer_card:
        results_comp+= card
    # print(computer_card)
    print(f"Computer first hand: {computer_card[0]}")
    print (f"Computer second hand: {computer_card[1]}")
    print(results_comp)
continue_playing = True
while continue_playing:
    Another_card = input("Type 'y' to get another card, type 'n' to pass:\n")
    if playing == 'y':
        random_card = random.choice(cards)
        My_cards.append(random_card)
        print(My_cards)
        results+=random_card
        print(results)
        random_comp_cards = random.choice(cards)
        computer_card.append(random_comp_cards)
        results_comp+=random_comp_cards
        print(computer_card)
        print(results_comp)
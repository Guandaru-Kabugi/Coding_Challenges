import random
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
playing = input("Do you want to play a game of blackjack? Type 'y' for yes and 'n' for no\n")
My_cards = []
computer_card = []
if playing == 'y':
    for number in range (2):
        random_card = random.choice(cards)
        My_cards.append(random_card)
    results = My_cards[0] + My_cards[1]
    print(f"Your cards are {My_cards}, current score: {results}")
    for number in range (2):
        random_comp_cards = random.choice(cards)
        computer_card.append(random_card)
    results_comp = computer_card[0] + computer_card[1]
    print(f"Computer first hand: {computer_card[0]}")
    # print(f"Computer second hand: {computer_card[1]}")
    print(results_comp)
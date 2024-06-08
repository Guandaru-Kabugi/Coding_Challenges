#Step 3

import random
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)

#Testing code
#print(f'Pssst, the solution is {chosen_word}.')

#Create blanks
Display = []
for letter in chosen_word:
    Display.append("_")
print(Display)
#end_game = True
#chosen_word_list = list(chosen_word)
#print(chosen_word_list)
end_game = False
while not end_game:
    Guessed_Letter = input("What letter do you guess belongs in the word?\n").lower()
    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter== Guessed_Letter:
            Display[position]= letter
    print(Display)
    if not "_" in Display:
        end_game = True
        print("You have won")
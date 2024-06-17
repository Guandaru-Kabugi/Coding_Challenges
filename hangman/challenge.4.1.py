import random
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
lives = 6
#Testing code
print(f'Pssst, the solution is {chosen_word}.')

#Create blanks
Display = []
for letter in chosen_word:
    Display.append("_")
chosen_word_list = list(chosen_word)
while not Display== chosen_word_list or lives != 0:
    Guessed_Letter = input("What letter do you guess belongs in the word?\n").lower()
    for position in range(len(chosen_word_list)):
        letter = chosen_word_list[position]
        if letter== Guessed_Letter:
            Display[position]= letter
    if not Guessed_Letter in chosen_word_list:
        lives-=1
        print(lives)
        #print(stages[lives])
        if lives == 0:
            print("you lose")
            print(stages[lives])
            exit()
    print(Display)
    if Display == chosen_word_list:
        print("You have won")
        exit()
    print(stages[lives])

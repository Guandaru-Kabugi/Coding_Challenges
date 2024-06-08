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
end_game = False
while not end_game:
    Guessed_Letter = input("What letter do you guess belongs in the word?\n").lower()
    for position in range(len(chosen_word_list)):
        letter = chosen_word_list[position]
        if letter== Guessed_Letter:
            Display[position]= letter
    if Guessed_Letter not in chosen_word_list:
        lives-=1
        print(lives)
        if lives == 0:
            end_game = True
            print("You Lose!")
    print(Display)
    if "_" not in Display:
        end_game = True
        print("You Win")
        print(f"{''.join(Display)}")
    print(stages[lives])
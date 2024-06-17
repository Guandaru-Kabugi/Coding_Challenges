line1 = ["⬜️","️⬜️","️⬜️"]
line2 = ["⬜️","⬜️","️⬜️"]
line3 = ["⬜️️","⬜️️","⬜️️"]
map = [line1, line2, line3]
print("Hiding your treasure! X marks the spot.")
position = input("Where do you want to put the treasure?") 
# 🚨 Don't change the code above 👆
# Write your code below this row 👇
Letter = position[0].lower()
abc = ['a', 'b', 'c'] #created this abc to hold the letters that are also in the map
letter_index = abc.index(Letter) # here we want to identify the position of the letter inside abc
number_index = int(position[1])-1 # here we are checking position of number index but also subtracting 1 because we will use it in the map
map [number_index][letter_index] = 'X'
# DO NOT CONFUSE SQUARE BRACKETS FOR INDEX ON LIST AND NORMAL PARENTHESIS 👆
# 🚨 CREATE A HOLDER LIKE ABC TO HELP COLLECT INFORMATION AND IDENTIFY SPECIFIC INDEX 
print(f"{line1}\n{line2}\n{line3}")
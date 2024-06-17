import random
names = ["Angela", "Ben", "Jenny", "Michael", "Chloe"]


names_index = len(names)
random_index_name = random.randint(0, names_index-1)
print (f"{names[random_index_name]} is going to buy the meal today!")
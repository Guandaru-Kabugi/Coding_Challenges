import random
names = ["Angela", "Ben", "Jenny", "Michael", "Chloe"]


name = len(names)
random_index_name = random.randint(0, name-1)
print (f"{names[random_index_name]} is going to buy the meal today!")
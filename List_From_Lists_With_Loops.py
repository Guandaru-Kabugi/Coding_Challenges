Item_A = [20.2, 22.2, 24.2, 26.2, 28.2, 30.2, 32.2, 34.2, 36.2]
Item_B = []
for i in range(len(Item_A)): #len(Item_A) = 9; notes index within the 9 items
    Item_B.append(Item_A[i] * 2)#adds the value of the item in a specific index to the end of the list
print("New List is: " +str(Item_B)) #ensure print is not in the loop

#print(Item_B)
#print("New List is: " +str(Item_B))
print("Old list is: ")
print(Item_A)
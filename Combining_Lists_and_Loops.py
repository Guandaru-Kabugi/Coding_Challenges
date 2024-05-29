temperatures = [22.2,23.3,24.4,25.5,26.6,27.7,28.8]
print(len(temperatures))
for i in range(len(temperatures)):
    #we have to call upon the temeprature list using the index of the list to ensure that there is looping
  print("The temperature is " + str(temperatures[i])+ " degrees")
#for temperature in temperatures:
#  print ("The temperature is " +str(temperature) + " degrees")
#for i, temperature in enumerate(temperatures):
 # print(str(i), str(temperature))
#we use enumerate to get the index and the value at the same time
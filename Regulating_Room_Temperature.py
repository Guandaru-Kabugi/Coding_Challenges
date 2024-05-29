import time

room_temperature = float(input("What is the room temperature? "))
#remember to include semi-colons after ifs
#remember that data type like int and float comes before input
#remember to indent your work!
if(room_temperature < 20.0):
    print("Turn on the heater!")
    time.sleep(1.5)
elif((room_temperature >= 20.0) and (room_temperature <= 25.0)):
    print("ok!")
    time.sleep(1.5)
else:
    print("Turn on the cooler!")
    time.sleep(1.5)
print("End of Program!")
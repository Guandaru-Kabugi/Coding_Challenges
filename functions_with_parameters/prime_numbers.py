# Write your code below this line 👇
def prime_checker(number):
    prime_number = True
    for no in range (2, number):
        if number % no == 0:
            prime_number = False
    if prime_number:
        print (f"{number} is a prime number")
    else:
        print(f"{number} is not a prime number")
            

# Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input("Check this number")) # Check this number
prime_checker(number=n)
#print(f"{prime_checker(number=n)} is a prime number")
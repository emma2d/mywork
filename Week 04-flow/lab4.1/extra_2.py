#is_even.py is a program that asks the user to enter in a number
# the program will tell the user if the number is even or odd
#Author: Emma Dunleavy


number = int(input("Enter a integer:"))

while(number != -1): #while the inputted number does not = -1
    print("Please enter -1") # 
    number = int(input("Enter a integer:")) # instruction to enter an integer
    print("Thank you") # once -1 entered print Thank you

# % is used to get the remainder 

#if inputted number is even and divided by 2 eg 40 / 2 = 20, no remmainder therefore even number
# or 41 / 2 = 20 remainder 1 therfore odd number

if (number % 2) == 0:
    print(f"{number} is an even number")
else:
    print(f"{number} is an odd number")
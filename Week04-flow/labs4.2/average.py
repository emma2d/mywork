# average.py is a program that keeps reading numbers until the user enters a 0
# the program will append each of them into a list
# the program will then print out each of the numbers entered and the average of them

#Author: Emma Dunleavy

numbers = [] # creates numbers as a list
number=int(input("enter a number, (0 to quit):")) # defines number as an integer to be inputted by the user
while number !=0:
    numbers.append(number)
    number=int(input("enter a number, (0 to quit):")) # while the number inputted is any number other than 0 the number will be added to the list
for value in numbers:
    print(value) #print the value in the list numbers

average=float(sum(numbers)) / len(numbers) #define average as the sum of the numbers in the list "numbers" divided by the number of enteries in the list "numbers"

print(f"The average is {average}") #print out the avergae of the numbers inputted
#lab 3.1 part 3
# program that reads in two numbers and divides the first one by the second and give the integer result and the remainder
#Author: Emma Dunleavy

#reading in first number as an int
x = int(input('Enter first number:'))
#reading in divsor as an int
y = int(input('Enter the number you want to divid by:'))

#code for answer 
answer=int(x/y)

#code for remainder
remainder=x%y
#printing "a divided by b is c remainder d"
print('{} divided by {} is {} remainder {}' .format(x,y,answer, remainder))
# Lab 3.2 part 1
# program called round.py. The program should take in a float and output an int (rounded up or down)
#Author Emma Dunleavy

#reading in a float number and coding it as float_number
float_number = float(input('Enter a float number:'))

#rounding the float number using round()
rounded_number = round(float_number)

#printing 'x rounded is y'
print('{} rounded is {}'.format(float_number, rounded_number))

# lab3.2 part 3
# program that takes in a float and outputs an int rounded down
# author: Emma Dunleavy

import math

#reading in a float number and coding it as float_number
float_number=float(input('Enter a float number:'))

#using imported math.floor to round down the imputted float number
rounded_number=math.floor(float_number)

#printing 'x  number floored in y'
print('{} floored is {}'.format(float_number, rounded_number))

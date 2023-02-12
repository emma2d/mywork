#Lab3.1 part 6
#program that prints out random fruits using tuple
#Author: Emma Dunleavy

import random

#creating list of fruits using round bracket for tuple
fruits = ('Apple', 'Orange', 'Banana', 'Pear')

index = random.randint(0,len(fruits)-1)

fruit=fruits[index]

#printing a random fruit
print('a random fruit:{}'.format(fruit))
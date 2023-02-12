#Lab3.1 part 5
#program that prints out random fruits using lists
#Author: Emma Dunleavy

#importing random
import random
#creating list of fruits using sq brackets for list
fruits = ['Apple', 'Orange', 'Banana', 'Pear']

# to get random fruit between 0 and lenght -1
index = random.randint(0,len(fruits)-1)


fruit=fruits[index]
print('a random fruit:{}'.format(fruit))

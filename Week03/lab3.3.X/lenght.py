#lab3.3 part 1
# Write a program (length.py) that reads in a string and outputs how long it is
#Author Emma Dunleavy

#reading in a string
string=input('Please enter a string:')

#counting the number of characters in the string
number_of_characters=(len(string))

#printing The length of xxx is y characters in two different ways
print('The length of {} is {} characters'.format(string, number_of_characters))
print(f'The lenght of {string} is {number_of_characters} characters')
#lab3.3 part 3
#program that reads in a string 
#and strips any leading or trailing spaces,
# the program converts the string to lower case
#author: Emma Dunleavy

#reading in a string and coding it inputted_string
inputted_string=input('Please enter a string:')

#converting all characters to lower case using .lower()
normalised_string=inputted_string.lower()

#trimming the white spaces before and after the string using .strip()
normalised_striped_string=normalised_string.strip()

#printing 'That string normalised is : xxxxxxx'
print(f'That string normalised is : {normalised_striped_string}')

#determining the length of the original string before trimming
len_inputted_string=len(normalised_string )

#determing the length of the string after trimming
len_normalised_string=len(normalised_striped_string)

#printing 'we reduced the input from x to y characters'
print(f'we reduced the input from {len_inputted_string} to {len_normalised_string} characters')

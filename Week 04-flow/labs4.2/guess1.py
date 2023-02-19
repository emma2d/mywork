#  guess1.py is a program that prompts the user to guess a number
#the program will keep prompting the user to guess the number until the user gets the right one
#Author: Emma Dunleavy

num_to_guess=4 #dine the right guess number
guess=int(input("Guess the correct number between 1-10:")) # intstruction to input a guess number
while guess != num_to_guess: 
    print("Nope, sorry guess again!") 
    guess=int(input("Guess the correct number between 1-10:")) # while not inputting the corect number, ask to guess again

print("Well Done! The number was ", num_to_guess) #when correct number guessed print well done!
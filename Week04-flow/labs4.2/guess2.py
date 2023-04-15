#  guess2.py is a modified program that prompts the user to guess a number
#the program will keep prompting the user to guess the number until the user gets the right one
# the program lets the user know to go higher or lower
#Author: Emma Dunleavy

num_to_guess=30 #define the right guess number
guess=int(input("Guess the correct number:")) # intstruction to input a guess number
while guess != num_to_guess: #while the guessed number doesn't = the correct number
    if guess < num_to_guess:  # and if the guessed number is less than the correct number
        print("higher") #print "higher"
    else:
        print("lower") #otherwise print lower
    guess=int(input("Please guess again:")) #ask user to guess again
   
print("Well Done! The number was ", num_to_guess) #when correct number guessed print well done!

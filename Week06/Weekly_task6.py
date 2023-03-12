#this program takes a positive floating-point number as input and outputs an approximation of its square root
#Author: Emma Dunleavy

no=float(input("Please enter a positive number: ")) #to input a positive floating point number
approx=0.5*no                                       #creates a variable "approx" that multiplies the inputted numbner by 0.5
better=0.5*(approx+no/approx)                       #creates a variable "better" that adds the inputted number to the variable "approx", divides by "approx" and then multiplies by 0.5
while (better!=approx):                             # while the variable "better" does not = "approx"
    approx=better                                   #it is ended and gives the statements for approx and better
    better=0.5*(approx+no/approx)
print(f"The square root of {no} is appox.", better) # after the loop prints the better sq root 

# ref https://www.youtube.com/watch?v=xdlIFw5EM4w



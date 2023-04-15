#extra.py is a program that reads in a student’s percentage mark
# prints out corresponding the grade 
# the program should check that the percentage is valid:
# Under 40% => Fail
# Between 40% and 49% => Pass
# Between 50% and 59% => Merit 2
# Between 60% and 69% => Merit 1
# Over 70% => Distinction

#Author: Emma Dunleavy

#user to enter a number that can be a decimal 

percentage_mark = (float(input("Enter the percentage:")))

grade_rounded=round(percentage_mark) # rounds the float number entered 

print(grade_rounded) # prints the rounded number

if percentage_mark <0 or percentage_mark > 100:
    print("Please enter a number between 0 and 100") # instruction if number less than 0 or greater than 100 entered 

elif percentage_mark < 40: #less the 40
    print("fail")
elif percentage_mark <=49: # between 40 and 49
    print("Pass")
elif percentage_mark <=59: # between 50 and 59
    print("Merit 2")
elif percentage_mark <=69: # between 60 and 69
    print("Merit 1")
elif percentage_mark >=70: # 70 and over
    print("Distinction")
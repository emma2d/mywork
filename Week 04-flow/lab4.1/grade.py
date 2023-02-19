# grade.py is a program that reads in a student’s percentage mark
# prints out corresponding the grade 
# the program confirms that the percentage is valid:
# Under 40% => Fail
# Between 40% and 49% => Pass
# Between 50% and 59% => Merit 2
# Between 60% and 69% => Merit 1
# Over 70% => Distinction

# Author: Emma Dunleavy

#user to enter a number that can be a decimal 

percentage_mark = (float(input("Enter the percentage:")))

print(percentage_mark)  # prints the grade

if percentage_mark < 40: #less the 40
    print("fail")
elif percentage_mark <=49: # between 40 and 49
    print("Pass")
elif percentage_mark <=59: # between 50 and 59
    print("Merit 2")
elif percentage_mark <=69: # between 60 and 69
    print("Merit 1")
elif percentage_mark >=70: # 70 and over
    print("Distinction")

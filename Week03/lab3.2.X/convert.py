#lab 3.2 part 4
# a program called convert.py that takes in a float amount of dollars and returns that absolute amount in cent
#Author: Emma Dunleavy

#reading in a float number and coding it as dollar_amount
dollar_amount=float(input('Please enter an amount:'))

#converting to an absolute number ie -4 or 4 would both output 4
absolute_amount=abs(dollar_amount)

#converting dollar amount to cents
cent_amount=int(absolute_amount*100)

#printing 'That amount in cent is: x'
print('That amount in cent is: {}'.format(cent_amount))

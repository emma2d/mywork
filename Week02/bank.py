#Weekly task 02
#Author: Emma Dunleavy
amount1=int(input('Enter amount 1 (in cent):'))
amount2=int(input('Enter amount 2 (in cent):'))
print(str(amount1))
print(str(amount2))
amount1_converted=amount1/100
amount2_converted=amount2/100
print(str(amount1_converted))
print(str(amount2_converted))
print(('The sum of these is €') + str(amount1_converted + amount2_converted))
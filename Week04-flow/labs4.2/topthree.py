#topthree.py is a program that generates 10 random numbers (0-100) and prints them out then prints out the top three

#Author: Emma Dunleavy

import random

how_many = 10
top_how_many = 3
range_from = 0
range_to = 100

numbers=[]

for i in range(0,how_many):
    numbers.append(random.randint(range_from,range_to))
    print(f"{how_many} random numbers\t {numbers}")



numbers.sort(reverse = True)
print(f"The top {top_how_many} are \t\t {numbers[0:top_how_many]}")
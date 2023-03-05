#This program puts 10 random numbers into a queue(list)
#the program  then output all the values in the queue
#then takes the numbers from the queue one at a time 
#print it and the current numbers still in the queue. (the command pop(0) takes the first element out of a list)
#Author: Emma Dunleavy

import random
queue=[]
number_of_numbers =10
range_to=100

for n in range(0,number_of_numbers):
    queue.append(random.randint(0,range_to))
print(f"queue is {queue}")

while len (queue) !=0:
    current_number = queue.pop(0)
    print(f"current number is {current_number} and {queue} is:")

print("The queue is now empty")
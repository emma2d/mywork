# this program has a tuple that stores the months of the year, 
#from that tuple it will create another tuple with just the summer months (May, June, July), 
# print out the summer months one at a time
#Author Emma Dunleavy

#define months of the year in a tuple
months = ("January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December")

# define months n the tuple that are summer
summer=months[4:7]


for month in summer:
    print (month)
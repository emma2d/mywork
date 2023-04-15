#Author: Emma Dunleavy



import os.path
filename = "count.txt"
if not os.path.isfile(filename):
    print("File does not exist")
    write_number(0)

def read_number():
    try:
        with open(filename) as f:
            number = int(f.read())
            return number
    except IOError:
        return 0


import math
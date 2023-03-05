#this program reads in a student’s name
#then keeps reading in their modules and grades until name is blank

#author: Emma Dunleavy

student = input(str("name (blank to quit):"))

while (len(student) >0):
    input("module:")
    input(("grade:"))
    student = input("name (blank to quit):")

print("All Done!")
   
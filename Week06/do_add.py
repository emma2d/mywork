# program that reads in the student’s name
# Author: Emma Dunleavy

students = []
def read_modules():
    return[]
def do_add(students):
    current_student= {}
    current_student["name"]=input("enter name: ")
    current_student["modules"] = read_modules()
    students.append(current_student)

do_add(students)
print (students)
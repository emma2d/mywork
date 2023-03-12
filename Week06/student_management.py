#program that allows a user to create new students and to view students
#prints out a menu of commands we can perform, ie add, view and quit
#The function should return what the user chose
#Author: Emma Dunleavy

def display_menu():
    print("What would you like to do?")
    print("\t(a) Add new student")
    print("\t(v) View students")
    print("\t(q) Quit")
    choice = input("Type one letter (a/v/q):").strip()
    return choice
def do_add():
    print("in adding")
def do_view():
    print("in viewing)")


choice = display_menu()
while (choice != "q"):
    if choice == "a":
        do_add()
    elif choice == "v":
        do_view()
    elif choice != "q":
        print("\n\nplease select either a,v or q")

    choice=display_menu()


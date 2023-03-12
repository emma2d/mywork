#program that reads in the module names and grades 
#Author: Emma Dunleavy

def read_modules():
    modules=[]
    module_name=input("\tEnter the first Module name (blank to quit) :").strip()

    while module_name != "":
        module ={}
        module ["name"]= module_name
        module["grade"]= int(input("\tEnter grade:"))
        modules.append(module)
        module_name = input("\tEnter next module name (blank to quit):").strip()
    return modules
   
read_modules()
print (read_modules)


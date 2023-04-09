#Author: Emma Dunleavy

import numpy as np


min_salary=20000
max_salary=80000
num_of_entries = 10
np.random.seed(1) 

salaries=np.random.randint(min_salary, max_salary, num_of_entries)

print(salaries)

salaries_plus=salaries + 5000
print(salaries_plus)
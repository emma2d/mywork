#Author: Emma Dunleavy

import matplotlib.pyplot as plt
import numpy as np


mean=5
std=2
number_values=1000

values=np.random.normal(mean, std, number_values)
print(values)

plt.hist(values)
plt.show()



def h(x):
    return x**3

xpoints=np.arange(1, 11)
ypoints=h(xpoints)

plt.plot(xpoints, ypoints, color='b', label="h(x)")
plt.xlabel('Distance')
plt.ylabel('Height')
plt.title('Plotting Example')
plt.legend()
plt.show()
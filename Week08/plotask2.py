import matplotlib.pyplot as plt
import numpy as np




# a plot of the function  h(x)=x cubed in the range [0, 10] on the one set of axes

def h(x):                           #define function h(X)
    return x**3                     # return x cubed

xpoints=np.arange(0, 11)            #assign range 0-10
ypoints=h(xpoints)                  # get the cube of the range

plt.plot(xpoints, ypoints, color='b', label="h(x)")
plt.xlabel('Distance')
plt.ylabel('Height')
plt.title('Plotting Example')
plt.legend()
plt.show()
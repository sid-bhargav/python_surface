#import libraries 
from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt 

#dataset
x = np.outer(np.linspace(-3, 3, 32), np.ones(32))
y = x.copy().T #transpose the array
z = x * np.exp(-x **2 -y **2)

#creating figure 
fig = plt.figure(figsize = (14, 9))
ax = plt.axes(projection = '3d')

#creating plot
ax.plot_surface(x, y, z)

#show plot
plt.show()
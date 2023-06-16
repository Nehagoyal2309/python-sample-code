# importing the required libraries
import matplotlib.pyplot as plt
import numpy as np

# define data values
x = np.array([1, 2, 3, 4]) # X-axis points
y = x*2 # Y-axis points

plt.plot(x, y) # Plot the chart

z=y*10
plt.plot(x, z,'--') # Plot the chart
plt.xlabel("integer value")  # add X-axis label
plt.ylabel("multiply by 2")  # add Y-axis label
plt.title("line chart")  # add title
plt.fill_between(x, y, z, color='green', alpha=0.5)
plt.show()

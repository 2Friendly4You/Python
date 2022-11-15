import numpy as np

X, Y = np.loadtxt("Data_Diagram.txt", unpack=True, skiprows=1)

# plot the data
import matplotlib.pyplot as plt
# show X, Y and the line
plt.plot(X, Y, "ro")
# connect every dot with the next one
plt.plot(X, Y, "b-")
# show the plot
plt.show()
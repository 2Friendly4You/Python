import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

X, Y = np.loadtxt('data.txt', unpack=True)
plt.plot(X, Y, 'rx', label='Messwerte')
plt.xlabel(r'$\lambda$ / nm')
plt.ylabel(r'$\frac{I}{I_0}$')
plt.legend(loc='best')
plt.grid()
plt.clf()
# show data in a plot formatted as logarithmic
plt.yscale('log')
plt.xscale('log')
# plot data

"""
plt.plot(X, Y, 'rx')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Data')
plt.grid(True)
"""

# draw a curve through the data
plt.plot(X, Y, 'b-')


plt.show()

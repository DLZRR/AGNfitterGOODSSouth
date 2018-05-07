import numpy as np


array = np.loadtxt('cfh7601.dat')

for i in range(len(array)):
    array[i][0] *= 1e9

np.savetxt('cfh7601_new.dat', array)

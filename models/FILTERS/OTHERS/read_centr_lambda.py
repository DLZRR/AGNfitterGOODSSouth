import numpy as np


c=    2.997e8
Angstrom = 1e10

factors = np.loadtxt('MAMBO.dat')
#print factors
#lambdas, factors = np.loadtxt('MAMBO.dat')

central_lamb = np.sum(factors[:,0]*factors[:,1])/np.sum(factors[:,1])
central_nu = float(np.log10((Angstrom*c)/central_lamb))

print central_nu

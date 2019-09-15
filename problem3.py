import numpy as np

l = 1
m = 2
c = 2

wq1 = l/(m*(m-l))
print('Wq1:', wq1)

r = l / c / m
tmp = 0
for i in range(c):
    tmp += (c ** i) / np.math.factorial(i) * (r ** i)

wq2 = ((c**c)*(r**(c+1)))/(np.math.factorial(c)*((1-r)**2)
                           * (tmp+(c**c)/np.math.factorial(c)*(r**c)/(1-r)))
print('Wq2:', wq2)

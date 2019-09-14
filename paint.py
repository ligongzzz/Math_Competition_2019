import numpy as np
import matplotlib.pyplot as plt

k = np.linspace(0, 49)
print(k)
p = np.zeros(k.shape[0])
l = 20

for i in range(k.shape[0]):
    p[i] = l**k[i]/np.math.factorial(k[i])*np.exp(-l)

plt.plot(k, p)
plt.show()

import matplotlib.pyplot as plt
import numpy as np

x=np.arange(100)
y=x**2
z=5*x
w=x**(1/2)
plt.plot(x,y, 'r--')
plt.plot(x,z, 'g--.')
plt.plot(x,w, 'b--')
plt.plot(x, 'y-')
plt.show()

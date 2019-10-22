import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0,2*np.pi,100)
y = np.cos(x)

plt.figure()
plt.xlabel("x")
plt.ylabel("cos(x)")
plt.plot(x,y)
plt.savefig("grafica.png")
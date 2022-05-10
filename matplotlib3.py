import numpy as np
import matplotlib.pyplot as plt
x=np.arange(2,12)
y=3*x+3
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.xlim(12)
plt.ylim(40)
plt.plot(x,y,'--b')
plt.show()
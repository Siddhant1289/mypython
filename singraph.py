import numpy as np
import matplotlib.pyplot as plt
x=np.arange(0,4*np.pi,0.1)
y=np.sin(x)   #sin graph
plt.plot(x,y)
plt.show()
y=np.cos(x)   #cos graph
plt.plot(x,y)
plt.show()
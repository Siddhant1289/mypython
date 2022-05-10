import numpy as np
a=np.arange(0,60,5)
b=a.reshape(3,4)
c=np.arange(5,65,5)
d=c.reshape(3,4)
print(np.add(b,d))
print(np.subtract(b,d))
print(np.divide(b,d))
print(np.multiply(b,d))
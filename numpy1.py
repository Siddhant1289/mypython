import numpy as np
a=np.arange(2,10,1)
print(a)
x=np.arange(10)
print(x)
d=np.arange(5,51,5)
e=d.reshape((2,5))
print(e)
a=np.arange(20)
s=slice(2,18,2)
print(a[s])
b=a[2:18:2]
print(b)
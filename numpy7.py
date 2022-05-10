import numpy as np
a=np.arange(0,60,5)
b=a.reshape(3,4)
print(b)
for x in np.nditer(b):
    print(x)
print(b.T)    #TRANSPOSE OF MATRIX
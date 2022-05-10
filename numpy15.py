import numpy as np
a=np.array([[7,4,6],[2,6,3],[7,4,9]])
print(a)
print(np.argmax(a))
print(a.flatten())
print(np.argmax(a,axis=0))
print(np.argmin(a,axis=1))
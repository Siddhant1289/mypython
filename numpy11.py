import numpy as np
x=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(x)
print(np.ptp(x))   #max of all
print(np.ptp(x,axis=1))
print(np.ptp(x,axis=0))
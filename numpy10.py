import numpy as np
x=np.array([[3,5,1],[2,4,6],[7,8,0]])
print(x)
print(np.amin(x,1))   #row wise
print(np.amin(x,0))   #column wise
print(np.amax(x,0))
print(np.amax(x,1))
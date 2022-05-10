import numpy as np
x=np.array([[3,4,5,8],[2,4,1,8],[5,7,3,0]])
print(x)
print(x.shape)  #print shape of array
y=x.reshape(4,3) #change shape of array
print(y)
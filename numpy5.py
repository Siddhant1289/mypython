import numpy as np
x=np.array([[3,4,2],[4,9,6],[5,6,7],[11,33,44]])
print(x)
p=x[1:4,1:3]
print(p)
r=x[0:4,[2]]
print(r)
print(x[x>5])   #[ 9  6  6  7 11 33 44]
import numpy as np
x=np.array([[3,4,2],[4,9,6],[5,6,7],[11,33,44]])
print(x)
'''[[ 3  4  2]
    [ 4  9  6]
    [ 5  6  7]
    [11 33 44]]'''
r=np.array([[0,0],[2,2]])   #row
c=np.array([[0,2],[1,2]])   #column
y=x[r,c]
print(y)
'''[[3 2]
    [6 7]]'''
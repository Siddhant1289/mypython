import numpy as np        #ADVANCED INDEX
a=np.array([[2,5],[7,9],[2,9]])
y=a[[0,1,2],[0,1,0]]  #row,column
print(y)     #[2 9 2]
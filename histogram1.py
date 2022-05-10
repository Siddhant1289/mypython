#HISTOGRAM
import matplotlib.pyplot as plt
import numpy as np
a=np.array([3,6,9,11,16,23,27,29,30,31,34,39,40,41,42,43,44,48,49,50,66,69,73,99,100])
plt.hist(a,bins=[0,20,40,60,80,100])
plt.title('HISTOGRAM')
plt.show()
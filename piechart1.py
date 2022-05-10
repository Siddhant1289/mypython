#PIECHART
import matplotlib.pyplot as plt
states=['UP','MP','RAJ','GUJ','WB']
lit=[20,10,40,30,20]
col=['r','g','b','y','m']
plt.pie(lit,labels=states,colors=col,explode=(0.1,0.1,0.1,0.1,0.1))
plt.legend()
plt.show()
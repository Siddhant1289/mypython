#READING CSV FILE AND PLOTING GRAPH
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
emp=pd.read_csv("EmpData.csv")
empgroup=emp.groupby("EmpCode")  #Group data by EmpCode
counts=empgroup.size()           #get size for each group
cityg=np.arange(len(counts))
plt.figure("Payment Graph Bar")
plt.xticks(cityg,emp['EmpCode'])
plt.plot(cityg,emp["Payment"],color="red",linestyle="--",linewidth=1)
plt.xlabel("Emp Codes",fontsize=20,color="blue")
plt.ylabel("Payments",fontsize=20,color="blue")
plt.show()
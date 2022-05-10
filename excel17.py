#READING CSV AND CREATING HISTOGRAM
import pandas as pd
import matplotlib.pyplot as plt
emp=pd.read_csv("EmpData.csv")
plt.figure("Histogram Example 1")
plt.hist(emp["Payment"],bins=5,color='red',normed=False,alpha=0.5)
plt.show()

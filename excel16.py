#READING CSV FILE AND CREATING PIE GRAPH
import pandas as pd
import matplotlib.pyplot as plt
emp=pd.read_csv("EmpData.csv")
payment=emp["Payment"]
city=emp["City"]
plt.figure("Pie Chart Example")
colors=["lightgreen","gold","lightskyblue"]
plt.pie(payment,labels=city,colors=colors,autopct='%1.1f%%',explode=(0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1))
plt.title("Distribution of Payments")
plt.show()
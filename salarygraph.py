import pymysql
import matplotlib.pyplot as plt
import numpy as np
name=[]
salary=[]
db=pymysql.connect('localhost','root','root','factory')
cur=db.cursor()
s="select name,salary from employee"
c=0
try:
    cur.execute(s)
    res=cur.fetchall()
    for r in res:
        name.append(r[0])
        salary.append(r[1])
        c=c+1
except Exception:
    print('any issue')
x=np.arange(c)
plt.bar(x,salary,tick_label=name,width=0.4,color=['blue','red'])
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.show()
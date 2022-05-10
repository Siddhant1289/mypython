import matplotlib.pyplot as plt
import matplotlib.pyplot as plt1
x=[]
y=[]
for i in range(0,3):
    n=input('enter name')
    x.append(n)
    for j in range(0,3):
        s=0
        m=int(input('enter marks'))
        s+=m
    y.append(s)
plt1.bar(x,y)
plt.pie(y,labels=x,explode=(0.1,0.1,0.1))
plt.legend()
plt1.legend()
plt.show()
plt1.show()
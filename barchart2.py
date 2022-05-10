import matplotlib.pyplot as plt
x=[]
y=[]
for i in range(0,5):
    t=int(input("enter year"))
    x.append(t)
    u=int(input('enter population'))
    y.append(u)
plt.barh(x,y)
plt.show()
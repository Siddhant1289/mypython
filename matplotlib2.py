import matplotlib.pyplot as plt
a=[]
b=[]
c=[]
stu1=input('enter name')
for i in range(0,3):
    print('enter marks')
    y1=int(input())
    a.append(y1)
stu2=input('enter name')
for j in range(0,3):
    print('enter marks')
    y2=int(input())
    b.append(y2)
stu3=input('enter name')
for k in range(0,3):
    print('enter marks')
    y3=int(input())
    c.append(y3)
plt.plot(a,'--b')
plt.plot(b,'--r')
plt.plot(c,'--ak')
plt.legend()
plt.show()
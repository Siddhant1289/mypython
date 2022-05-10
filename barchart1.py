import matplotlib.pyplot as plt
x=[1,2,3,4,5]
y=[25,30,50,35,41]
lb=['one','two','three','four','five']
plt.bar(x,y,tick_label=lb,width=0.5,color=['blue','red'])
plt.xlabel('x-axis')
plt.ylable('y-axis')
plt.show()
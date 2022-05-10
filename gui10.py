import threading
import time
import tkinter
from tkinter import *
def inc():
	x=10
	lt=['yellow','red','green','blue','purple']
	for i in range(0,4):
		time.sleep(1)
		l.config(fg=lt[i])
	while x<=50:
		x=x+1
		time.sleep(1)
		l.config(font=('Arial',x))
def hi():
	t=threading.Thread(target=inc)
	t.start()
t=tkinter.Tk()
t.title('MINE')
t.geometry('1000x1000')
l=Label(t,text="SIDDHANT",bg='pink',fg='red')
l.place(x=190,y=100)
b=Button(t,text="SIZE",bg='pink',fg='red',command=hi)
b.place(x=200,y=200)
t.mainloop()
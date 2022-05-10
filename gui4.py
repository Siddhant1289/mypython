#event handeling
import tkinter
from tkinter import *
from tkinter import messagebox
t=tkinter.Tk()
t.title('FOURTH FRAME')
t.geometry('1000x1000')
x=IntVar()
def ch():
	a=x.get()
	if a==1:
		t.config(bg='red')
	if a==2:
		t.config(bg='yellow')
	if a==3:
		t.config(bg='green')
b1=Radiobutton(t,text='red',variable=x,value=1,command=ch)
b1.place(x=200,y=100)
b1=Radiobutton(t,text='yellow',variable=x,value=2,command=ch)
b1.place(x=200,y=150)
b1=Radiobutton(t,text='green',variable=x,value=3,command=ch)
b1.place(x=200,y=200)
t.mainloop()
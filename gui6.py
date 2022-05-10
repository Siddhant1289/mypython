import tkinter
from tkinter import *
t=tkinter.Tk()
t.title('SPIN BOX')
t.geometry('1000x1000')
def ch():
	x=b.get()
	a.config(font=('Arial',x))
a=Label(t,text='A B C',fg='green',font=50)
a.place(x=300,y=100)
b=Spinbox(t,from_=0,to=100,command=ch)
b.place(x=250,y=300)
t.mainloop()
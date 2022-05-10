import tkinter
from tkinter import *
from tkinter import messagebox
t=tkinter.Tk()
t.title('THIRT FRAME')
t.geometry('1000x1000')
def sum():
	a=int(e1.get())
	b=int(e2.get())
	c=a+b
	messagebox.showinfo('sum is ->',c)
def sub():
	a=int(e1.get())
	b=int(e2.get())
	c=a-b
	messagebox.showinfo('sub is ->',c)
def mult():
	a=int(e1.get())
	b=int(e2.get())
	c=a*b
	messagebox.showinfo('mult is ->',c)
def div():
	a=int(e1.get())
	b=int(e2.get())
	c=a/b
	messagebox.showinfo('div is ->',c)
l1=Label(t,text='ENTER 1st NO.',bg='yellow',fg='red')
l1.place(x=100,y=50)
e1=Entry(t,bd=2,width=20)
e1.place(x=200,y=50)
l2=Label(t,text='ENTER 2nd NO.',bg='yellow',fg='red')
l2.place(x=100,y=100)
e2=Entry(t,bd=2,width=20)
e2.place(x=200,y=100)
b1=Button(t,text='+',command=sum)
b1.place(x=150,y=150)
b2=Button(t,text='-',command=sub)
b2.place(x=200,y=150)
b3=Button(t,text='X',command=mult)
b3.place(x=250,y=150)
b4=Button(t,text='%',command=div)
b4.place(x=300,y=150)
t.mainloop()
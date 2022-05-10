import tkinter
from tkinter import *
t=tkinter.Tk()
def p1():
	l.config(font=('Arial',b))
t.title('A B C')
t.geometry('1000x1000')
l=Label(t,text='A B C',fg='black')
l.place(x=470,y=200)
b=Button(t,text='+',font=40,bg='pink',command=p1)
b.place(x=200,y=300)
t.mainloop()
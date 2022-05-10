import tkinter
from tkinter import *
from tkinter.colorchooser import askcolor
from tkinter import messagebox
import sys
t=tkinter.Tk()
t.title('MY NAME')
t.geometry('1000x1000')
def bk():
	r=askcolor(color='red',title='choose a color')
	t.config(bg=r[1])
def f():
	r=askcolor(color='red',title='choose a color')
	l.config(fg=r[1])
def ex():
	if (messagebox.askyesno('sure','want to exit')):
		sys.exit()
	else:
		messagebox.showinfo('Thanks')
l=Label(t,text='SIDDHANT',bg='yellow',fg='red',font=50)
l.place(x=200,y=100)
b1=Button(t,text='Background',bg='pink',command=bk)
b1.place(x=100,y=150)
b2=Button(t,text='Font color',bg='pink',command=f)
b2.place(x=300,y=150)
b3=Button(t,text='Exit',bg='pink',command=ex)
b3.place(x=230,y=200)
t.mainloop()
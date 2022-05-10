import pymysql
import tkinter
import sys
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
t=tkinter.Tk()
t.title('SQL')
t.geometry("800x600")
def ex():
	if(messagebox.askyesno('SURE','WANT TO EXIT')):
		sys.exit()
	else:
		messagebox.showinfo('THANK YOU')
def save():
	db=pymysql.connect(host="localhost",user="root",password="root",database="factory")
	cur=db.cursor()
	e=int(e0.get())
	n=e1.get()
	c=e2.get()
	sl=int(e3.get())
	s="insert into employee values(%d,'%s','%s',%d)"%(e,n,c,sl)
	try:
		cur.execute(s)
		db.commit()
		messagebox.showinfo('THANK YOU RECORD SAVED')
	except Exception as es:
		messagebox.showinfo('ANY ISSUE',es)
	db.close()
l0=Label(t,text='EMPNO',bg='yellow',fg='red',font=50)
l0.place(x=100,y=50)
e0=Entry(t,bd=2,width=20)
e0.place(x=200,y=50)
l1=Label(t,text='NAME',bg='yellow',fg='red',font=50)
l1.place(x=100,y=100)
e1=Entry(t,bd=2,width=20)
e1.place(x=200,y=100)
l2=Label(t,text='CITY',bg='yellow',fg='red',font=50)
l2.place(x=100,y=150)
e2=Entry(t,bd=2,width=20)
e2.place(x=200,y=150)
l3=Label(t,text='SALARY',bg='yellow',fg='red',font=50)
l3.place(x=100,y=200)
e3=Entry(t,bd=2,width=20)
e3.place(x=200,y=200)
b1=Button(t,text='SAVE',font=50,command=save)
b1.place(x=100,y=250)
b2=Button(t,text='EXIT',font=50,command=ex)
b2.place(x=200,y=250)
t.mainloop()
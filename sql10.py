import pymysql
import sys
import tkinter
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
t=tkinter.Tk()
t.title('SQL')
t.geometry("1000x1000")
def ex():
	if(messagebox.askyesno('SURE','WANT TO EXIT')):
		sys.exit()
	else:
		messagebox.showinfo('THANK YOU')
def find():
	db=pymysql.connect(host="localhost",user="root",password="root",database="factory")
	cur=db.cursor()
	e=int(e0.get())
	s="select name,city,salary from employee where empno=%d"%(e)
	try:
		cur.execute(s)
		res=cur.fetchone()
		e1.insert(0,res[0])
		e2.insert(0,res[1])
		e3.insert(0,res[2])
	except Exception as es:
		messagebox.showinfo("!!!!!!!!","ANY ISSUE")
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
b1=Button(t,text='FIND',font=50,command=find)
b1.place(x=100,y=250)
b1=Button(t,text='EXIT',font=50,command=ex)
b1.place(x=200,y=250)
t.mainloop()
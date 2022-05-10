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
def delete():
	db=pymysql.connect(host="localhost",user="root",password="root",database="factory")
	cur=db.cursor()
	e=int(e0.get())
	s="delete from employee where empno=%d"%(e)
	try:
		cur.execute(s)
		db.commit()
		messagebox.showinfo('THANK YOU RECORD DELETED')
	except Exception as es:
		messagebox.showinfo('ANY ISSUE',es)
	db.close()
l0=Label(t,text='EMPNO',bg='yellow',fg='red',font=50)
l0.place(x=100,y=50)
e0=Entry(t,bd=2,width=20)
e0.place(x=200,y=50)
b1=Button(t,text='DELETE',font=50,command=delete)
b1.place(x=100,y=250)
b2=Button(t,text='EXIT',font=50,command=ex)
b2.place(x=200,y=250)
t.mainloop()
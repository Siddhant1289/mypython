import pymysql
import tkinter 
from tkinter import *
from tkinter import messagebox
t=tkinter.Tk()
t.title('library management system')
t.geometry('1500x1500')
def save():
	db=pymysql.connect("localhost","root","root","factory")
	cur=db.cursor()
	a=int(rno.get())
	b=bid.get()
	c=idate.get()
	d=srd.get()
	s="insert into issue values(%d,'%s','%s','%s')"%(a,b,c,d)
	try:
		cur.execute(s)
		db.commit()
		messagebox.showinfo("record saved")
		updatestock(b)
	except Exception as e:
		print("ERROR",e)	
def updatestock(bookid):
	db=pymysql.connect("localhost","root","root","factory")
	cur=db.cursor()
	s="update books set stockin=stockin-1 where stockin>=0 and bookid='%s'"%(bookid)
	try:
		cur.execute(s)
		db.commit()
		messagebox.showinfo("stock changed")
	except Exception as e:
		print("ERROR",e)	

l=Label(t,text='BOOK ISSUE DETAILS',font=250)
l.place(x=600,y=50)
l1=Label(t,text='ROLLNO',font=100)
l1.place(x=450,y=100)
rno=Entry(t,bd=5)
rno.place(x=800,y=100)


l2=Label(t,text='BOOK ID',font=100)
l2.place(x=450,y=200)
bid=Entry(t,bd=5)
bid.place(x=800,y=200)


l3=Label(t,text='ISSUE DATE(yyyy-mm-dd)',font=100)
l3.place(x=450,y=300)
idate=Entry(t,bd=5)
idate.place(x=800,y=300)


l4=Label(t,text='SUSPECTED RETURN DATE',font=100)
l4.place(x=450,y=400)
srd=Entry(t,bd=5)
srd.place(x=800,y=400)


bt=Button(t,text='SUBMIT',command=save)
bt.place(x=600,y=650)
t.mainloop()

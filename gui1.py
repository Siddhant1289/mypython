#GUI in python
import tkinter
from tkinter import *
from tkinter import ttk
t=tkinter.Tk()
t.title('My First Frame')
t.geometry('1000x1000')
l1=Label(t,text='NAME',bg='yellow',fg='red')       #LABEL
l1.place(x=100,y=50)
e=Entry(t,bd=2,width=20)                           #ENTRY
e.place(x=200,y=50)
l2=Label(t,text='GENDER',bg='yellow',fg='red')
l2.place(x=100,y=100)
x=IntVar()
r1=Radiobutton(t,text='Male',variable=x,value=1)    #RADIOBUTTON
r1.place(x=200,y=100)
r2=Radiobutton(t,text='Female',variable=x,value=0)
r2.place(x=300,y=100)
l3=Label(t,text='HOBBIES',bg='yellow',fg='red')
l3.place(x=100,y=150)
a=IntVar()
b=IntVar()
c=IntVar()
c1=Checkbutton(t,text='Reading',variable=a,onvalue=1,offvalue=0)  #CHECKBUTTON
c1.place(x=200,y=150)
c2=Checkbutton(t,text='Writing',variable=b,onvalue=1,offvalue=0)
c2.place(x=250,y=150)
c3=Checkbutton(t,text='Sports',variable=c,onvalue=1,offvalue=0)
c3.place(x=320,y=150)
l4=Label(t,text='CITY NAME',bg='yellow',fg='red')
l4.place(x=100,y=230)
lt1=Listbox(t,width=20,height=5)                                 #LISTBOX
lt1.insert(1,'AGRA')
lt1.insert(2,'DELHI')
lt1.insert(3,'PUNJAB')
lt1.insert(4,'MUMBAI')
lt1.insert(5,'MATHURA')
lt1.place(x=200,y=200)
l5=Label(t,text='YOUR SCALE',bg='yellow',fg='red')
l5.place(x=100,y=330)
s=Scale(t,from_=0,to=100)                                     #SCALE
s.place(x=200,y=300)
l6=Label(t,text='YOUR SPIN',bg='yellow',fg='red')
l6.place(x=100,y=420)
sp=Spinbox(t,from_=0,to=100)                                   #SPIN
sp.place(x=200,y=420)
l7=Label(t,text='QUALIFICATION',bg='yellow',fg='red')
l7.place(x=100,y=450)
ltx=['PHD','UG','PG','MATRIC','INTER']
cb=ttk.Combobox(t,value=ltx)               #combobox 
cb.place(x=200,y=450)
t.mainloop()
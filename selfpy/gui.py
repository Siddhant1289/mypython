import tkinter
from tkinter import *
t=tkinter.Tk()
t.title("Canvas")
t.geometry("1000x1000")
c=Canvas(t,height=500,width=500,bg="black")
c.place(x=10,y=10)
c.create_line(250,0,250,500,fill='blue') 
c.create_line(0,250,500,250,fill='blue')
c.create_line(250,0,200,250,fill='blue')
c.create_line(250,0,300,250,fill='blue')
c.create_line(250,50,150,250,fill='blue')
c.create_line(250,50,350,250,fill='blue')
c.create_line(250,100,100,250,fill='blue')
c.create_line(250,100,400,250,fill='blue')
c.create_line(250,150,50,250,fill='blue')
c.create_line(250,150,450,250,fill='blue')
c.create_line(250,200,0,250,fill='blue')
c.create_line(250,200,500,250,fill='blue')

c.create_line(200,250,250,500,fill='blue')
c.create_line(300,250,250,500,fill='blue')
c.create_line(150,250,250,450,fill='blue')
c.create_line(350,250,250,450,fill='blue')
c.create_line(100,250,250,400,fill='blue')
c.create_line(400,250,250,400,fill='blue')
c.create_line(50,250,250,350,fill='blue')
c.create_line(450,250,250,350,fill='blue')
c.create_line(0,250,250,300,fill='blue')
c.create_line(500,250,250,300,fill='blue')
t.mainloop()
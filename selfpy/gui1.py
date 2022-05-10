import tkinter
from tkinter import *
t=tkinter.Tk()
t.title("Canvas")
t.geometry("1000x1000")
c=Canvas(t,height=500,width=500,bg="black")
c.place(x=10,y=10)
c.create_oval(0,0,500,500,fill='light green') 
t.mainloop()
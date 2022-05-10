import tkinter
from tkinter import *
t=tkinter.Tk()
t.title('CANVAS')
t.geometry('1000x1000')
c=Canvas(t,height=600,width=600,bg='pink')
c.place(x=10,y=10)
c.create_line(0,0,350,430,fill='blue')               #line
c.create_rectangle(30,40,200,300,fill='red')         #rectangle
c.create_oval(3,3,200,30,fill='green')               #oval
p=[50,200,200,50,400,200]
c.create_polygon(p,fill='red')                       #polygon
img=PhotoImage(file='go.gif')
c.create_image(200,200,image=img)                    #image
t.mainloop()
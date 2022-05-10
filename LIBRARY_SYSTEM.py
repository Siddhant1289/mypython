#LIBRARY SYSTEM
import pymysql
import sys
import tkinter
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
print('1.Student')
print('2.Course')
print('3.Books')
x=int(input('Enter Your Choice'))
if x==1:
	print('   #Student')
	print('1.Add')
	print('2.Delete')
	print('3.Find')
	y=int(input('Enter Choice'))
elif x==2:
	print('   #Course')
	print('1.Add')
	print('2.Delete')
	print('3.Find')
	y=int(input('Enter Choice'))
elif x==3:
	print('   #Books')
	print('1.Add')
	print('2.Delete')
	print('3.Find')
	y=int(input('Enter Choice'))
else:
	print('ANY ISSUE')
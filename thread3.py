import threading
import time
def show(name):
	x=name[::-1]
	for a in x:
		time.sleep(1)
		print(a)
x=input("enter a name")
t=threading.Thread(target=show,args=(x,))
t.start()
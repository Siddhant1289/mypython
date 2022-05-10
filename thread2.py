import threading
import time
def show(name):
	print('wait for 3 second')
	time.sleep(3)
	print('THANKS',name)
t=threading.Thread(target=show,args=("SIDDHANT",))
t.start()
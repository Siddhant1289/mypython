#THREADING
import threading
import time
def Hello():
	print('WAIT FOR 5 SECOND')
	print('')
	time.sleep(5)
	print('WELCOME TO HELLO')
t=threading.Thread(target=Hello)
t.start()
#raised 
try: 
	x=int(input('enter any no')) 
	if x>10: 
		raise Exception 
	else:
		print('ok') 
except: 
	print('some issue')
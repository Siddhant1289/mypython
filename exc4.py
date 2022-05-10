try:
	n=input('enter file name')
	f=open(n,'r')
	s=f.read(500)
	print(s)
except:
	print('any error')
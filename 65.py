#function of highest of three
def high(x,y,z):
	if x>y and x>z:
		print(x)
	elif y>x and y>z:
		print(y)
	else:
		print(z)
a=int(input('enter->'))
b=int(input('enter->'))
c=int(input('enter->'))
high(a,b,c)
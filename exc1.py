try:
	x=int(input('enter a no.'))
	y=int(input('entar a no.'))
	z=x/y
	print(z)
except ZeroDivisionError:
	print('second no. is zero')
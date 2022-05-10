#largest no.
x=int(input('enter value of x'))
y=int(input('enter value of y'))
z=int(input('enter value of z'))
if x>y and x>z:
	print(x)
elif y>x and y>z:
	print(y)
else:
	print(z)
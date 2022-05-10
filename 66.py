#returning value from function
def high(x,y,z):
	if x>y and x>z:
		return x
	elif y>x and y>z:
		return y
	else:
		return z
a=high(25,65,78)
print(a)
print(high(25,65,78))
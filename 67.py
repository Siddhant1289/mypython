def fact(x):
	f=1
	while x!=0:
		f=f*x
		x=x-1
	return f
w=fact(5)
print(w)
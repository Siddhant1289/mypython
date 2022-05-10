class My:
	x=0
	y=0
	def __init__(self,a,b):
		self.x=a
		self.y=b
		print('constructor called')
	def show(self):
		print('x is',self.x)
		print('y is',self.y)
	def __del__(self):      #name of destructor
		print('bye object')
m=My(20,10)
m.show()
p=My(20,500)
p.show()
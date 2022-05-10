#inheretance
#multi level
class Asup:
	x=0
	y=0
	def read(self,a,b):
		self.x=a
		self.y=b
	def sum(self):
		print('sum is',self.x+self.y)
class Asub(Asup):
	m=0
	n=0
	def get(self,p,r):
		self.m=p
		self.n=r
	def calc(self):
		print('sub is',self.m-self.n)
class Bsub(Asub):
	o=0
	p=0
	def val(self,g,h):
		self.o=g
		self.p=h
	def mul(self):
		print('multiply is',a*b)
p=Bsub()
p.get(10,5)
p.calc()
p.read(10,5)
p.sum()
p.val(2,2)
p.mul()
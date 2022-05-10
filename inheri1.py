#inheretance
#single level
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
p=Asub()
p.get(10,5)
p.calc()
p.read(10,5)
p.sum()
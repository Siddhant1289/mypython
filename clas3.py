class fruit:
	name=''
	price=0
	color=''
	def read(self,n,p,c):
		self.name=n
		self.price=p
		self.color=c
	def show(self):
		print(self.name,self.price,self.color)
f=fruit()
f.read('apple',100,'red')
f.show()
g=fruit()
g.read('orange',15,'orange')
g.show()
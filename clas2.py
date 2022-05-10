class fruit:
	name=''
	price=0
	color=''
	def read(self):
		self.name='apple'
		self.price=100
		self.color='red'
	def show(self):
		print(self.name,self.price,self.color)
f=fruit()
f.read()
f.show()
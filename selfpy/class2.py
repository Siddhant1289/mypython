class computer:
	
	def __init__(self):
		self.name="Siddhant"
		self.age=20
	def update(self):
		self.age=30


c1=computer()
c2=computer()
c3=computer()



print(id(c1))
print(id(c2))
c1.name="Rashi"
c1.age=12
c3.update()
print(c1.name,c1.age)
print(c2.name,c2.age)
print(c3.name,c3.age)
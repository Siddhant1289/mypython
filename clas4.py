class Employee:
	empno=0
	ename=''
	salary=0
	grade=''
	def read(self,a,b,c):
		self.empno=a
		self.ename=b
		self.salary=c
	def cgrade(self):
		if self.salary>=20000:
			self.grade='A'
		else:
			self.grade='B'
	def show(self):
		self.cgrade()
		print(self.ename,self.empno,self.grade,self.salary)
e=Employee()
e.read(20,'siddhant',50000)
e.show()
g=Employee()
g.read(101,'aman',10000)
g.show()
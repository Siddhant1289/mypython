class car:

	wheels=4				#class variable

	def __init__(self):
		self.mil=10			#instance variable ,different for different variable 
		self.com="BMW"		#instance variable




c1=car()
c2=car()
c1.mil=8
print(c1.com,c1.mil,c1.wheels)
print(c2.com,c2.mil,c2.wheels)
class phone:
	def __init__(self,phone_type,phone_cost):
		self.__phone_type=phone_type
		self.__phone_cost=phone_cost
		self.__total_cost=None
	def get_total_cost(self):
		return self.__total_cost
	def set_total_cost(self):
		self.__total_cost=value
	def calculate_total_cost(self,no_of_phones=2):
		flat_discount=500
		self.__total_cost=(no_of_phones*self.__phone_cost)- flat_discount
class Smartphone(phone):
	def __init__(self,phone_type,phone_cost,amenities_provided):
		super().__init__(phone_type,phone_cost)
		self.__amenities_provided=amenities_provided

	def calculate_total_cost(self,no_of_phones):
		super().calculate_total_cost()
		for index in self.__amenities_provided:
			amenity=index.split(":")
			self.set_total_cost(self.get_total_cost()+int(amenity[1])*int(amenity[2]))

spl=Smartphone("smart",16000,["charger:1:600","earphone:1:1200"])
spl.calculate_total_cost(1)
print(spl.get_total_cost())
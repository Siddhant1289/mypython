#function with variable arguments
def Dis(*val):
	print('call')
	for x in val:
		print('value is',x)
Dis(20)
Dis(20,2)
Dis(20,2,2,2,'abc')
Dis()
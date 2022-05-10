#we have a list of country input new country if this is already in list give error otherwise append to the list
lt=['india','us','uk','france']
c=input('enter country name-->')
if c in lt:
	print('error')
else:
	lt.append(c)
	print(lt)
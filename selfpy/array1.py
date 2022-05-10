import array
from array import *
vals=array('i',[5,9,8,4,2])
print(vals)						#print array    array('i', [5, 9, 8, 4, 2])
print(vals.buffer_info())		#(1835727235056, 5)  (address , size)
print(vals.typecode)			#i
vals.reverse()					#reverse the values
print(vals)						#array('i', [2, 4, 8, 9, 5])
vals.reverse()
vals.append(45)                 #appends value
print(vals)
for i in range(len(vals)):
    print(vals[i])
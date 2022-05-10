#matrix
from numpy import *
m1=matrix('1 2 3 ; 4 5 6 ; 7 8 9') 	#creating matrix
m2=matrix('2 5 4 ; 6 1 8 ; 3 9 7')
print(m1)							# ";" sepetates the two rows
print(diagonal(m1))					#print diagonal elements
print(m1.min())						#give min value
print(m1.max())						#give max value
#addition of two matrix
print(m1+m2)
#subtraction of two matrix
print(m1-m2)
#multiplication of two matrix
print(m1*m2)
#understanding matrix from arrays
from numpy import *
arr=array([2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17])
arr1=array([

				[1,2,3],
				[4,5,6],
				[7,8,9]
			])
print(arr1,"\n")				#print matrix
print(arr1.dtype,"\n")			#print datatype
print(arr1.shape,"\n")			#print the tuple of no. of rows and no. of columns
print(arr1.size,"\n")			#print the size of matrix
print(arr1.flatten(),"\n")		#convert 2D array into 1D array

arr2=arr.reshape(4,4)			#convert 1D array into 2D array
print(arr2,"\n")

arr3=arr.reshape(2,2,4)			#convert 1D arrar int 3D array
print(arr3,"\n")
#find out the sum of n no. of value from cmd line
import sys
l=len(sys.argv)
s=0
if l==1:
	print('pls pass value')
else:
	for i in range(1,l):
		s=s+int(sys.argv[i])
	print('the sum is -->> ',s)
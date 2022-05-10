#pass any no of name and there length 
import sys
l=len(sys.argv)
s=0
if l==1:
	print('pls pass value')
else:
	for i in range(1,l):
		print('length of ',sys.argv[i],'is',len(sys.argv[i]))
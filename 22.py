#name of largest length
import sys
l=len(sys.argv)
h=0
s=0
if l==1:
	print('pls pass value')
else:
	for i in range(1,l):
		x=len(sys.argv[i])
		if x>h:
			s=sys.argv[i]
			h=len(sys.argv[i])
	print('largest name..',sys.argv[i])
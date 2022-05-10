#pass highest value from cmd line
import sys
l=len(sys.argv)
h=0
if l==1:
	print('pls pass value')
else:
	for i in range(1,l):
		if int(sys.argv[i])>h:
			h=int(sys.argv[i])
	print(h)
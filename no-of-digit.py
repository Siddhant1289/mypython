f=open('my.txt','r')
s=f.read(500)
c=0
for x in s:
	if x.isdigit():
		c=c+1
print('digit',c)
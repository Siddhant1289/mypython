f=open('new.txt','r')
s=f.read(500)
c=0
for x in s:
	if x.islower():
		c=c+1
print('digit',c)
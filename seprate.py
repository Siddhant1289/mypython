f=open('my.txt','r')
s=f.read(500)
f1=open('bb.txt','w')
f2=open('cc.txt','w')
for x in s:
	if x.isdigit():
		f1.write(x)
	else:
		f2.write(x)
print('saved')
f.close()
f1.close()
f2.close()
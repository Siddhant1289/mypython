import time
t=time.time()
print(t)
tc=time.localtime(t)
print(tc)
ac=time.asctime(tc)
print(ac)
h=int(ac[11:13])
m=int(ac[14:16])
if h==23 and m>=4:
	print('go')
else:
	print('stay')
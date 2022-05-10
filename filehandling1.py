#reverse the text 

f=open("new.txt","r")
ff=open("BB.txt","w")

s=f.read(500)
l=len(s)

for i in range(l-1,-1,-1):
    ff.write(s[i])

print("file saved")
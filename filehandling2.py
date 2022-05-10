#to count how many numbers in a file

f=open("new.txt","r")
s=f.read(500)
c=0

for i in s:
    if i.isdigit():
        c+=1
print(c)
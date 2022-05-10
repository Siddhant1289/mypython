#user defined array
import array
from array import  *
arr = array('i' , [])
n = int(input("enter the length of array"))
for i in range(n):
    x=int(input("enter the values"))
    arr.append(x)
print(arr)
#search
val=int(input("enter the value for search"))
k=0
for e in arr:
    if e==val:
        print(k)
        break
    k+=1
#search using predefined function
print(arr.index(val))
#we can simply use the the method of temporary variable 
#or we can use the method a,b=b,a
#or we can use the method of XOR(^)
#or we can use the method of difference
a=int(input("enter 1st number: "))
b=int(input("enter 2nd number: "))

a=a+b #^
b=a-b #^
a=a-b #^
print("the value of a is: ",a)
print("the value of b is: ",b)
x=input()
y=input()
z=x+y
print(z)
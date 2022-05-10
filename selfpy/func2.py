def greet():
    print("hello")
    print("good morning")
def add_sub(x,y):
    c=x+y
    d=x-y
    return c,d
greet()
result1,result2=add_sub(4,5)
print(result1,result2)

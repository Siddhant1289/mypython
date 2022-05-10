def update(x):
    print("x",id(x))
    x=8
    print("x",id(x))
    print("x",x)

a=10
print("a",id(a))
update(a)
print("a",a)
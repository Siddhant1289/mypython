def person(name,age):           #default person(name,age=18)
    print(name)
    print(age)
    
person("Siddhant",19)           #positioning
person(age=33,name="Verma")     #keyword


#variable length argument
def sum(*a):                    # *a will create a tuple
    print(a)
    c=0
    for i in a:
        c=c+i
    print(c)
    
sum(5,6,7,8)
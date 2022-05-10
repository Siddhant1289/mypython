def person(name,**data):
    print(name)
    print(data)
    for i,j in data.items():
        print(i,j)
    
    
person("Karan Verma",age=19,city="Agra",mob=9557979666)
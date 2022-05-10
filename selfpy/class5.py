class student:
    
    def __init__(self,name,rollno):
        self.name = name
        self.rollno = rollno
        self.lap = self.laptop()
        
    def show(self):
        print(self.name,self.rollno)
        self.lap.show()
        
        
    class laptop:
        
        def __init__(self):
            self.brand="HP"
            self.cpu="i5"
            self.ram=8
        
        def show(self):
            print(self.brand,self.cpu,self.ram)
        
        
        
s1=student("Siddhant",54)
s2=student("Kumar", 33)

s1.show()
s2.show()

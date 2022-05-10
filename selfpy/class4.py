class student:
    
    school="St. Steaphen's"
    
    def __init__(self,m1,m2,m3):    #instance method
        
        self.m1=m1
        self.m2=m2
        self.m3=m3  
        
    def avg(self):              #instance method
        
        return (self.m1 + self.m2 + self.m3)//3
    
    def get_m1(self):           #getters
        return self.m1   
    
    def set_m1(self,value):     #setters
        self.m1=value
        
    
    @classmethod                #decorator
    def get_school(cls):        #class method
        return cls.school
    
    @staticmethod               #decorator
    def info():                 #static method
        print("This is student class")
        
        
    
s1=student(m1=25, m2=22, m3=27)
s2=student(m1=24, m2=26, m3=22)

print(s1.avg())
print(s2.avg())

print(student.get_school())

student.info()
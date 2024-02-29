class student:
    def  __init__(self,name,rollno):
        self.name=name      #instance  
        self.rollno=rollno
s1=student("ankush",12)
s2=student("karunakar",5)
print(s1.__dict__)
print(s2.__dict__)
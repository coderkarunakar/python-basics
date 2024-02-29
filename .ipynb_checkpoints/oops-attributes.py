# adding attributes to individual objects

class student:
    pass
s1=student()
s2=student()
s3=student()
s1.name='karunakar'
s2.name='raon'
s3.name='ram'
s2.rollno=25
s3.rollno=45
print(s1.name)
print(s2.__dict__) #this gives what u assigned for s2 like here name and roll no is assigned
print(s3.name)
print(s2.name)
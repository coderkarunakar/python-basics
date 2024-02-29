class student:
    def __init__(self,name,rollno) :
        self.name=name
        self.rollno=rollno
        
    def studentprint(self):
        print('my name is ',self.name,'and my rollno is',self.rollno)


s1=student('ranbhir singh',99)
s1.studentprint()
student.studentprint(s1)   #here this 2lines calling is same u can follow any one 
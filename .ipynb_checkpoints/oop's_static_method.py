                        #STATIC METHOD.....OR (CLASS MEHTOD) ALSO.....
                #IT WORKS WITHOUT GIVING THE SELF PARAMETER IN THE DEF FUNCTION....JUST BY DECLARING THE STATIC KEY WORD....


class student:        #NOTE: this is class name
    
    pass_percentage=40
    def studentDetails(self):           #NOTE:function name
        self.name='karunakar'
        self.percentage=80              #NOTE:this is called instance attribute
        # print('name=',self.name)
        # print('percentage=',self.percentage)
        
        


    def ispass(self):
        if self.percentage>=student.pass_percentage:    #HERE DEFINETELY NEED TO MENTION THE CLASS NAME ELSE IT CAN'T FIGUREOUT WHAT WE ARE ASKING FOR AND  GIVES ERROR.... 
            print("student is passed exam")

        else:
            print("student  is not passed the exam")


            
    @staticmethod
    def welcometoschool():
        print('hey!welcome to school')
            
            
            
s1=student()   #NOTE:object creation syntax

student.studentDetails(s1)   #NOTE:class_name.function(object_name)  is the syntax for calling  

student.ispass(s1)   #syntax for calling


s1.welcometoschool()    #static method is called with out self justby declaring @staticmethod




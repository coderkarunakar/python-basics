                    #CONCEPT:SELF PARAMETER:


# vvv.imp
# NOTE:instance attribute is available every where in the code 
# but local attribute is available to only that method only  

# class student:
#     def studentDetails(self):  #NOTE:Here not only self we can give any name
#         self.name='karunakar'     #NOTE: this is called instance attribute
#         print("name=",self.name)
#         percentage=80               #NOTE:this is called local attribute
#         print("percentage=",percentage)



        


# s1=student()
# s2=student()
# s1.studentDetails()
# student.studentDetails(s1)



# #case2:
# class student:        #NOTE: this is class name
    
#     pass_percentage=40
#     def studentDetails(self):           #NOTE:function name
#         self.name='karunakar'
#         self.percentage=80              #NOTE:this is called instance attribute
#         print('name=',self.name)
#         print('percentage=',self.percentage)
        

#     def ispass(self):
#         if self.percentage>=student.pass_percentage:   #NEED TO MENTION CLASS NAME AS IT IS VERY IMP TO ACESS...

#             print("student is passed exam")

#         else:
#             print("student  is not passed the exam")

# s1=student()   #NOTE:object creation syntax

# student.studentDetails(s1)   #NOTE:class_name.function(object_name)  is the syntax for calling  OR OBJECTANME.FUCNTIONNAME()  both are correct

# s1.ispass()   #NEED TO CALL BOTH FUCNTIONS SINCE BOTH HAVE LINK THAT PERCENTAGE... SO BOTH NEED TO CALL ELSE ERROR OCCUR NO ATTRIBUTE AS 'PERCENTAGE'



# # #OUT PUT PREDICT QUESTION....

# class student:
#     name='parikh'
#     def store_details(self):
#         self.age=60
      
#     def print_age(self):
      
#         print(self.age)


# s=student()
# s1=student()

#                                     # NOTE:for s1 need to call both function names then only it 
#                                     # will acess both function instances
# s1.store_details()
# s1.print_age()        #OBJECT NAAME.FUCNTION NAME CALL IT .... THIS IS SHORT CUT SYNTAX....
   
# #AS HERE S IS NOT USED SO IT WONT WORK JUST LIKE DUMMY IN THIS CASE...
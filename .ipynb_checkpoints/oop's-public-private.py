                                        #PUBLIC AND PRIVATE MODIFIERS....



# #NOTE:public: changing the instance variable outside the object creation  

# class student:
#     passingpercent=40
#     def __init__(self,name,age=15,percentage=80):
#         self.name=name
#         self.age=age
#         self.percentage=percentage

#     def studentDetails(self):
#         print('name=',self.name)
#         print('age=',self.age)
#         print('percentage=',self.percentage)



# s1=student('karunakar')  #SINCE IT IS AN CONSTRUCTOR AND SOME DEFAULT VALUES ARE ALREADY GIVEN... AND IN PLACE OF NAME NO VALUE ID GIVEN SO I HAD GIVEN HERE....
# print(s1.name,end=' ')
# print(s1.age)
# # changing outside  class   so it is called public
# s1.name='ranbhir singh'
# s1.age=12
# print(s1.name,end=' ')
# print(s1.age)
        




                                        #PRIVATE MODIFIERS....
            #NOTE:WE CAN MAKE VARIABLES OR FUNCTIONS AS PRIVATE MODIFIERS... JUST BY GIVING 2UNDERSCORES..IN FRONT OF IT...

# #NOTE:PRIVATE: cant change the instance variable outside 
# #the object creation


# class student:
#     passingpercent=40


#     # this block is only for creation  OF CONSTRUCTOR...
#     def __init__(self,name,age=15,percentage=80):
#         self.__name=name  #making it as private just by giving __ 2 underscor
#         self.__age=age     #making it as private just by giving __ 2 underscor
#         self.percentage=percentage
    
        
        
#     # this block is for printing purpose
#     def studentDetails(self):
#         print('name=',self.__name)   #need to give like how we declared above  (I,E FOR ACESSING HERE...)..
#         print('age=',self.__age)
#         print('percentage=',self.percentage)



# s1=student('karunakar')   #created an object for class
# s1.studentDetails()   #here just called





# # name mangling can use to fix private concept but it is no where
# # used in the python just for reference see this how to declare


# # object._classname__variable name
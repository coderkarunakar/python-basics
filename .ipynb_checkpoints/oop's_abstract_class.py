# #                                     #ABSTRACT CLASS

# #Note:abstract class cannot be created.. only it's child class is created...
# # #ABSTRACT CLASS contains abstract methods .it is declared but it has no implementation. it is implemented by someone 
# # #here in this case it is implemented by abc class.


# # #abc is a base class which contains all the classes and methods.
# # from abc import ABC,abstractmethod          #here  abc(i.e abstract base class) in which ABC(is just a class in the abc) 
# #                                             #,abstract method  is an functionality or an decorator in the abc only 

                                                    
# # class automobile(ABC):      #note:this is just the syntax don't worry we are inheriting From ABC class from the abc that's it 

# #     def __init__(self) :    #it is just an constructor
# #         print("automobile created")   #some thing is printed  here that's it ..

        

# #         #NOTE:     vvvvv,imp point  this are called as abstract methods in parent class this needed to be
# #                                             # called in child class definetely and it does not have any implementation 
# #                                                 #every thing is implemented in the abc class only from that we are gettig this.
# #     @abstractmethod
# #     def start(self):
# #       pass

# #     @abstractmethod
# #     def stop(self):
# #         pass
    
# #     @abstractmethod
# #     def drive(self):
# #         pass

# # class car(automobile):


# #     def __init__(self,name):
# #         print("car is created")
# #         self.name=name

    
# #     def start(self):
# #       pass

# #     def stop(self):
# #       pass

# #     def drive(sself):
# #         pass

# # class bus(automobile):      #just this acquires the all  properties from the automobile.


# #     def __init__(self,name):
# #         print("delhi metro bus  is created")
# #         self.name=name

    
# #     def start(self):
# #         pass
# #     def stop(self):
# #         pass
# #     def drive(sself):
# #         pass  
    
# # c=car("sam")     #note:when ever we call like this it directly refers to the constructor if constructor is not found in the child then it goes to parent class
# # D=bus("rahi")      #vvvvv.imp point  here only car bus is used automobile is not called since abstract class cant be created......













#                                     #CONTINUTION OF ABSTRACT CLASS.......


# # #NOTE:ABSTRACT METHODS CAN HAVE SOME MATTER  ALSO NOT ONLY EMPTY . AND U CAN CALL THAT ABSTRACT METHOD AS WELL.....
 

# from abc import ABC,abstractmethod          #here ABC is class  abc(i.e abstract base class) abstract method is an functionality or an decorator

# class automobile(ABC):      #note:this is just the syntax don't worry we are inheriting From ABC class that's it 

#     def __init__(self) :    #it is just an constructor
#         print("automobile created")   #some thing is printed

        

#         #NOTE:     vvvvv,imp point  this are called as abstract methods in parent class this needed to be called in child class definetely 
#     @abstractmethod
#     def start(self):
#         print("hey here automobile function is called")

#     @abstractmethod
#     def stop(self):
#         pass
    
#     @abstractmethod
#     def drive(sself):
#         pass

# class car(automobile):


#     def __init__(self,name):
#         print("car is created")
#         self.name=name

    
#     def start(self):
#         super().start()   #here just parent function is called
#         print("hey here the start of the car is called")

#     def stop(self):
#         print("hey here the stop of car is called")

#     def drive(sself):
#         pass

# class bus(automobile):


#     def __init__(self,name):
#         print("delhi metro bus  is created")
#         self.name=name

    
#     def start(self):
#         pass
#     def stop(self):
#         pass
#     def drive(sself):
#         pass  
#                         #now we will be calling the fuctions present inside the child class and parent abstract class cant be created vv.imp note
# c=car("sam")     #note:when ever we call like this it directly refers to the constructor if constructor is not found in the child then it goes to parent class
# c.start()  #this is the syntax for calling the function inside the def i.e abstract method
# c.stop()

# D=bus("rahi")      #vvvvv.imp point  here only car bus is used automobile is not called since abstract class cant be created......









# #     LITTLE CONFUSION IN THIS CODE..... 
 


# # #                     CASE 3: WITHOUT CONSTRUCTOR IN THE CHILD CLASS ALSO WE CAN MAKE IT 
# # from abc import ABC,abstractmethod          #here ABC is class  abc(i.e abstract base class) abstract method is an functionality or an decorator

# # class automobile(ABC):      #note:this is just the syntax don't worry we are inheriting From abc class that's it 

# #     def __init__(self,wheel) :    #it is just an constructor
# #         self.wheel=wheel
# #         print("automobile created")   #some thing is printed
       
        

# #                               #NOTE:     vvvvv,imp point  this are called as abstract methods in parent class this needed to be called in child class definetely 
# #     @abstractmethod
# #     def start(self):
# #         print("hey here automobile function is called")

# #     @abstractmethod
# #     def stop(self):
# #         pass
    
# #     @abstractmethod
# #     def drive(self):
# #         pass
# #     @abstractmethod
# #     def wheel(self):
# #         return self.wheel

# # class car(automobile):



    
# #     def start(self):
# #         super().start()   #here just parent function is called
# #         print("hey here the start of the car is called")

# #     def stop(self):
# #         print("hey here the stop of car is called")

# #     def drive(self):
# #         pass

# #     def wheel(self):
# #         return super().wheel()

# # class bus(automobile):


 

    
# #     def start(self):
# #         pass
# #     def stop(self):
# #         pass
# #     def drive(self):
# #         pass  
# #     def wheel(self,wheel):
# #         return super().wheel()
    
# # c=car(4)     #note:when ever we call like this it directly refers to the constructor if constructor is not found in the child then it goes to parent class


# # D=bus(8)     

# # print(c.wheel())








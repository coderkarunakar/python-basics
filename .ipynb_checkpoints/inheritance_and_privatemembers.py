#                                         # #INHERITANCE and PRIVATE MEMBERS:


# # #this is the code for inheritance very easy concept
# # making private members  using __ 2 underscores and and accesing it by using get and set methods.. and note;while printing also need to use the get method only ..

# class vechile:
#     def __init__(self,color,maxspeed):
#         self.color=color
#         self.__maxspeed=maxspeed   #here we have done it as private member

#     def getMaxspeed(self):     #this is the get method syntax
#         return self.__maxspeed
#     def setMaxspeed(self,maxspeed):    #this is set method syntax
#         self.__maxspeed=maxspeed

# class car(vechile):     #this is the syntax for acquiring properties of super or parent class
#     def __init__(s, color, maxspeed,no_of_gears,is_convertible):
#         super().__init__(color, maxspeed)       #this is actual purpose of code which actually reducing our writing of codeit is the syntax lool it carefully
#         s.no_of_gears=no_of_gears
#         s.is_convertible=is_convertible

#     def print_car(self):
#         print("color",self.color)
#         print("maxspeed",self.getMaxspeed())   # this is syntax for calling the private member
#         print("no_of_gearsis",self.no_of_gears)
#         print("is_convertible",self.is_convertible)

# c1=car("orange",190,5,True)  #as we know this is our simple assigning terms what we gave above
# c1.print_car()    #this is simple calling of function name


# #note : instead of giving only self we can give anything like our wish but need to continue same till end of the code complete...





                        #INHERITANCE CONTINUTION

#A SMALL TRICK TO AVOID GET SET METHOD IN ORDER TO ACESS THE PRIVATE MEMBER IN THE FUNCTION

#this is easy instead of using get and set method just 2 steps i.e giving a print function below the private members and just by calling that print function   in the last print function
#instead of using get set method in the code for accesing the private members this is also a trick 

class vechile:
    def __init__(self,color,maxspeed):
        self.color=color
        self.__maxspeed=maxspeed   #here we have done it as private member

# NOTE: VVV.IMP POINT for printing the private members u can simply declare like this as given below
    def printfunction(self):
        print("color",self.color)
        print("maxspeed",self.__maxspeed)  

class car(vechile):     #this is the syntax for acquiring properties of super or parent class
    def __init__(s, color, maxspeed,no_of_gears,is_convertible):
        super().__init__(color, maxspeed)       #this is actual purpose of code which actually reducing our writing of codeit is the syntax lool it carefully
        s.no_of_gears=no_of_gears
        s.is_convertible=is_convertible

    def print_car(self):
        super().printfunction()     #iNOTE:VV .IMP POINT Instead of super() we can use self. as well both works fine ,this is another way of accesing the private  memebers
        print("no_of_gearsis",self.no_of_gears)
        print("is_convertible",self.is_convertible)

c1=car("orange",190,5,True)  #as we know this is our simple assigning terms what we gave above
c1.print_car()    #this is simple calling of function name

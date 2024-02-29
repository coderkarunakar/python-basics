#PROTECTED MEMBERS:it is just same like public member the only difference is in public we can change anything and we can make any modification
#but in protected we cannot make any modification we need to use this astise
#NOTE:this protected member is represented as _ single underscore and we need to use this with single under score only no need to change it...







class vechile:
    def __init__(self,color,maxspeed):
        self.color=color
        self._maxspeed=maxspeed   #here we have done it as protected member just by giving single underscore infront
                                                #of maxspeed

# NOTE:  short cut method just give print stament and call it below VVV.IMP POINT for printing the private members
        #u can simply declare like this as given below
    def printfunction(self):
        print("color",self.color)
        print("maxspeed",self._maxspeed)  

class car(vechile):     #this is the syntax for acquiring properties of super or parent class
    def __init__(s, color, maxspeed,no_of_gears,is_convertible):
        super().__init__(color, maxspeed)       #this is actual purpose of code which actually reducing our writing of codeit is the syntax lool it carefully
        s.no_of_gears=no_of_gears
        s.is_convertible=is_convertible

    def print_car(self):
        print('color',self.color)    #iNOTE:VV .IMP POINTInstead of super() we can use self. as well both works fine ,this is another way of accesing the private  memebers
        print('maxspeed',self._maxspeed)
        print("no_of_gearsis",self.no_of_gears)
        print("is_convertible",self.is_convertible)

#         #this gives all as the child class contains parent+child class
# c1=car('red',180,5,True)  #as we know this is our simple assigning terms what we gave above
# c1.print_car()    #this is simple calling of function name


        
#     #this gives only the parent classs details only as we are calling only parent class
# v=vechile('red',18)
# v.printfunction()
# v._maxspeed=180   #we can use like this just by giving the single underscore and modify it 
# v.printfunction()
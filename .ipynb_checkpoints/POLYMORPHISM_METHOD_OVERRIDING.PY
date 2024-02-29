#NOTE:POLYMORPHISM:(I.E METHOD OVERRIDING CONCEPT):THIS MEANS IT CAN WORK IN MULTIPLE WAYS OR MANY WAYS
#IN THIS CODE WE HAD CREATED A SAME FUNCTION NAME I.E printfunction() in parent class and child class  as well and it can be acessed through
#super(). if both child has the parent class function as well.....  





class vechile:
    def __init__(self,color,maxspeed):
        self.color=color
        self.__maxspeed=maxspeed   #here we have done it as private member

# NOTE: VVV.IMP POINT for printing the private members u can simply declare like this as given below
    def printfunction(self):      #see here same function name as mentioned in child class so method riding involves hence super(). is used in child class
        print("color",self.color)
        print("maxspeed",self.__maxspeed)  

class car(vechile):     #this is the syntax for acquiring properties of super or parent class
    def __init__(s, color, maxspeed,no_of_gears,is_convertible):
        super().__init__(color, maxspeed)       #this is actual purpose of code which actually reducing our writing of codeit is the syntax lool it carefully
        s.no_of_gears=no_of_gears
        s.is_convertible=is_convertible

    def printfunction(self):        #see heree same function as mentioned above in the vechile class
        super().printfunction()     #NOTE:instead of printing  properties we can call function as wellhere we used super().since mehtod overriding concept involved it cant be called through the self.
        print("no of gears is",c1.no_of_gears) #here u can give self or object name as well both works fine
        print("is_convertible",self.is_convertible)

c1=car("orange",190,5,True)  #as we know this is our simple assigning terms what we gave above
c1.printfunction()    #this is simple calling of function name



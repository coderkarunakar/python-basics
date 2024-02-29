                                                #INHERITANCE:
#this is the code for inheritance very easy concept
#only 3 steps  are very imp i.e 1.acquiring properties of parent class 2.

class vechile:      #for parent class
    def __init__(self,color,maxspeed):
        self.color=color
        self.maxspeed=maxspeed

class car(vechile):     # this is child class .this is the syntax for acquiring properties of super or parent class
    def __init__(self, color, maxspeed,no_of_gears,is_convertible):
        super().__init__(color, maxspeed)       # this acquires the properties of parent instance . this is actual purpose of code which actually reducing our writing of codeit is the syntax lool it carefully
        self.no_of_gears=no_of_gears
        self.is_convertible=is_convertible

    def print_car(self):        #this is just for printing purpose
        print("color",self.color)
        print("maxspeed",self.maxspeed)
        print("no_of_gearsis",self.no_of_gears)
        print("is_convertible",self.is_convertible)

c1=car("orange",190,5,True)  #as we know this is our simple assigning terms what we gave above
c1.print_car()    #this is simple calling of function name


#note : instead of giving only self we can give anything like our wish but need to continue same till end of the code complete...
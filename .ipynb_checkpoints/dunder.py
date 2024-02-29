# class snowflake:  #just created a class
#     pass                #as of now i have no info so am keeping it as pass
# flake=snowflake()       #here object is created
# print(dir(flake))       #here getting the al methods available  in that objects just run and check it once.we get all the dunder methods.


# class martian:
#     pass
# m1 = martian()
# m1.first_name='owen'
# m1.last_name='phels'
# print(m1.__dict__)  #this dict gives object attrributes like keys and its values




# class martin:
#     "someone who lives on mars"
#     def __init__(self,fn,ln) :
#         self.first_name=fn
#         self.last_name=ln

        
# m1=martin("karunakar","anu")
# m1.arrival_date ='199-8-54'  #note:we can add data like this additionally also for the object..
# m1.deathdate='2088-8-7'
# print(m1.__dict__)
        




                    #DUNDER METHODS
#THE NAME DUNDER METHOD SINCE IT HAS DOUBLE UNDERSCORES


#when object is created the init method is automatically called  init is an constructor 



# #normal way of addition
# class addition:

#     def set_val(self):
#         self.var1=int(input("enter the value1:"))

#         self.var2=int(input("enter the value1:"))
#     def add(self):
#         self.sum=self.var1+self.var2

        
#     def disp(self):
#         print(f'sum of{self.var1} and {self.var2} is {self.sum}')

# a=addition()
# a.set_val()
# a.add()
# a.disp()

        


#using the init constructor method 
# class addition:

#     def __init__(self,var1,var2) :
#         self.value1=var1
#         self.value2=var2



#     def add(self):
#         self.sum=self.value1+self.value2

        
#     def disp(self):
#         print(f'sum of{self.value1} and {self.value2} is {self.sum}')



# a=addition(2,8)


# a.add()
# a.disp()

        



#___str__


class addition:

    def __init__(self,var1,var2) :
        self.value1=var1
        self.value2=var2



    def add(self):
        self.sum=self.value1+self.value2

        
    def disp(self):
        print(f'sum of{self.value1} and {self.value2} is {self.sum}')

    def __str__(self) :
        print("rey kak")
        return "rey  mama manaki enduku ra"
    def __repr__(self) :
        print("repr is same like str mamu")
        

a=addition(2,8)


a.add()
a.disp()
print(a)  #here we are trying to print the object created above directly it gives u the reference like its information in binary format  
            #if u have __str__ in the code it will return,or print both works here what u gave in the str only else it shows u the object reference.


# #note:__repr__ is just does the same work of __str__ does but when both are present only __str__ works not __repr__ since in python 
# __repr__ it does not have much importance .but  when only __repr__ is present then defintetely it prints the information available in the 
# __repr__
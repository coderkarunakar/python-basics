# #operator overloading means : example + operator this works in many ways i.e addition ,concatinating two strings 
# #merging two lists.

# #here we are trying to add two points  i.e p1,p2... using __add__ dunder method..


# # #operator_overloading concept:
# # #here our main aim is to add 2points like p1=(1,1) and p2=(2,2) and if we add p1+p2 we need to get (3,3) as x+x term and y+y term is getting
# # #added and we  will be getting our result this is our main aim and in order to add 2 points we have some inbuild function like __add__,for add
# # #for subttaction __sub__ like this 

# import math   #this is for performing sqrt operation we have imported
# class point:
#     def __init__(self,x,y):   #2 parameters
#         self.__x=x   #here 2 underscores is used as it is private
#         self.__y=y     # simple assigning is done

#         #note:when ever u use the __add__ __sub__ like this dunder methods we need to use the __str__ fucntion.
#      #this down line just makes the logic to add and for printing purpose we need to use __str__ dunder fucntion
#     def __add__(self,point_object):     #this add  is for adding purpose..
#         return point(self.__x+point_object.__x,      self.__y+point_object.__y)  #here x terms and y terms are added
    

#     #this down line gives u the actual print that is done in the __add__ fucntion.
#     def __str__(self) :            #as we studied previously this is for our understanding purpose ,here we can make any note
#         return "this point is at ("+str(self.__x)+","+str(self.__y)+")"   # here x term and y term is assigned in self only so it gives actual output
    
    
#     #this down line is for printing true or false i.e (x^2 + y^2 )<(p.x^2 +p.y^2)

#     def __lt__(self,point_object):  #note:this lt method is used for < less than operator  mainly for maths function.
#         return math.sqrt(self.__x**2+self.__y**2)<math.sqrt(point_object.__x**2+point_object.__y**2) #here simple sqrt function implemented and compared less than or not
    
# p1=point(1,290)  # here points are assigned
# p2=point(3,4)
# p3=p1+p2
# print(p3) #p3 is printed
# print(p2<p1)  #just comparision is done
    
        


                                                    # OOP'S FRACTION CLASS...  

# #CASE1:this is for 2 arguments like example:f=Fraction(2,3)


# #NOTE:   .__dict__  value gives the  key value pairs like what we have assigned to all of it...

# class Fraction:
#     def __init__(self,numerator,denominator):
#         self.numerator=numerator
#         self.denominator=denominator

# f=Fraction(2,3)
# print(f.__dict__)

        

# # CASE2:this is for no arguments like f=Fraction() and it have to take like 0/1  WE CAN MAKE IT LIKE GIVING IN THE DEFAULT VALUE ONLY ...

# class Fraction:
#     def __init__(self,num=0,den=1):
#         self.num=num
#         self.den=den


# f1=Fraction()  #note:if we dont give any thing here just it takes like 0/1 as we declared in the def else given values will
# print(f1.__dict__)

#CASE 3:IF ONLY  ONE ARGUMENT WAS PASSED THEN IT HAVE TO RETURN LIKE   0/1

# class Fraction:
#     def __init__(self,num=0,den=1):
#         self.num=num
#         self.den=den


# f1=Fraction(3) 
# print(f1.__dict__)
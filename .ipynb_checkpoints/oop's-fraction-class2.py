                                    #FRACTION CLASS -2




# # #case1:if the numerator is zero then the output should be 0 else it should be like a/b only...

# class Fraction:
#     def __init__(self,num,den):
#         self.num=num
#         self.den=den
#     def printfraction(self):
#         if self.num==0:
#             print(0)
#         else:
#             print(self.num,'/',self.den)
# a=int(input("enter the first number please..."))
# b=int(input("enter the second number please..."))

        
# f1=Fraction(a,b)
# Fraction.printfraction(f1)


#case2:   if the denominator is 1 then print output as numerator only


# class Fraction:
#     def __init__(self,num,den):
#         self.num=num
#         self.den=den
#     def printfraction(self):
#         if self.num==0:
#             print(0)
#         elif(self.den==1):
#             print(self.num)
#         else:
#             print(self.num,'/',self.den)
# a=int(input("enter the first number please..."))
# b=int(input("enter the second number please..."))
        
# f1=Fraction(a,b)
# Fraction.printfraction(f1)



#case3: if denominator=0 then take den=1 and print numerator only
# class Fraction:
#     def __init__(self,num,den):
#         if den==0:                    #note:this two steps are for taking if den==0 take it as den=1 .nothing just u need to remember this syntax that,s it
#             den=1
#         self.num=num
#         self.den=den
#     def printfraction(self):
#         if self.num==0:
#             print(0)
#         elif(self.den==1):
#             print(self.num)
#         else:
#             print(self.num,'/',self.den)

# a=int(input("enter the first number please..."))
# b=int(input("enter the second number please..."))
        
# f1=Fraction(a,b)
# Fraction.printfraction(f1)




  


# # #case4: 
#SIMPLYFYING THE NUMERATOR AND DENOMINATOR


# class Fraction:
#     def __init__(self,num=0,den=1):
#         if den==0:
#             den=1
#         self.num=num
#         self.den=den

        

#     def printfraction(self):
#         #IF NUM=0 OUTPUT SHOULD BE 0
#         if self.num==0:
#             print(0)
#         #IF DEN=1 THEN OUTPUT SHOULD BE NUMERATOR
#         elif(self.den==1):
#             print(self.num)
#         #IF NUM!=0 AND DEN!=1 THEN PRINT OUTPUT LIKE A/B
#         else:
#             print(self.num,'/',self.den)
        

#     def simplify(self):
#         #IF NUM/DEN IS IS BIG NO AND CAN BE DIVIDED WITH ANY NO 
#         #THEN IT MUST DIVIDE THAT SIMPLIFICATION IS DONE HERE
#         current=min(self.num,self.den)
#         while current>1:
#             if self.num%current==0 and self.den%current==0:         #here we need to take  check the remainder.if thsi statement false means only curent -1 i.e next statement takes place...
#                 break
#             current-=1
#         self.num=self.num//current    # we need to take the float
#         self.den=self.den//current

# a=int(input("enter the first number please..."))
# b=int(input("enter the second number please..."))
            
            
            
# f1=Fraction(a,b)

# f1.simplify()       #WE NEED TO PRINT AFTER SIMPLIFY IT THEN ONLY WE GET SIMPLIFICATION
# f1.printfraction()




#                                     #case 5:

# #ADDITION OF 2 FRACTIONS IS DONE IN THIS CASE 
# #SEE NOTES AND COME HERE ONCE


# class Fraction:
#     def __init__(self,num=0,den=1):
#         if den==0:
#             den=1
#         self.num=num
#         self.den=den

        

#     def printfraction(self):
#         #IF NUM=0 OUTPUT SHOULD BE 0
#         if self.num==0:
#             print(0)
#         #IF DEN=1 THEN OUTPUT SHOULD BE NUMERATOR
#         elif(self.den==1):
#             print(self.num)
#         #IF NUM!=0 AND DEN!=1 THEN PRINT OUTPUT LIKE A/B
#         else:
#             print(self.num,'/',self.den)
        

#     def simplify(self):
#         #IF NUM/DEN IS IS BIG NO AND CAN BE DIVIDED WITH ANY NO 
#         #THEN IT MUST DIVIDE THAT SIMPLIFICATION IS DONE HERE
#         current=min(self.num,self.den)
#         while current>1:
#             if self.num%current==0 and self.den%current==0:
#                 break
#             current-=1
#         self.num=self.num//current
#         self.den=self.den//current
            
            
        
#                                         #THSI IS VERY UNIQUE IMPLEMENTATION AS FAROF NOW IN THE INSTANCE CLASS...


#         #here we are performing add operation (i.e self,other fraction) are the 2 fractions 
#         #here we are creating an instance i.e operation is given i.e logic in NewNum,NewDen.. and we are asigning it with the self.NewNun,self.NewDen
        
#     def add(self,otherFraction):
#         NewNum=otherFraction.den*self.num+otherFraction.num*self.den            #this is the operation of the logic....

#         NewDen=self.den*otherFraction.den

#         self.num=NewNum
#         self.den=NewDen
#         self.simplify()
# f1=Fraction(2,3)
# f2=Fraction(1,3)


# f1.add(f2)              #this plays a major role in this logic which is actually adding the f1,f2
# f1.printfraction()




#                                                         case6:
# IN THIS CASE MULTIPLICATION OF 2 FRACTIONS IS DONE

class Fraction:
    def __init__(self,num=0,den=1):
        if den==0:
            den=1
        self.num=num
        self.den=den

        

    def printfraction(self):
        #IF NUM=0 OUTPUT SHOULD BE 0
        if self.num==0:
            print(0)
        #IF DEN=1 THEN OUTPUT SHOULD BE NUMERATOR
        elif(self.den==1):
            print(self.num)
        #IF NUM!=0 AND DEN!=1 THEN PRINT OUTPUT LIKE A/B
        else:
            print(self.num,'/',self.den)
        

    def simplify(self):
        #IF NUM/DEN IS IS BIG NO AND CAN BE DIVIDED WITH ANY NO 
        #THEN IT MUST DIVIDE THAT SIMPLIFICATION IS DONE HERE
        current=min(self.num,self.den)
        while current>1:
            if self.num%current==0 and self.den%current==0:
                break
            current-=1
        self.num=self.num//current
        self.den=self.den//current
            
            
    def add(self,otherFraction):
        NewNum=otherFraction.den*self.num+otherFraction.num*self.den

        NewDen=self.den*otherFraction.den

        self.num=NewNum
        self.den=NewDen
        self.simplify()


        
        #THIS IS THE LOGIC FOR MULTIPLICATION  LIKE (X/Y)*(A/B)=(XA/YB ) WE NEED TO MAKE AS PER THAT  LOGIC IS MADE..
    def multiply(self,otherFraction):
        NewNum=otherFraction.num*self.num
        NewDen=otherFraction.den*self.den
        self.num=NewNum
        self.den=NewDen
        self.simplify()

f1=Fraction(2,3)
f2=Fraction(1,5)
f1.multiply(f2)     #THIS MAKES THE LOGIC FOR THE MULTIPLICATION...
f1.printfraction()          #THIS IS FOR CALLING THE FUCNTION OF MULTIPLICATION...
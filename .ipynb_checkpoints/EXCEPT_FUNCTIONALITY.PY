# # #                     #EXCEPT FUCNTIONALITY..

#raise keyword it works like when except is present it gives the except value only if the error was not found in except 
#then this raise keyword comes into picture..and in console we can  see the what ever we gave in the raise keyword.

#if we give some error in the class then definetely it will throw the errror which was given the class only 
#if we give Except in  the class then this Except  consist of all the error so it checks for the error what it has in the except 
#if not found it gives the error present  in the raise keyword...






# # # #case 1: refering the value error in the except

# class zerodenominatorerror(Exception):    #Exception  contains all the errors and we can give a specific error as well
#     pass                                    #IF U GIVE specific error it throws that error only...
# while True:

    
#     try:
#         num=int(input("enter an no"))
#         a=num
#         num2=int(input("enter a no"))
#         b=num2
#         if b==0:
#             raise zerodenominatorerror ('arey babu rey denominator lo zero  ivakura')  #if u give correcct it wont give error if u give wrong it gives error here what u mentioned..with init constructor as well
#         print("hii")   
#         c=a/b
        
#         print(c)
#     except(ValueError):  
#         print("Numerator and Denominator should be same TAMUD")   

#     except(zerodenominatorerror):  
#         print("rey tamudu denominator lo zero ivadani chepana")   
        

# #case 2:  order matters even if we give the specific error        

class zerodenominatorerror(Exception):    #Exception  contains all the errors and we can give a specific error as well
    pass
while True:

    
    try:
        num=int(input("enter an no"))
        a=num
        num2=int(input("enter a no"))
        b=num2
        if b==0:
            raise zerodenominatorerror ('arey babu rey denominator lo zero  ivakura')  #if u give correcct it wont give error if u give wrong it gives error here what u mentioned..with init constructor as well
        print("hii")   
        c=a/b
        
        print(c)
   
            #order matters 
    # except(zerodenominatorerror):  
    #     print("rey tamudu denominator lo zero eyAKANIchepana")  

    except(ValueError):  
        print("Numerator and Denominator should be same chicha") 
        








# #         #CASE 3: if we give only except without any any name...then it matters.. but  we need to give empty except only at the last if we try to give at first we get error

# class zerodenominatorerror(ValueError):    #Exception  contains all the errors and we can give a specific error as well
#     pass
# while True:

    
#     try:
#         num=int(input("enter an no"))
#         a=num
#         num2=int(input("enter a no"))
#         b=num2
#         if b==0:
#             raise zerodenominatorerror ('arey babu rey denominator lo zero  ivakura')  #if u give correcct it wont give error if u give wrong it gives error here what u mentioned..with init constructor as well
#         print("hii")   
#         c=a/b
        
#         print(c)
   
        
   
            
#     except(NameError):  
#         print("rey tamudu denominator lo zero eyyamni chepana")  

#     except(TypeError):  
#         print("Numerator and Denominator should be same chicha") 

       #above 2 not matched so we get this empty except since it contains all errors.....NOTE:BUT THIS NEED TO GIVE ONLY AT THE LAST ELSE ERROR MIGHT OCCUR
    # except:  
    #     print("hey rama except lo emi ivaka pothe kachitanga ide print avtadi ra babu")
        
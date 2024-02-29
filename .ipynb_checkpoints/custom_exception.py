
#CASE 1:
#in this case we gave Zero  division error and  it is that error it checks in the code i.e at the except .. and gives the print value what we gave

# try:
#     num=int(input("enter an no"))
#     a=num
#     num2=int(input("enter a no"))
#     b=num2
#     if b==0:
#         raise ZeroDivisionError  #as we here we gave zeroDivisionError it checks if it is zerodivision errror then it prints what we gave in the except code
#     print("hii")
#     c=a/b
#     print(c)
# except(ValueError,ZeroDivisionError):  #like this we can give multiple errors in a single line 
#     print("Numerator and Denominator should be same mama")   


#CASE 2:
#if it is not the error what we mentioned then it gives that what we gave error name that is what done using the raise keyword

# try:
#     num=int(input("enter an no"))
#     a=num
#     num2=int(input("enter a no"))
#     b=num2
#     if b==0:
#         raise TypeError  #as we here we gave zeroDivisionError it checks if it is zerodivision errror then it prints what we gave in the except code
#     print("hii")
#     c=a/b
#     print(c)
# except(ValueError,ZeroDivisionError):  #like this we can give multiple errors in a single line 
#     print("Numerator and Denominator should be same mama")   



#CASE 3:giving as per requirement without any error then works fine

# try:
#     num=int(input("enter an no"))
#     a=num
#     num2=int(input("enter a no"))
#     b=num2
#     if b==0:
#         raise ZeroDivisionError  #as we here we gave zeroDivisionError it checks if it is zerodivision errror then it prints what we gave in the except code
#     print("hii")   #this statement means else .even we dont mention it mean that only since given the below the if lines... so it takes in that mannner
#     c=a/b
    
#     print(c)
# except(ValueError,ZeroDivisionError):  #like this we can give multiple errors in a single line 
#     print("Numerator and Denominator should be same mama")   


#CASE 4:  CREATING OUR OWN EXCEPTION 

# class zerodenominatorerror(Exception):    #Exception  is a inbuild object which has own constructor and inbuild exception errors as welll
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
#     except(ValueError):  
#         print("Numerator and Denominator should be same mama")   




#CASE5: CALLING THE EXCEPT ERROR ONLY AS WE GAVE IN THE PRINT FUNCTION 

class zerodenominatorerror(Exception):    #Exception  is a inbuild object which has own constructor and inbuild exception errors as welll
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
    except(ValueError):  
        print("Numerator and Denominator should be same mama")   

    except(zerodenominatorerror):  #IT JUST GIVES THIS ERROR IF DEN IS ZERO INSTEADD OF RAISE BECAUSE IT CHECKS IN except FIRST THEN RAISE....
        print("rey tamudu denominator lo zero ivadani chepana")   

                

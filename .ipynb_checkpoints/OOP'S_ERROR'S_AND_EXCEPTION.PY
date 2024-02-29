                                    #ERROR'S AND EXCEPTION...
#here we are just trying to   print division  a/b

# num=int(input("enter an no"))
# a=num
# num2=int(input("enter a no"))
# b=num2

# c=a/b
# print(c)


#here if i try  to give  string (like abc)and a integer(lke 4) it gives an VALUE ERROR: invalid literal for int ()
#but even though if wwe give like that we can stop that type of error just by giving (try and except ) let us see




#handling the (VALUE ERROR) using try and except

# try:

#     num=int(input("enter an no"))
#     a=num
#     num2=int(input("enter a no"))
#     b=num2

#     c=a/b
#     print(c)
# except ValueError:    #note:if u dont specify anything like valueerror ,name error ,typeerror then it will handle all the errors,
#     print("Numerator and Denominator should be same mama")   # now instead of value error we get what we have printed in  the print statement if we try to print the strinng and an integer 


#NOTE:if u give SOME ERROR instead of ACTUAL ERROR it might give u error it can't handle it .... better not to specify anything it will handle all the errors





# try:
#     num=int(input("enter an no"))
#     a=num
#     num2=int(input("enter a no"))
#     b=num2

#     c=a/b
#     print(c)
# except:    #see here i didn't  specified anything here so it will handle all the errors
#     print("Numerator and Denominator should be same mama")   # now instead of value error we get what we have printed in  the print statement if we try to print the strinng and an integer 


#NOTE:if code works fine then no error will raise






#just time pass i gave this if it is true it works else it breaks
# while True:

#     try:
#         num=int(input("enter an no"))
#         a=num
#         num2=int(input("enter a no"))
#         b=num2

#         c=a/b
#         print(c)
#         break
#     except:    #see here i didn't  specified anything here so it will handle all the errors
#         print("Numerator and Denominator should be same mama")   # now instead of value error we get what we have printed in  the print statement if we try to print the strinng and an integer 

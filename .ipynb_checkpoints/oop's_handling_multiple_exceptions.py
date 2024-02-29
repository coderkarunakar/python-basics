#             #HANDLING MULTIPLE EXCEPTIONS...

# try:
#     num=int(input("enter an no"))
#     a=num
#     num2=int(input("enter a no"))
#     b=num2

#     c=a/b
#     print(c)
# except(ValueError,ZeroDivisionError):  #like this we can give multiple errors in a single line 
#     print("Numerator and Denominator should be same CHICHA")   



    


#     #or we can give it in multiple lines also both works fine
try:
    num=int(input("enter an no"))
    a=num
    num2=int(input("enter a no"))
    b=num2

    c=a/b
    print(c)
except ValueError:   #this line specifies the error u want to handle..just give the errror in the last line ...after the code get completed..   
    print("Numerator and Denominator should be same mama")   

except  TypeError:    
    print(" hey ka ka denominator me zero nahi rahna chahiye")   
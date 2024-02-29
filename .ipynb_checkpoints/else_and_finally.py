# #         #concept
# # #else and finally keywords.



# # #else concept

# # class zerodenominatorerror(ValueError):    #Exception  contains all the errors and we can give a specific error as well
# #     pass
# # while True:

    
# #     try:
# #         num=int(input("enter an no"))
# #         a=num
# #         num2=int(input("enter a no"))
# #         b=num2
# #         if b==0:
# #             raise zerodenominatorerror ('arey babu rey denominator lo zero  ivakura')  
# #         print("hii")   
# #         c=a/b
        
# #         print(c)
   
        
   
            
# #     except(NameError):  
# #         print("rey tamudu denominator lo zero eyyamni chepana")  

# #     except(TypeError):  
# #         print("Numerator and Denominator should be same chicha") 

       
# #     except:  
# #         print("hey rama except lo emi ivaka pothe kachitanga ide print avtadi ra babu")
        

# #     else:           #note:this else code will work only if no error has been raised..that means all the above exception has not raised
# #         print("hey babu ikada exception em ledu le po") 



# #                                             #FINALLY CONCEPT
# #          #THE ORDER MUST BE LIKE THIS CASE 1:TRY,except,FINALLY  OR CASE 2:TRY ,EXCEPT,ELSE,finally
        
        
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

#        #above 2 not matched so we get this empty except since it contains all errors.....NOTE:BUT THIS NEED TO GIVE ONLY AT THE LAST ELSE ERROR MIGHT OCCUR
#     except:  
#         print("hey rama except lo emi ivaka pothe kachitanga ide print avtadi ra babu")
#     else:
#         print("rey mama gurtupetuko exception error raise avakapotene e else panichestundi ra mama")
#     finally:
#         print("rey mama exception error raise ina avakapoina e final matram panichestadi ra babu")
#         print(a)
#         print(b)
#         print(c)  #note:here it gives which is in scope like only integers,float like that it wont give error value..... just know it or 
#                     #try to give the error values....
# basic syntax for function 


# def function_name(paramater1,paramatern)#note :function name can be anything,param is inputs variable
#     body
#     body 
#     body
#     body 
# return value#it act like a output

#Note:we can give multiple output values.....

#Note :it is very very important topic vvvvvvvv 100%

#example:calculator
def calci(x,y):
    print("the addition is ", x+y)
    print("the subtraction  is ", x-y)
    print("the multiplication  is ", x*y)
    print("the division is =", x/y) #here this , is very important
calci(2,3)


# calci(5,6)



# calci(1,1)

# calci(3,3)


#if we dont give any parameters we get like this

def great():
     print('hello mama')  #WE GET HELLO MAMA BECAUSE CALLING FUNCTION NAME
great()   #here we get output as None since we didnt gave any parameters



#if we print with  out giving any parameters

# def great():
#      print('hello mama')
# print(great())#HERE WE GET OUTPUT AS NONE BECAUSE NO PARAMETERS IN LINE 43 AND PRINTING FUNCTION NAME


# def great():
#       print('good') #here we  get "none" since return is not used 
# print(great())

# #return


# def great():
#      return "good evening"

# print(great())#here we get out as "good evening "since used return 


#with return key word

# #printing output using a 'variable' 
# def king():
#      return 'how are you'
# msg=king()
# print(msg) #here we get output as how are you since return used and a variable also used


#with out return key 

# def king():
#      print('how are you')
# msg=king()
# print(msg)  #in this case return is not used used print and a variable so
#            #so we get 'how are you ' and None since return is not used




#'Positional argument use '

# def great(name):
#     print("my name is :",name) #here name is called as positional argument
# great("karunakar") #(o/p: my name is karunakar)


#types in functions 


#(1): positional function


# def H(firstname,lastname):
#     print('please tell your name',firstname,lastname)
# H("chembeti","karunakar")



#2.key word argument


# def G(firstname,lastname):
#     print("mynameis:",firstname,lastname)
# G(lastname="karunakar",firstname="chembeti")#here order is not necessary but params =args



#03. Default value


# def great(firstname="guest"):   #here firstname is defaultly given as guest
#     print("good evening",firstname)
# great()




# def great(firstname="guest"):   #here firstname is defaultly given as guest
#     print("good evening",firstname)
# great()


#REPLACING DEFAULT VALUE BY PASSING ARGUMENT

# def great(firstname="guest"):   
#     print("good evening",firstname)
# great(" ghost   ")  #here we get good evening ghost since we have passed argument
#                  #if we dont pass it takes default value given at top


#04_VARIABLE - LENGTH ARGUMENTS

#without any arguments

# def test(*args):
#     print(args)
#     print(len(args))
#     print(type(args))
# test()


#with arguments


# def test(*args):
#     print(args)
#     print(len(args))
#     print(type(args))
# test("australia","america", "europe")


#Note :here we cant use keyword args but for that a trick is there we need to use (**args)

# def test(**args):
#     print(args)
#     print(type(args))
#     print(len(args))
# test(firstname="karunakar",lastname="chembeti",father="son")

















# #USING  RETURN AND CALLING WITH PRINT

# from re import I


# def fact(n):
#     n_fact=1
#     for i in range(1,n+1):
#         n_fact=n_fact*i
#     return n_fact
# print(fact(5))
    



#USING PARAMETERS AND ARGUMENTS
# def cal(a,b):
#     print('add', a+b)
#     print('sub', a-b)
#     print('mul', a*b)
#     print('end')

# cal(4,4)
# cal(2,6)


#return here (return statement +calling(i.e with print())) is very much important


#case 1: it is general form 
# def greet():
    


#     print("kevvu anu")
#     return 
    

# print(greet())

#case 2: at output gives only kevvu anu and () because after return we gave only ()
# def greet():
    


#     print("kevvu anu")
#     return ()
    

# print(greet())

# case 3: below return statements wont work
# def greet():
    



#     return 
#     print("kevvu anu")
    

# print(greet())





# parameters and arguments in def method


# def cal(a,b):
#     print("hii")
#     print('add',a+b)
#     print('sub',a-b)
#     print('mul',a*b)
# cal(3,4)


# #POSITIONAL ARGUMENT IN DEF METHOD ,(i,e it has some rules also go and learn it in note book)


# def mana_tv(first_name,last_name):
#     print("my name is ",first_name,last_name)

# mana_tv('karunakr','chembeti')

# mana_tv('karunakr','talagapu')

# mana_tv('karunakr','pilla')


# #return + parameters (Note: when u use  return  + parameter it wont work ) If u give parameter functionality then it works
# # only for parameter and return ka work nahi karega b
# def user_id(firstname,lastname):
#     print("my name is ram kalyan")
#     return ("hii guys")
    
# user_id('ram','kalyan')





#keyword (read rules in book)

#case1
 
# def user_id(first_name,last_name):
#     print("my name is ",first_name,last_name)


# user_id(first_name="chembeti",last_name="karunakar")

#case2
#after positional  argument a keyword argument (Note:vice versa wont work)

# def user_id(first_name,last_name):
#     print("my name is ",first_name,last_name)


# user_id("chembeti",last_name="karunakar")





#DEFAULT ARGUMENT

# #case 1: no arguments given only default parameters are given
# def user_id(firstname="karuankar",lastname="chembeti"):
#     print("my name is ",firstname,lastname)




# #case 2: default value is given + arguments also given
# def user_id(firstname="karunakar",lastname='chembeti'):
#     print('my name is',firstname,lastname)
# user_id("surya ","bhai")


#4.variable-length argument
#it is used when we dont know how many inputs are going to be  and output is in the form of tuple or dict as per our req
#it is of 2 types they are as follows
# #1.*args

#Note:it should have only 1star* and it takes only individual not an (keywords)
#output gives as an tuple
# def  test(*args):
#     print(args)
#     print(len(args))
#     print(type(args))
# test('karunakar','chembeti','hari')

#**kwargs #here 2stars **must be given
#Note: it gives output as dict i.e{'':''} and it takes only keywords here individuals wont work
#output gives as a dictionary

# def  test(**kwargs):
#     print(kwargs)
#     print(len(kwargs))
#     print(type(kwargs))
# test(first='karunakar',second='chembeti',third='hari')
# write a program to perform all input and output operations of all basic data types


# user input with a message


# name=eval(input("enter your name please"))
# print("hello ",name)
# print(type(name))


# taking float as input


# a=float(input("enter your float input")) 
# add = a+1
# print(add)

# taking multiple inputs from user in a single line

# Note:here .split() is very important while taking multiple inputs in a single line

# Note:here map is also imp because using 2 or more inputs at a same line

# Note:after every single input give 1 space because of split  or instead of space 
# u can give anything like , just keep .split(",")

# integer type

# Name,age=map(int,input("enter your name and age:").split())
# print(Name)
# print(age)
# print(type(Name))
# print(type(age))

# float type


# Name,age=map(float,input("enter your name and age:").split())
# print(Name)
# print(age)
# print(type(Name))
# print(type(age))


# string  type


# Name,age=(input("enter your name and age:").split(","))#here no need to give space give ,after a input
# print(Name)
# print(age)
# print(type(Name))
# print(type(age))


# #taking input from list and set
# list=list()        #this is called creating a list
# set=set()          #   this is called creating a list
# l=int(input("enter the no of elements in a list")) #here we took int because for taking
#                                                    # no elements always like1,2,3..int form 
#                                                    # later after selecting we can give int ,
#                                                    # float ,
#                                                     # str etc list set always take
# for i in range(0, l):
#     list.append(input())#in list we can give elements through 
#                         #.append()


# s=int(input("enter the no elements in set"))
# for i in range(0,s):
#     set.add(input())   #in set we can give elements through 
#                         #.add()

# print(list)
# print(set)




# taking input from in list and set using map function  just in  a single line


# list=list(map(int,input("enter the set values").split()))
# set=set(map(int,input("enter the set values").split()))
# print(list)
# print(set)



# taking user input from tuple using list

# t=(1,2,3,4)
# print("tuple values before ",t)
# l=list(t)
# l.append(int(input("enter value u want ")))# here after int , is not took sinz append takes only 1 element  , for multiple elements , is taken
# T=tuple(l)
# print("the values of tuples after is",T)




# #out put  using print( )
# print("gfg")
# print("g","f","f")




# #in output using end =""   and sep =""


# print("gfg", end="@") #Note: end ="" is used to get  only 1 next line in the current line with a symbol
# print("karun","akar",sep="&")
# print("karun","akar",sep="\n")# sep="" it is used seperate a string with a symbol





# string formatting

# RULES: WE NEED TO USE {} AND A     f  or F at the beggining let us see


# name="karunakar"
# print(f"my name is {name}, am fine")
# print(F"my name is {name},! am fine") # we can use F also 


# string formatting using .format()   and   checking ....
# RULE: NEVER FORGET {} ,.format()


# a=10
# b=20

# sum=a+b
# sub=a-b

# print("the value of a is {} and b is {}".format(a,b))
# print("{2} is the sum of {1} and {0}".format(a,b,sum))
# print("{value_sub}is the subtraction of {value_a} and {value_b}".format(value_a=a,value_b=b,value_sub=sub))






# #using %d operator in python 

# num=int(input("enter the input value"))
# add=num+5
# print("the value of add is %d" %add)





# RULE:  FOR .FORMAT() AND %d operator there will be no , after statement  ends

#vvv imp

#taking multiple user input in new line let us see



# l=[]
# n=int(input("enter range of no"))
# for i in range(n):   #here it can give how many u enter in n  like 3 means 3
#     a=int(input())
#     l.append(a)
# print(l)
#

# l=[]

# for i in range(3):   #here it can give only like 3 means 2
#     a=int(input())
#     l.append(a)
# print(l)



#multiple inputs in tuple

l=[]
n=int(input("enter no of elements"))
for i in range(n):
    elements=(int(input()))
    l.append(elements)
    tup=tuple(l)
print(tup)    
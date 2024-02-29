# using positional argument

# def cube(x):
#     return x*x*x

# n=int(int(input("enter the number u want to perform cube")))

# cube(n)
# print('the cube of a {0} is {1}'.format(n,cube(n)))




# # # finding diameter ,circumference,area of a circle
# import math

# def diameter(x):
#     return 2*x
# def circumference(x):
#     return 2* math.pi*x
# def area(x):
#     return math.pi*x*x

# n=int(input('enter the radius'))

# diameter(n)
# circumference(n)
# area(n)
# print(diameter(n),end=' ,')
# print(circumference(n),end=' ,')
# print(area(n),end=',')


# using return functionality

# import math

# def find_Diameter(radius):
#     return 2 * radius

# def find_Circumference(radius):
#     return 2 * math.pi * radius

# def find_Area(radius):
#     return math.pi * radius * radius

# r = float(input(' Please Enter the radius of a circle: '))

# diameter = find_Diameter(r)
# circumference = find_Circumference(r)
# area = find_Area(r)

# print(diameter)
# print(circumference)
# print(area)


# # Python program to find the
# # maximum of two numbers

# Python program to find the
# maximum of two numbers

# using position parameter

# def maximum(a, b):
	
# 	if a >= b:
# 		print(a) 
# 	else:
# 		print(b)
# a=int(input('enter '))
# b=int(input('enter '))
# maximum(a,b)
	

# # find even or odd using def key word
# def evenodd(n):
#     if n%2==0:
#         return "even"
#     else:
#         return "odd"
# n=int(input('enter the  no  to be checked'))
# print(evenodd(n))




# # using positional parameter
# def evenodd(n):
#     if n%2==0:
#         print("even")
#     else:
#         print("odd") 
# n=int(input('enter the  no  to be checked'))
# (evenodd(n))



# doubt
# # printing amstrong number using def keyword
# def amst(low,upp):
#     for i  in range(low,upp):
#         sum=0
#         order=len(str(i))
#         temp=i
#         while temp>0:
#             digit=temp%10
#             sum=sum+digit**order
#             temp=temp//10

#         if i==sum:
#             return i
    
# low=int(input("enter the lower no"))
# upp=int(input("enter the upper no"))
# a=low
# b=upp
# print(amst(a,b))







         
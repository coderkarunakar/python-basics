# #gcd of two no usig for loop

# a=int(input("enter the first no"))
# b=int(input("enter the second no"))
# c=(min(a,b))
# gcd=c
# i=1
# for i in range(1,c):
#     if(a%i==0 and b%i==0):
#         gcd=i


# print("the gcd of two numbers is ",gcd)

#using while loop

# a=int(input("enter the first no"))
# b=int(input("enter the second no"))
# c=(min(a,b))
# gcd=c
# i=1
# while(i<=c):
#     if(a%i==0 and b%i==0):
#         gcd=i
#     i=i+1

# print("the gcd of two numbers is ",gcd)



# #prime numbers in a range
# lower=int(input("please enter the number"))
# upper=int(input("please enter the no"))
# print("the prime numbers in the given range is ")
# for num in range (lower,upper+1):
#     if(num>1):
#         for i in range(2,num):
#             if(num%i==0):
#                 break
#         else:
#             print(i)
    

#check if the given no is in fibonacci or not

# num=int(input("enter the number u want to check"))

# a=0
# b=1
# c=0
# if num==0 or num==1:
#     print("the given no is fibonacci member")
# else:
#     while c<=num:
#         c=a+b
#         a=b
#         b=c
#     if c==num:
#         print("the given number is fib")
#     else:
#         print("the given  number is not a fib")



#printing all prime no in this range

# num=int(input("please enter the no"))

# k=2
# while(k<=num):
#     flag=False
#     d=2
#     while(d<k):
#         if(k%d==0):
#             flag=True
#         d=d+1
#     if not(flag):
#         print(k)
#     k=k+1


# n=int(input("enter"))
# i=1
# while i<=n:
#     start_char=chr(ord('A')+i-1)
#     j=1
#     while j<=n:
#         x=chr(ord( start_char)+j-1)
#         print(x,end=" ")
#         j=j+1
#     print()
#     i=i+1


# n=int(input("enter the number"))
# i=1
# while i<=n:
#     space=1
    
#     #spacing
#     while space<=n-i:
#         print(' ',end=" ")
#         space=space+1
#     #increasing seq
    
#     j=1
#     while j<=i:
#         print(j,end=' ')
#         j=j+1
#     #decreasing seq
#     p=i-1
#     while p>=1:
#         print(p,end=" ")
#         p=p-1
#     i=i+1
#     print()





#    1
#   121
#  12321
# 1234321






# n=int(input(" enter a number"))
# i=1
# while i<=n:
    
#     #spacing
#     space=1
#     while space<=n-i:
#         print(" ",end=" ")
#         space=space+1
    
#     #increasing no
#     j=1
#     while j<=i:
#         print(j,end=" ")
#         j=j+1
#     #decreasing no
#     p=i-1
#     while p>=1:
#         print(p,end=" ")
#         p=p-1
#     print()
#     i=i+1


# # A
# # B C
# # C D E
# # D E F G
# # PATTERN PRINT
# n=int(input("enter the number"))
# i=1
# while i<=n:
#     j=1
#     start_char=chr(ord('A')+i-1)
#     while j<=i:
#         x=chr(ord(start_char)+j-1)
#         print(start_char,end=" ")
#         j=j+1
#     print()
#     i=i+1


from this import d


# # D
# # C D
# # B C D 
# # A B C D 
# n=int(input("enter the range grid"))
# i=1
# while i<=n:
    
#     start_char=chr(ord('A')+n-i )
#     j=1
#     while j<=i:
#         x=chr(ord(start_char)+j-1)
#         print(x,end=" " )
#         j=j+1
#     print( )
#     i=i+1



# # A B C D 
# # A B C 
# # A B 
# # A 

# n=int(input("enter the grid "))
# i=1
# while i<=n:
#     j=1
#     start_char=chr(ord('A')+i-1)
#     while j<=n-i+1:
#         x=chr((ord(start_char)+j-1))
#         print(x,end=" ")
#         j=j+1
#     print()
#     i=i+1

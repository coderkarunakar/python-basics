# def greet():
#     print("hiii mama how are you")
#     print('yesterday i met an person in the conference room')
# greet()

# arguments and parameters


# def greet(first_name,last_name):
#     print(f"hii,{first_name} {last_name}")  #it is also a type of printing with   f "{}{}"
#     print("welcome to abroad")
# greet('karunakar','chembeti')


# arguments and parameters +return and its print type
# def greet(first_name,last_name):
#     print(f"{first_name} {last_name}")


# def greet_card(first,last):
#     return f'{first} {last}'


# message=greet_card("karan","chembeti")
# print(message)

# greet("ramm","sita")

#vv.imp that when ever u give return u must give print type else u wont get output 
#and when ever u give parameters  u  must give arguments


#Note:all functions return a None when u dont specify its value in it


# def greet(name):
#     return name  
# print(greet("ram"))


# def increment(a,b):
    
#     return a+b
# print(increment(3,7))



#CODING NINJAS DEF FUNCTIONS

# # factorial of a no

# ncr formula is n!/r!*(n-r)! this is what here is done using def key

# def fact(a):
#     a_fact=1
#     for i in range(1,a+1):
#         a_fact=a_fact*i
#     return a_fact


# n=int(input("enter the no"))
# r=int(input("enter the no"))
# n_fact=fact(n)
# r_fact=fact(r)
# n_r_fact=fact(n-r)
# ans=n_fact//(r_fact*n_r_fact)
# print(ans)  #here print is used since return is used



# check the given no is prime or not using def key

# def primeornot(b):

#     for i in range(2,b):
#         if b%i==0:
#             break
#     else:
#         return True
#     return False
# def primefrom2ton(n):
#     for k in range(2,n+1):
#         is_k_prime=primeornot(k)
#         if(is_k_prime):
#             print(k)
# n=int(input('enter a no'))
# primefrom2ton(n)  



# n=int(input("enter the no"))
# r=int(input("enter the no"))
# def fact(a):
#     a_fact=1
#     for i in range(1,a+1):
#         a_fact=a_fact*i

#     return a_fact

# def ncr(n,r):

   
#     n_fact=fact(n)
#     r_fact=fact(r)
#     n_r_fact=fact(n-r)
#     ans=n_fact//(r_fact*n_r_fact)
#     return ans
    
# print(ncr(n,r))

# def func(a ):
#     a=a+10
#     return a
# a=5
# print(func(a))
# # print(a)

# #conjugate of a complex number in python
# z3=complex(2,-3)
# def conjugateof(z3):
#     return(z.conjugate())
# z=z3
# print("the complex conjugate of a no is",conjugateof(z3))
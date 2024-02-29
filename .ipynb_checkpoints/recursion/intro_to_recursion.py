#                                     #INTRO_TO_RECURSION
# def fact(n):
    
#     if n==0:  #the base case (i.e which is very necessary for the recursion)
#         return 1

#     return n*fact(n-1)  #the main logic
# n=int(input('enter the no u want factorial'))
# print(fact(n))  #here the function is called 


# def fact1(n):
    
#     if n==0:  #the base case (i.e which is very necessary for the recursion)
#         return 1

#     return n*fact1(n-1)  #the main logic
# n=int(input('enter the no u want factorial'))
# print(fact1(n))  #here the function is called 


#assignment question power of a number using recursion..
def power(n,p):
    if p==0:
        return 1
    elif p>0:
        return (n*power(n,p-1))  #here n remains same and power is getting reduced till it reaches to 1 and fucntion is getting called here . it get stores in the memory untill the condition is true..
    else:
        return 1/power(n,-p)
if __name__=='__main__':  
    n=2
    p=5

print(power(n,p))
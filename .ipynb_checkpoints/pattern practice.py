# # ****
# # ***
# # **
# # *
# # print this pattern
# n=int(input("enter the grid:"))
# i=1
# while i<=n:
#     j=1
#     while j<=n-i+1:
#         print("*",end="")
#         j=j+1
#     print()
#     i=i+1

# # ****
# #  ***
# #   **
# #    *
# #print this pattern

# n=int(input("enter the grid please"))
# i=1
# while i<=n:
#     space=1
#     while space<=i-1:
#         print(" ",end="")
#         space=space+1
#     j=1
#     while j<=n-i+1:
#         print("*",end="")
#         j=j+1
#     print()
#     i=i+1






# n=int(input("enter the grid please"))
# i=1
# while i<=n:
#     space=1
#     while space<=i-1:
#         print(" ",end="")
#         space=space+1
#     j=1
#     while j<=n-i+1:
#         print(j,end="")
#         j=j+1
#     print()
#     i=i+1


# #    1
# #   121
# #  12321
# # 1234321
# #print this pattern



# n=int(input("Please enter the grid"))
# i=1
# while i<=n:
#     #for spaces on left side
#     space=1
#     while space<=n-i:
#         print(" ",end="")
#         space=space+1
#     #for increment purpose
#     j=1
#     while j<=i:
#         print(j,end="")
#         j=j+1
#     #for decrement purpose
        
#     p=i-1
#     while p>=1:
#         print(p,end="")
#         p=p-1
#     print()
#     i=i+1

# #    1
# #   232
# #  34543
# # 4567654

# n=int(input("Enter the grid"))
# i=1
# while i<=n:
#     #for spacing purpose
#     space=1
#     while space<=n-i:
#         print(' ',end='')
#         space=space+1
#     #for left  pattern
#     j=1
#     value=i
#     while j<=i:
#         print(value,end="")
#         value=value+1
#         j=j+1
#     #for right pattern
#     p=i-1
#     while p>=1:
#         print(p+i-1,end="")
#         p=p-1
#     print()
#     i=i+1
    

# #    *
# #   ***
# #  *****
# # *******
# #  *****
# #   ***
# #    *
# #print this diamond pattern



# N=int(input("enter the grid"))
# n1=(N+1)/2
# n2=n1-1
# print(n1)
# print(n2)
# n2=n1-1
# i=1
# while i<=n1:
#     space=1
#     while space<=n1-i:
#         print(" ",end="")
#         space=space+1
#     j=1
#     while j<=(i*2)-1:
#         print("*",end="")
#         j=j+1
#     print()
#     i=i+1

# row=n2
# while row>=1:
#     spa=1
   
#     while(spa<=n2-row+1):
#         print(" ",end="")
#         spa=spa+1
#     col=1
#     while col<=(2*row)-1:
#         print("*",end="")
#         col=col+1
#     print()
#     row=row-1


# factorial of a number the formula is n!/r!*(n-r)!
# n=int(input('enter a number'))
# r=int(input('enter  the r number'))
# n_fact=1
# for i  in range(1,n+1):
#     n_fact=n_fact*i

    
# r_fact=1
# for i  in range(1,r+1):
#     r_fact=r_fact*i

    
# n_r_fact=1
# for i  in range(1,n-r+1):
#     n_r_fact=n_r_fact*i


# ans=n_fact//(r_fact*n_r_fact)
# print(ans)

   
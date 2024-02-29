#1. #python program to print all  natural no from 1-100
# i=1
# while i<=100:
#     print(i)
#     i=i+1

# #2.program to find thee reverse of a no using while loop

# num=int(input("please enter a no"))
# reverse =0


# while num!=0:
#     digit=num%10
#     reverse=reverse*10+digit
#     num//=10
# print("the reverse of a no is"+str(reverse))

#3.while loop to print a-z alphabets


# #note: 97  means a and 122 means z vv imp in ascii
# i=97
# while i<123:  #here we took like this condition 
#                   #is enter no should be in range of 97 se 122 i.e a-z
#     print(chr(i))  #chr is used to print characters like a-z
#     i=i+1  #for increment


#4. #print all odd no's from  1-100
# i=1
# while i<=100:
#     if(i%2!=0):
    
#         print(i)
#     i=i+1





#5.print all even no's from range 1-100

# i=1
# while i<=100:
#     if i%2==0:

#         print(i)
#     i=i+1





#6.print sum of all natural no between 1-100


# num=int(input("please enter the no"))

# sum=0
# while num>0:
#     sum=sum+num
#     num=num-1
# print(sum)


# #7. sum of all even from 1-100

# i=1
# sum=0
# while i<=100:
#     if i%2==0:
#         sum=sum+i
#     i=i+1
# print(sum)



# #8.SUM OF ODD NO BETWEEN 1-N


# i=1
# sum=0
# while i<=3:
#     if i%2!=0:
#         sum=sum+i
#     i=i+1 

# print(sum)


#9.print multiplication table of any no

# i=1
# sum=int(input("please enter a no"))
# while i<=10:
#     sum=sum*1#for getting a no as like table u will understand
#     mul=sum*i#logic
#     print(sum,'*',i,'=',mul)
#     i=i+1
    

#10. count no of digits in a number

# #124 as 3 no's


# num=int(input("please enter the number"))

# count=0
# while(num!=0):
#     num=num//10
#     count=count+1
# print("the no of digits is ",count)





# #12.addition of first digit and last digit of a given no

# num=int(input("enter a no"))
# last=num%10
# while(num!=0):
#     first=num%10
#     num=num//10

# sum=last+first
# print(sum)



# # #11.TO FIND FIRST DIGIT AND A LAST DIGIT OF A NUMBER

# #as of now there are two ways to find the approach

# # num=int(input("please enter a number"))

# # last_digit=num%10

# # first_digit=int(str(num)[0])
# # print(last_digit)
# # print(first_digit)



# num=int(input("please enter thee number"))
# last=num%10
# while(num!=0):
#     first=num%10
#     num=num//10

# print(first)
# print(last)



# #13.to swap first digit and last digit of a number

# num=int(input("please enter a number"))

# last_digit=num%10

# first_digit=int(str(num)[0])
# print("before swap lastno",last_digit)
# print("before swap first no",first_digit)


# first_digit,last_digit=last_digit,first_digit


# print("after swap first no",first_digit)
# print("after swap last no",last_digit)




# #14.program to calculat sum digits of a number

# num=(input("please enter the number"))

# sum=0

# for i in  num:
#     sum=sum+int(i)  #here we gave int since string cannot iterate so only int can iterate
# print(sum)



# #another approach

# num=int(input("please enter the number"))

# tot=0

# while(num!=0):
#     dig=num%10
#     tot=tot+dig
#     num=num//10
# print("the total of a digits are",tot)



# 15.product of a number

# num=int(input("please enter a number"))

# product=1
# while(num!=0):
#     rem=num%10
#     product=product*rem
#     num=num//10
# print("the product of this no is",product)



#16.to reverse a number

# num=int(input("please enter the number"))


# rev=0
# while(num!=0):
#     rem=num%10
#     rev=rev*10+rem
#     num=num//10
# print("the reverse of a number is ",rev)




# #17.pallindrome or not



# num=int(input("please enter the input"))
# original_no=num
# rev=0
# while(num!=0):
#     rem=num%10
#     rev=rev*10+rem
#     num=num//10
# print("the reverse of a number is ",rev)

# if rev==original_no:
#     print("it is pallindrome")
# else:
#     print("it is not a  pallindrome")

#18.program to find the frequency of each digit of a given integer







base = 3
exponent = 4

result = 1

for exponent in range(exponent, 0, -1):
    result *= base

print("Answer = " ,(result))
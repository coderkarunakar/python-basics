# #  2.write a program to take two no and find sum of them


# # a=int(input("enter a value"))
# # b=int(input("enter next value"))
# # c=a+b
# # print("the sum of two no is ",c)

# #3. write a program to take two no and perform arthimatic operations


# # a,b=map(int,input("enter the two no").split())

# # print("the addition of these no is ", a+b)
# # print("the subtraction of these no is ", a-b)
# # print("the multiplicatiom of these no is ", a*b)
# # print("the division of these no is ", a/b)



# #4.perimeter of a rectangle

# # length=int(input("enter the value of length"))

# # breadth=int(input("enter the value of breadth"))

# # perimeter=2*(length+breadth)  #formula
# # print("the perimeter of a rectangle is",perimeter)


# #5. program to find  area of  a rectangle

# # length,breadth=map(int,input("enter the length and breadth").split())
# # area=length *breadth
# # print("the area of a rectangle is", area)




# # #6.find circumference,area , diameter of a circle with  given radius
# # radius=int(input("please enter the  radius of a circle"))
# # diameter=2*radius

# # print("the diameter of a circle is ", end="")
# # print(diameter )
# # circumference=2*3.14*radius

# # print("the circumference of a circle is ", end="")
# # print(circumference )
# # area =3.14*(radius *radius)

# # print("the area of a circle is ", end="")
# # print(area)


# #7.write a python program to take length in centimeter and convert to meter and kilometer

# # centimeter,meter,kilometer=float(input("please enter length in centimeters")),0,0

# # meter=float(centimeter/100)  #formula
# # print("the centimeter to meter conversion is", meter ,"meter")

# # kilometer=float(centimeter/100000)  #formula
# # print("the centimeter to kilometer conversion is",kilometer,"kilometer")




# # #8.write a python program to enter temperature in celsius and convert to farhein  heat


# # celsius=float(input("enter the temperature in celsius"))

# # farheinheat=(celsius*1.8)+32  #formula


# # print("the temperature in celsius is converted to farhein heat i.e is",farheinheat)


# # #9.take input temperature as fahreinheat and convert to  celsius

# # fahreinheat=float(input("enter the temperature in terms of fahreinheat"))


# # celsius =(fahreinheat-32)/1.8
# # print("the celsius is ",celsius,"degreees")


# #10. write a pyton program to convert days into years , weeks , days

# #this program is used to show no of days as yrs,weeks,and days like 365 days as
# # 1yr,0weeks,0days


# # num=int(input("please enter the no of days"))
# # year=int(num/365)
# # weeks=int(num%365)/7
# # days=int(num%365)%7
# # print('\nyear' +str(year),'week' + str(weeks),'days'+str (days)) #here +is used because str can only concate



# #11.write a python program to find power of any number

# #using for loop




# # base=int(input())
# # exponent=int(input())

# # result=1
# # for data in range(exponent,0,-1): #if ex:exponenet is 3 it goes like 3,2,1
# #     result=result*base #if base is 2 it gives like 1*(2*2*2) this will be stored in result
# # print(result)


# # #using pow() function

# # base=int(input())
# # exponent=int(input())


# # result=pow(base,exponent)
# # print(result)




# #12.finding square root of a number

# # num=int(input("enter a number"))
# # sqrt=num**0.5
# # print("the square root of a number is ",sqrt)

# #13.write a python program to enter two angles and find third angle


# # p,q,r=int(input()),int(input()),None
# # r=180-(p+q)
# # print("the third angle is ",r)

# #14.write a program to find area of a triangle with its base and height

# # base=float(input("enter the base of triangle"))
# # height=float(input("enter the height of a triangle"))

# # area=0.5*(base*height)       #formula

# # print("the area of a triangle is ",area)


# #15.find the area of equilateral triangle

# # side=float(input("please enter the side of a triangle"))

# # area=1.73*side*side/4
# # print("the area of  a equilateral triangle is ", area)


# # #16.program to enter marks of a five subjects and find the total,average, and percentage
# # telugu=int(input('enter the marks of the telugu subject'))
# # hindi=int(input('enter the marks of the hindi subject'))
# # english=int(input('enter the marks of the english subject'))
# # maths=int(input('enter the marks of the maths subject'))
# # science=int(input('enter the marks of the science subject'))
# # total=telugu+hindi+english+maths+science
# # average=total/5
# # percentage=(total/500)*100
# # print(total)
# # print(average)
# # print(percentage)




# #17. find simple intrest

# # principle=int(input("please enter principle"))
# # time=int(input("please enter time"))
# # rate=int(input("please enter rate of interest"))
# # simple_intrest=(principle*time*rate)/100
# # print(simple_intrest)


# #21.power of a no
# base=2
# exp=3

# result=1
# # while exp!=0:
# #     result=result*base
# #     exp=exp-1
# # print(result)



# #using for loop

# # for exp in range(exp,0,-1):
# #     result=result*base
# # print(result)


# # 22.factorial of a number

# # num=int(input("please enter a num"))

# # for i in range(1,num+1):#factor will be from 1 and here for loop ends <1 to what u give
# #     if num%i==0:#a factor is a no gives rem as zero
# #         print(i)



# # #using while loop
# # num=int(input("please enter a number"))
# # i=1
# # while i<=num:
# #     if num%i==0:
# #         print(i)
# #     i=i+1


# #23.factorial  of a no
# #using while loop

# # num=int(input("enter a no"))

# # i=1
# # res=1
# # while i<=num:
# #     res=res*num
# #     num=num-1
# # print(res)


# # #using for loop
# # num=int(input("enter a no"))
# # res=1
# # for i in range (1,num+1):
# #     res=res*i
# # print(res)


# #24.program to find hcf   #doubt


# # # # using a for loop

# # # num1=int(input(""))
# # # num2=int(input(""))
# # # hcf=1
# # # for i in range(1,min(num1,num2)):
    
# # #     if num1%i==0 and num2%i==0:
# # #         hcf=i

# # # print(hcf)


# # #26.check wheather given no is prime or not i.e divisible by 1 and itself


# # num=int(input("please enter the no"))

# # flag=False
# # if num>1:

  
# #     i=2
# #     while(i<num):
# #         if(num%i)==0:
# #             flag=True
# #         break
# # if flag:
# #     print("it is not a prime ")
# # else:
# #     print("it is a prime no")


# # # #using for loop
# # # num=int(input("please enter a no"))


# # # flag=False
# # if num>1:
# #     i=2
# #     for i in range(2,num):
# #         if num%2==0:
# #             flag=True
# #         break
# # if flag:
# #     print("it is not prime")
# # else:
# #     print("it is  prime")




# # #27.print all prime no in between 1 to n

# # num=int(input("enter a no"))

# # for i in range(2,num+1):
# #     for j in range(2,i):  #vvv.imp always remem  in for loop ends at less than 1
# #         if(i%j==0):
# #             break
# #     else:
# #         print(i)


# # #28.sum of n prime no
# # num=int(input("enter  a  no"))
# # sum=1

# # for i in range(2,num+1):
# #     for k  in range(2,i):
# #         if(num%i==0):
# #             i=num
# #         break
# #     if i is not num:
# #         sum=sum+num
# #         #logic
# # print(sum)



# # #30.CHECK WHEATHER THE GIVEN NO IS AMSTRONG OR NOT


# # num=int(input("plese enter the no"))

# # sum=0

# # temp=num

# # while temp>0:

# #     digit=temp%10

# #     sum=sum+(digit**3)

# #     temp=temp//10

# # if num==sum:
# #     print(sum,"it is an amstrong")
# # else:
# #      print(sum,"it is not an amstrong")


# # #31.print all  amstrong no in between an n interval


# # lower=int (input("enter the no"))
# # upper=int (input("enter the no"))


# # for i in range(lower , upper+1):


# #     sum=0
    
# #     order=len(str(i))
# #     temp=i
# #     while(temp>0):
# #         digit=temp%10
# #         sum=sum+(digit **order)
# #         temp=temp//10

# #     if (sum==i):
# #         print(i)



# # #32.perfect no or not
# # num=int(input("please enter the no"))

# # sum=0

# # for factor in range(1,num):
# #     if(num%factor==0):
# #         sum=sum+factor
# # if sum==num:
# #     print("the given no is an perfect no")

# # else:
# #     print("the given no is not an perfect")

# # #34.given no is strong no or not 
# # num=int(input("please enter the no"))#145

# # tem=num
# # sum=0
# # while(tem>0):
# #     digit=tem%10

# #     fact=1
# #     for i in range(1,digit+1):
# #         fact=fact*i

# #     sum=sum+fact
# #     tem=tem//10

# # if(sum==num):
# #     print("the given is strong")
# # else:
# #     print("the given no is not strong")


# # #36.print all the fibonacci series upto n 
# # num=int(input("enter the limit of a no"))
# # a=0
# # b=1
# # count=0
# # while(count<num):
# #     print(a)
# #     c=a+b
# #     a=b
# #     b=c
# #     count=count+1



# #using for loop
# # num=int(input("enter the limit of a no"))

# # a=0
# # b=1
# # count=1

# # for i in range(1,num+1):
# #     print(a)
# #     c=a+b
# #     a=b
# #     b=c

# #37.ones complement of a number



# # a=6
# # bin(a)
# # b=bin(~a)
# # print(b)


# import functools

# nums=[1,2,4,6]
# x=functools.reduce(lambda x,y:x^y,list(range(len(nums)+1))+nums)

# print(x)


def shift_string(s, n):
    # Initialize an empty string to hold the shifted result
    shifted = ''
    # Loop through each character in the input string
    for char in s:
        # Check if the character is a letter
        if char.isalpha():
            # Convert the character to lowercase for easier indexing
            lower_char = char.lower()
            # Compute the index of the shifted character
            shifted_index = (ord(lower_char) - 97 + n) % 26 + 97
            # Convert the shifted index back to its corresponding letter
            shifted_char = chr(shifted_index)
            # Preserve the original case of the character
            if char.isupper():
                shifted_char = shifted_char.upper()
            # Append the shifted character to the result string
            shifted += shifted_char
        else:
            # If the character is not a letter, just append it to the result string
            shifted += char
    # Return the final shifted string
    return shifted

# Example usage:
s = 'algo123'
n = 1
shifted = shift_string(s, n)
print(shifted)  # Outputs "bmhp123"

s = 'axy'
n = 3
shifted = shift_string(s, n)
print(shifted)  # Outputs "dab"
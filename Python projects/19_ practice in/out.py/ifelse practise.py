# #1.write a python program to find maximum between two numbers


# a=int(input('enter a no')) 
# b=int(input("enter another no"))
# if a>b:
#     print("a is maximum value")
# else:
#     print("b is maximum ")


# #2.write a python program to find maximum betweeen  three no


# a=int(input("enter a no"))
# b=int(input("enter another no"))
# c=int(input("enter a no"))
# if a>b and a>c:              #note:and means when both are correct only gives true 
#     print("a is greater")
# if b>a and b>c:
#     print("b is greater")
# if c>a and c>b:
#     print("c is greater")
# else:
#     print("all values are equal")  #a=b=c condition




# #3.write  a program to check given no is -ve,+ve, or zero

# a=int(input("please enter a no"))
# if a>0:
#     print("the given no is positive")
# elif a<0:
#     print("the given no is negative")

# else:
#     print("the given no is zero")




# #4.write a program to check wheather the given no is divisible by 5,11, or not

# no=int(input("please enter the no"))
# if (no%5==0)  or (no%11==0):           #or means if one condition,both is true gives true 
#     print("the no is divisible by 5,11")

# else:
#     print("the no is not div by 5,11")



# #5.write a program  to check the given no is even or odd

# no=int(input("please enter a no"))
# if(no%2==0):
#     print("the given no is even")
# else:
#     print("the given no is odd")


#6.write a program to check wheather the given no is leap year or not



#this are the steps need to follow to check leap or not 

# year=int(input("please enter the year bhai"))
# if (year%400==0):    #since checking for the decade so divided with 400  every 4 yrs is leap yr so decade means 100 *4=400
#     print("leap year") #if this fails checks for down condition 
# elif(year%4==0 and year%100!=0):  #check for 4 yr , and it shoud not a decade yr
#     print("leap year")
# else:
#     print("it is not an leap year bhai")


# #7. write a program to check wheather the character is alphabet or not


# character=str(input("please enter the character"))

# if (character>='a' and character<='z'):   #note : never forget this "" quotes
#     print("it is an alphabet")
# elif(character>='A' and character<='Z'):   #note : never forget this "" quotes
#     print(("it is an alphabet"))
# else:
#     print('it is not an  alphabet')


# #8.program to check given letter is a vowel or consonant

# ch=(input("please enter the letter"))
# if (ch=='a'  or ch=='A' or ch=='e'or ch=='E' or ch=='i'or ch=='I' or ch=='o' or ch=='O'  or ch=='u' or ch=='U'):
#     print("it is a vowel letter ")
# else:
# #     print("it is a consonant")



# #9.program to check input is a alphabet, digit, or a special character

# box=(input("enter something")) #here every thing is taken as string 
# if(box>='a'and box<='z') or (box>='a'and box<='z'): 
#     print("it is a alphabet")
# elif(box>='0'and box <='9'): #note : here also '' is very imp
#     print("it is a digit")
# else:
#     print("it is a special character")




# #10. program to check the character is upper case or lower case

# ch=input("please enter a character bhai")
# if (ch>="a" and ch<="z" ):
#     print("it is lowercase")
# elif(ch>='A' and ch<='Z'):
#     print("it is uppercase")
# else:
#     print("it is not a alphabet")

# #11.program to input week no and enter week day


# weekday=int(input("please enter the week day"))
# if weekday==1:
#     print("sunday")
# elif weekday==2:
#     print("monday")
# elif weekday==3:
#     print("tuesday")
# elif weekday==4:
#     print("wednesday")
# elif weekday==5:
#     print("thursday")
# elif weekday==6:
#     print("friday")
# elif weekday==7:
#     print("saturday")



# #12.program to input month no and print no of days in that month

# month=int(input("please enter the month no "))
# if month==1:
#     print("it has 30 days january")

# elif month==2:
#     print("it has 29/28 days febraury")
# if month==3:
#     print("it has 30 days march")
# if month==4:
#     print("it has 30 days april")
# if month==5:
#     print("it has 30 days may")
# if month==6:
#     print("it has 30 days june")
# if month==7:
#     print("it has 30 days july")
# if month==8:
#     print("it has 30 days august")
# if month==9:
#     print("it has 30 days september")
# if month==10:
#     print("it has 30 days october")
# if month==11:
#     print("it has 30 days november")
# if month==12:
#     print("it has 30 days december")



# #14.input the angles of triangle and check it is valid or not

# a=float(input("enter the angle of triangle"))
# b=float(input("enter the angle of triangle"))
# c=float(input("enter the angle of triangle"))


# total=a+b+c   #since the sum of angles of a triangle shoud be 180 degrees
# if total==180:
#     print("the given triangle is valid")
# else:
#     print("the given triangle is not a valid ")




# #15.input all  the sides of a triangle and check wheather it is valid or not


# a=float(input("please enter the side of a triangle"))
# b=float(input("please enter the another side of a triangle"))
# c=float(input("please enter the another side of a triangle"))

# if a+b>=c and a+c>=b and b+c>=a :  #it is the condition for sides valid or not
#     print("it is a valid triangle ")
# else:
#     print("it is valid triagle")
    

#16.program to check wheather  the given triangle   sides is equilateral , isosceles, or scalene

# #equilateral triangle:3 equal sides
# #isosles triangle: if any 2 sides are equal it is called as isosles
# #scalen triangle: not any of the sides are equal
# a=float(input("please enter the side of triangle"))
# b=float(input("please enter the side of a triangle"))
# c=float(input("please enter the side of a triangle"))
# if a==b==c:
#     print("it is an equilateral triangle")
# elif a==b or b==c or c==a:
#     print("it is an isosles triangle")
# else:
#     print("it is an scalen triangle")



#17.program to find all roots of a quadratic equation


#import complex math module

import cmath

a=float(input("please enter the values"))
b=float(input("please enter the value"))
c=float(input("please enter the value"))


d=((b**2 )-(4*a*c))


# #find two solutions

# sol1=(-b+cmath.sqrt(d))/(2*a)


# sol2=(-b-cmath.sqrt(d))/(2*a)


# print(sol1,sol2)

# print("the solution are {0} and{1}".format(sol1,sol2))









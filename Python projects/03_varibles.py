from re import S


x=2 #it is called as assigning a value to a  variable vv imp
print(x+3) #since previously we have assigned x as 2 so we get ans as 5,
#here x is called variable
y=8
print(x+y) #the ans is 10 since we have assigned x as 2 ,it takes only assigned values
x=9
print(x+y)  # ans is 9+8 since previously x is updated as 9;takes only updated value

#strings  ......................
name = 'youtube'
print(name)
print(name+    "  " "karunakar")  #this double quote space is just for "space",
#we can concate like this also
print(name[0]) #here in order to find index value we use square braces 
#here indexing starts fron 0,1,2,3,....
print(name[-2]) #here inorder to find index from right side we simply use negative no
#here index starts from -1,-2,......

#if u want two or more or multiple follow this
name='youtube'
print(name[0:3]) #here it gives "you" 
#note it gives 0,1,2 only 3 is not included ,and must give in square braces

 
name ='youtube'
print(name[  :4]) #here it gives yout because starting is not mentioned and end is
#given as 4 so it stops at index 3
print(name[1: ]) #here it gives otube because starting index is 1 , end is not given
print(name[3:15])  #here it wont give error as like integer simply it starts at t i.e 3 and goes on....

#note : in strings except len  it is 1,2,3,...everthing starts with 0,1,2,..... 
myname='karunakar rao'
print(len(myname))  #the ans is 13, here index starts fron 1,2,3.... 
#here it counts space also, len() is used to find length of the string


#in this strings cant be changed as like integer ,
#hence strings in python are imutable or changed vv imp
print(r'telusko \n rocks') # since r means astise or raw string  .it will ignore \n 
#i.e newline 
#and print astise


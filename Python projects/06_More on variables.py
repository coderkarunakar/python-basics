#num=5.8  here a number is assigned to a variable
#x=id(num)  in order to find address of it use id()
#print(x)  

#we can check for string and float also
#box=("karunakar")
#y=id(box)
#print(y)

# if we fetch a variable from another variable we get same address
a=10
b=a
print(a)
print(b)
x=id(a)
print(x)
y=id(b)
print(y)
PI=3.14
Z=type(PI)
print(Z)
s="karunakar"
t=type(s)
print(t)
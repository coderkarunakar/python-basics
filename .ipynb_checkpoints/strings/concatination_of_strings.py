                            #CONCATION OF STRINGS..
#Note:we need to use the + operator in string ...in order to add two strings..

#case 1:
# c="red"+"blue"
# print(c)

# #case 2:
# d="orange"
# d=d+"white"
# print(d)

#case 3:we can give multiple strings in concatination...

# e="ram"
# e=e+"babu"+"alias"
# print(e)


# #Note:we can use += operator as well,even this makes string concationation...
#this is the shortcut for concatination...
# f="ravi"
# f+="raghu"
# print(f)

#Note:strigs are immutable...as like variables...



# #Note:in this case the id also get changed and refers to new reference 
# #Note:we can use multiply operator as well
# z="karunkar"
# z=z*3  #this makes to print the string into 3 times...
# print(z)
# print(z*3)  #this line makes the z (i.e previous 3 times string into again into 3 times this gives us 9 times)  just try to run it and check once if u want..it ...



#NOTE:python doesn't know how to add integer and a number it gives u the error 
# let's see a=print("raghu"+3) this line will give an error,this gives concatination error str and int can't be added...python doesn't know how to add a word and a number..    


#but if u want to do this string and integer it is not possible but we can use inbuilt function called str()

a="karunakar"
a=a+str(3)  #like this we can convert integer to string and make it concatinate...
print(a)
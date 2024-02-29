#FOR THIS INBUILT FUNCTIONS WE NEED TO STORE IT IN SOME VARIABLE THEN ONLY WE CAN GET THE ACTUAL OUTPUT...

# #we have inbuilt string functions on python...

# # 1.split()
# #note:if we don't give anything it automatically splits on the basis of space...
# #it actually returns a list of  strings..
# #this gives u in terms of list only...

# #CASE 1:

# k="My name is Karunakar"   #here if we give ,s then it wont print anything since here then there would be no space only ,s so it can't split , if u give nothing (by default it takes only white spaces...)
# li=k.split()
# print(li)

# m="my name is anu "
# print(m.split())

# r="hello, mastaru, em chestunav ra"
# print(r.split(','))


# #CASE 2: WE CAN GIVE HOW MANY ITEMS U WANT TO SPLIT AS WELL AND IF U GIVE LIKE 1 IT SPLITS 2 AND IF U GIVE LIKE 2 IT SPLITS 3 ARGUMENTS I.E IT SPLITS NO OF ARGUMENTS U PASS THAT +1


# g="hello,ra, mahesh , babu ,ela , unnav"
# print(g.split(',',2))  #here we gave 2 so it splits 3 so total u will be able to 3 strings..


# #case 3: using replace()
# s="my name is karunakar"
# s.replace("karunakar","rohan")
# print(s)   #this wont change anything..since we are not storing it in anything..

#case 4:
# s="my name is raghu"
# st=s.replace("raghu","ram")  #this gives u the change since it has stored the variable in the some new variable that makes u the replace..and be carefull we need to give astise the name in the string no white spaces as well please look it carefully..
# print(st)

# # NOTE:if we try to replace which is not present in our code then it wont change anything and wont give any error also
# s="ram raghu both are friends"
# k=s.replace('mahesh','babu')
# print(k)  #in this case we gave mahesh which is not in the given string and we are trying to replace it with something but in this it just prints what is actually present in our code that's it ..and replace wont work in this case ..

#case 5:
# j="my name is karunakar karunakar karunakar"
# j=j.replace("karunakar","anu")
# print(j)  #in this case it tries to replace the all karunakar characters with what we gave in the replace...

# #case 6:
# j="my name is karunakar karunakar karunakar"
# j=j.replace("karunakar","anu",2)
# print(j)  #in this case we can replace a specific number like we gave here as 2 so only 2 characters with that name get's changed... look output.. if u give means it replaces first 2 characters...



                            # FIND FUNCTION....
#FIND MEANS U WANT TO FIND SOMETHING IN THE STRING (IT ACTUALLY FINDS THE SUBSTRING IN  THE STRING ..) IT ACTUALLY RETURN THE INDEX OF THE STRING ..
#case 7:

# m="my name is karunakar"
# index=m.find("na")
# # print(index) #this gives output as 3 since this n is getting started from index 3 since it also counts the white space as well so it gave 3 only it gives what ever the first it catches...

# #case8:
# m="my name is karunakar"
# index=m.find("nae")
# print(index) #it gives output as -1 since this substring is not present in our string so it gave automatically -1   note:index starts from 0,1,2,3,,4,5,.....

# #case 9:
# m="my name is karunakar karunakar karunakar karunakar"
# index=m.find("kar")
# print(index)   #this output is 11 since index starts with 0,1,2,3...and it checks the first who comes..so here it checked the first kar which is located at 11 th index ,and index starts from the 0,1,2,3,......

#case 10:  we can specify in the given range also... like this

# m="my name is karunakar karunakar karunakar karunakar"
# index=m.find("kar",16,20)  #here we gave 21 since the next character is getting started with index no 21..the first is getting started with index 11 it has to touch the next character if we have multiple similar characters like this.. here it is not touching the 2nd character it is touching only the first character last alphabet 'kar' note it .and one thing it stops till end -1 what we specify only remember ..
# print(index)




                #LOWER AND UPPER FUNCTION....
#case 11:
#note:we need to store in some variable else we wont  get the actual expected output


# str="My Name is Karunakar"
# str=str.lower()
# print(str)  #in the output we will be able to seee that what ever the caps we gave here that get converted to caps...

# #upper this converts string into upper form...


# str="My Name is Karunakar"
# str=str.upper()
# print(str)  #this makes our whole string into upper case...


#starts with function....(wheather this string starts with this substring..) this actually return true or false...

# #case 12:
# str="My Name is Karunakar"
# ans=str.startswith( "My Na")
# print(ans)   #this gives output as (true) since it is getting starts with My Na

# # another case in this false let's seee

# #case 12:
# str="My Name is Karunakar"
# ans=str.startswith( "My Nae")
# print(ans) #this gives false since here it is not getting started with Nae here e is not present so this give false indication as our output...


# #another approach of the above one...using a specific range of numbers..
# #case 12:
# str="My Name is Karunakar"
# ans=str.startswith( "My Nae" ,11,25) 
# print(ans) #this gives false since here it is not getting started with Nae here e is not present so this give false indication as our output... this gives false since the given character is not present in that range of index..it also ignore the last no and it starts with index no as 0,1,2, 3,.......



#case 13:
str="My Name is Parikh"
ans=str.startswith( "Pa",11,25) 
print(ans) #this gives output as true since the given character exist in that specific range ,note:we can give a specific range or by default it takes the starting from 0 index to end of the string ...

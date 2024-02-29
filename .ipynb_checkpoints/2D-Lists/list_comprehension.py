# #NOTE:LIST COMPREHENSION IS THE MOST POWERFULL TOOL WHICH IS USED IN 2D LISTS AND OTHERS AS WELL..THIS CONCEPT IS VERY VERY IMPORTANT ONE ,IT IS JUST LIKE SHORTCUT WE CAN REDUCE THE NO OF LINES OF CODE  FOR CLEARING THE CODING ROUNDS WE WILL USE THIS...

# #QUESTION :SQUARE OF NUMBER USING THE NORMAL WAY AND LIST _COMPREHENSION..

# #normal way 

# #our normal list
# li=[2,3,4]
# #creating the new list for  storing all the squares of a list 
# li_new=[]

# #for iterating on each element of the list ..
# for ele in li:
#     #after iterating applying logic+appending in the new list 
#     li_new.append(ele**2)
#     #finally printing the our new list..
# print(li_new)


# #using the list comprehension method..


# #SYNTAX FOR LIST COMPREHENSION IS [MAIN OUTPUT LOGIC FOR EXPRESSION   CONDITION ]  HERE CONDITION IS OPTIONAL.... HERE THESE LOGIC IS WRITEEN IN THE SQUARE BRACKETS AND SO THAT IT CREATED AN EMPTY LIST  AS WELL  FOR THIS QUESTION... THIS IS DONE ONLLY IN SINGLE LINE..

# #HERE CONDITIION IS NOT TOOK IT IS OPTIONAL WE CAN LEAVE IT ALSO ...
# li=[4,3,2,1]
# li_new=[ele**2 for ele in li]
# print(li_new)


#                                 #WITH CONDITION 
#we can have multiple for loops as well as like multiple conditions..
# Note: we can use infinity number of conditions remember...
# #if we want to print the only even numbers then we can also do that by giving the condition

# # QUESTION PRINT ONLY THE SQUARE OF EVEN NUMBERS IN THE GIVEN LIST ,THIS PRINTS ONLY THE EVEN NO OF THE LIST ...
# li=[1,2,3,4,5,6,7,8,9,10]
# li_new1=[ele**2 for ele in li  if ele%2==0]
# print(li_new1)

# #USING THE NORMAL LIST 
# li=[1,2,3,4,5,6,7,8,9,10]
# li_new=[]
# for ele in li:
#     if ele%2==0:
#     #after iterating applying logic+appending in the new list 
#         li_new.append(ele**2)
#     #finally printing the our new list..
# print(li_new)



# #print the multiples of 2 and 3 

# li=[1,2,3,4,5,6,7,8,9,10]
# li_new=[]
# for ele in li:
#     if ele%2==0:
#         if ele%3==0:
#             li_new.append(ele)
# print(li_new) #this gives output as [6]

# # using the list comprehension method

# li_new=[ele for ele in li if ele%2==0 if ele%3==0]  #here taking that element..
# print (li_new)


#finding the common element in the 2 lists
#using the normal approach..


# li_1=[1,2,3,4,5]
# li_2=[2,4,5,6,8]
# li_new=[]
# for ele1 in li_1:
#     for ele2 in li_2:
#         if ele1==ele2:
#             li_new.append(ele1)  #here we can append ele1 or ele2 since both are same...

# print(li_new)


#                 #USING THE MULTIPLE FOR LOOPS
# li_1=[1,2,3,4,5]
# li_2=[2,4,5,6,8]

# li_new=[ele1 for ele1 in li_1 for ele2 in li_2 if ele1==ele2]
# print(li_new)



#IF ELSE CONDITION ...
#QUESTION IF IT  IS A MULTIPLE  OF 2 THEN TAKE  IT AS A SQUARE ELSE TAKE THAT NUMBER ASTISE..

#NOTE :tHIS IS VERY VERY TRICKY ...LOOK IT VERY CAREFULLY 

# li=[1,2,3,4,5]

# #here only if else condition only used we can use like this also only if else
# # if that element is multiple of 2 then square it else print that no astise
# li_new=[ele**2 if ele%2==0 else ele for ele in li]
# print(li_new)


#we can generate a each  character in a list...
# a='karunakar'
# li=[ele for ele in a]
# print(li)


# #string in a list.. of character times..
# a='karunakar'
# li=[a for ele in a]
# print(li)



#we can generate a list of list as well i.e 2d list..
li=['parikh','rohan','ankush']
li_2d=[[s for s in ele]for ele in li]
print(li_2d) #once check the output we will get the list in list as the output ..here (ele is iterating through li )and (s is iterating through the ele ) and finally printing the iterating values of s we get list in list as the output..

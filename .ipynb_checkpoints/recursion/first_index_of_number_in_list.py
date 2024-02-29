
# #                                 #FIRST INDEX OF A NUMBER IN A ARRAY 


# # #once pls look at our class notes as well...
# # def firstindex(a,x):
# #     l=len(a)

# #     #base case if the list is empty return -1 since no elements
# #     if l==0:
# #         return -1
# #     #if the elements found at index 0 only then return 0 since the element is found at index 0 only
# #     if a[0]==x:
# #         return 0
    
# #     #if the element is not found at index 0 then copy those elements into the smalloutput list 
# #     smallerlist=a[1:]

# #     #continously call the function untill all the elements become empty and 
# #     smallerlistoutput=firstindex(smallerlist,x)

# #by the above conditions if the elements are -1 then return -1 else return +1 to the found index...and keep  goes on till the starting  indexi.e till 0
# #     if smallerlistoutput==-1:
# #         return -1
    
# #     #if the element is found then return that found index of smallerlist +1  ,this recursion keeps going on and return correct index of searching element
# #     else:
# #         return smallerlistoutput+1

# # a=[1,2,5,6,7,9]
# # print(firstindex(a,7))




# #2nd approach using start index..

# #si means start index 
# def firstindexbetter(a,x,si):
#     l=len(a)
    
#     #base case if startindex==length then element will not be found thern return -1
#     if si==l:
#         return -1
    
#     #if the start index is equal to our searching element then return that startindex element simply ..
#     if a[si]==x:
#         return si

#     smallerlistoutput=firstindexbetter(a,x,si+1)  #this line keeps on calling the fucnction recursion and si keeps on increasing untill value get found or our basecase get executed..
#     return smallerlistoutput  #this keeps simply runs the recursion untill the condition is satified  and keeps on calling the function

# a=[1,2,3,4]
# print(firstindexbetter(a,3,0)) #here start index is given as 0 since it checks all the elements from the index 0



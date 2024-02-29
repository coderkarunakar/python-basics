# # #last index of a number..

# # #1st approach using copying the elements...



# #please look at the class notes and look at the dry run .. then only u can understand it is little tricky but easy to grasp
# # #here a means an array and x means searching element 
# # def lastindex_of_no(a,x): 
# #     #base case if no element  means in the list then return -1 since no elements of searching element
# #     l=len(a)
# #     if l==0:
# #         return -1
# #     smalllist=a[1:]
# #     smalllistoutput=lastindex_of_no(smalllist,x)

# #     if smalllistoutput!=-1:
# #         return smalllistoutput+1
    
# #     else:
# #         if a[0]==x:
# #             return 0
# #         else:
# #             return -1
        
# # a=[1,2,2,4,5,7,8,2,0,8,3]
# # print(lastindex_of_no(a,2))


# #2nd approach..
# def lastindexb(a,x,si):
#     l=len(a)
#     if si==l:
#         return -1
#     #astise it iterates but for every iteration the si value (start index value ) get's increased.. and note anyhow it need to get -1 after that only our actual logic starts
#     smallerlistoutput=lastindexb(a,x,si+1)

#     if smallerlistoutput!=-1:
#         return smallerlistoutput
#     else:
#         if a[si]==x:
#             return si
#         else:
#             return -1
        
# a=[1,4,2,,,4,6,8,0]
# print(lastindexb(a,4,0))



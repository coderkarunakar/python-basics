


#                                 #largest column sum in 2d list


# #this is for iterating vertically..
# #once pls look at class notes as well for better understanding 
# #the condition is the no of columns will be same in every row..

# # def lar_col_sum(li):
# #     #note :len(li) is no of rows since no of columns in every row is same as per our condition zand len(li[0]) is the no of columns
# #     n=len(li)  #no of rows
# #     m=len(li[0]) #is the no of columns

# # #every time we try to iterate horizontally but for largest sum we need to iterate vertically 
# # #first we need to add all  of these single column and there will be of some sum and store some max call index if any call sum becomes greater than the current sum then we need to update that sum and updadte the index as well
# #     for  j in range(m):  #going to each column  
# #         sum=0#initially sum will be 0 in order to add all those
# #         max_col_index=-1 #because index cannot be -1
# #         max_sum=-1 #initially keeping it as negative
# #         for i in range(n):#through each column i need to iterate on row
# #             sum+=li[i][j]

# #         if sum>max_sum:
# #             max_col_index=j
# #             max_sum=sum

# #     return max_sum,max_col_index
# # li=[[1,2,3,4],[8,7,6,5],[9,10,11,12]]
# # #we need the largest of the sum..
# # lar_sum,lar_cal_index=lar_col_sum(li)
# # print (lar_sum,lar_cal_index)


# #in output we will get output as largest sum and it's index no


# #2nd approach
# def lar_col_sum(li):
#     #note :len(li) is no of rows since no of columns in every row is same as per our condition zand len(li[0]) is the no of columns
#     n=len(li)  #no of rows
#     m=len(li[0]) #is the no of columns

# #every time we try to iterate horizontally but for largest sum we need to iterate vertically 
# #first we need to add all  of these single column and there will be of some sum and store some max call index if any call sum becomes greater than the current sum then we need to update that sum and updadte the index as well
#     for  j in range(m):  #going to each column  
#         sum=0#initially sum will be 0 in order to add all those
#         max_col_index=-1 #because index cannot be -1
#         max_sum=-1 #initially keeping it as negative
#         for ele in li:#through each column i need to iterate on row  for every column we need to go for each row
#             sum+=ele[j]  #for each row i need the j th column no for 0column i need all the columns of j the column

#         if sum>max_sum:
#             max_col_index=j
#             max_sum=sum

#     return max_sum,max_col_index
# li=[[1,2,3,4],[8,7,6,5],[9,10,11,12]]
# #we need the largest of the sum..
# lar_sum,lar_cal_index=lar_col_sum(li)
# print (lar_sum,lar_cal_index)

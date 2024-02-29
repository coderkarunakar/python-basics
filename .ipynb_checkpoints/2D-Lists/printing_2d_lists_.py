                            #PRINTTING THE ELEMENTS OF THE 2D LISTS
#HERE WE WILL BE SEEING HOW CAN WE ITERATE ON 2D LIST AND TRY TO PRINT THE ELEMENTS OF THE 2D LIST

# #case 1
# li=[[1,2,3,4],[5,6,7,8,],[9,10,11,12]]

# n=3 #since rows =3 
# m=4 # since columns =4

# #simple way of printing the elements of 2d list
# for i in range(n):
#     for j in range(m):
#         print(li[i][j],end=' ')  #this gives space seperated input in the same line but if u want a single row then print() since this i,j is printing the single row

# #     print('')  #this makes to print in next line after every iteration since i,j is printing each row and column

    
#THIS CONCEPT IS VVIMP MOST OF THE TIMES WE WILL BE USING THIS CONCEPT..
# #case 2:
# #if the column size is not fix then we can use this method

# li=[[1,2,3,4],[5,6,7],[8,9]]
# for row in li:
#     for ele in row:
#         print(ele,end=' ')
#     print()
#     #for the above 2d list the column size is not fix so we can print this as well using simple above loop  



                #JOIN PLEASE LOOK CLASS WORK AS WELL FOR BETTER UNDERSTANDING...

#RULE:IT NEED ELEMENTS TO BE FINE..

#there is a concept called join it tries to add or join the elements all except the last element..
#SINCE CONCATINATION OF 2STRINGS IS POSSIBLE BUT CONCATINATION OF INT AND STRING IS NOT POSSIBLE

# #JOINING  A STRING
# li='ab'.join('abcd')
# print(li)  #the output will be aabbabcabd for the last element the given string wont be added

# #JOINING A LIST AND ITS ELEMENTS SHOULD BE STRING 

# li='abc'.join(['1','2','3'])
# print(li)  #output is 1abc2abc3abc




# #printing using join operation..
# li=[[1,2,3,4],[5,6,7],[8,9]]
# n=3  #since row size is 3
# for row in li:
#     output =' '.join([str(ele) for ele in row])
#     print(output)  #after every row we need to go to the next line so we have used this print..

                                            #EXPLAINATION...
#here row iterates on li
#with empty space it is joining and when it reaches to end of the row it wont apply any space since join concept
# here we make ele as a string since join only works on string and ele iterates on row..

print('a')
print()
print('c')
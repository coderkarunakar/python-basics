                                    #2D LIST USER INPUT..

# #input for the 2d list..;

#here no need of  m but simply we are giving..as to get like our m*n 
# #here taking string as a input and accordingly we are able split that and we are able to take input..based on n ,m and   we cannot exceed the n rows we give automatically it stops
# str=input().split()
# n,m=int(str[0]),int(str[1])
# li=[[int (j) for j in input().split()]for i in range(n)] #here n means rows..and m means colulmn 
# print(li)
# #NOTE:in the above list we can take any no of columns and (rows are mandatory )since we mentioned range of n ..


# #example: 2 2
# 1 2
# 12 2 
# output [[1,2],[12,2]]




                                    #JAGGED LIST USER INPUT..
#jagged list is the case where no of columns is not mentioned..
# #jagged list is taken as input no need to take input as columns  because in 2d list  there is no need of m in the input taking side so we can skip it and make it as jagged list..as well
# n=int(input())
# li=[[int (j) for j in input().split()]for i in range(n)]
# # print(li)


# str=input().split()
# n,m=int(str[0]),int(str[1])
# b=input().split()
# arr=[[int(b  [m*i+j] )for j in range(m)] for i in range(n)] # range of n means no of rows we need to take and getting no of list elements from the m .if we get i and j then we will be knowing that if we get i and j then we will be knowing that our element is present at b(m*i+j) position and since it is a string we are converting it to integer part.
# print(arr)

#here in this case we need to give only one space and how many n m (i.e row and column we specify that many only we need to take if we try to take extra or tryto  give more than one space we get error ) 
#here after mentioning m n in the next line simply we need to enter the numbers in a single line and based on m n it will take the 2d list this is also a different type  of 2d list user input taking


# ex: 2 2
# 1 2 3 5
# output [[1,2],[3,5]]



#next format of 2d list is m,n and all elements in a single line example
# 3 3 1 2 3 1 2 3 here first 2(i.e0,1 ) elements are m,n and remaining are the elements of the list
str=input().split()
n,m =int(str[0]),int(str[1])
b=str[2:]  #this since we need to start taking elements from the index 2 actuall elements..
arr=[[int (b[m*i+j]) for j in range(m)] for i in range (n)]
print(arr)

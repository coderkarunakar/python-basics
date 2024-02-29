#JAGGED LISTS ARE THE 2d LISTS IN WHICH THERE WILL BE DIFFERENT IN COLUMN SIZE

# 1st row
li=[[1,2,3,4],[5,6,7],[8,9],[10,11]]
print(li[0][3])

# 2nd row
# print(li[1][3])  #this is out of  range since it does not have column index of 3 
print(li[1][2])  #this is valid since it has column of index 2


#3rd row
# print(li[2][2])  #this is list out of  range since it is different in column size(i.e it does not has the column index 2)
print(li[2][1]) #this is valid since it has index row ,column


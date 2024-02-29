# # l=[1,2,3]
# # print(sum(l))  #using sum inbuilt function also we can find sum of elements of an list


# #sum of array elements using recursion function

# def array_sum(k):
    
#     if len(k)==0:#this is the base case if the length of the function is zero the return 0
#         return 0
#     else:
#         return k[0]+array_sum(k[1::])  #here every single list element is taken and put aside untill it completes all the elements of the given list and after completed (i.e length of the array is zero then ti finally sums up all and then return lifo (i.e last in first out ..))

# l=[22,33,444,555]
# sum=array_sum(l)
# print("the array sum is",sum)





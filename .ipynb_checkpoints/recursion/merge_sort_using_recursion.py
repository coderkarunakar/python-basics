
#                                             #merge sort using recursion 

# def merge(a1,a2,a):
#     i=0
#     j=0
#     k=0

#     #below both conditions has to be satisfied
#     while i<len(a1) and j<len(a2):  #here we have used less than len(a1,a2 ) since i,j is started with 0 and len function starts with 1....
#         #if  the first index element is smaller than 2nd element then do this 
#         if (a1[i]<a2[j]):
#             #that small element which is in the a1[i] is stored in the a[k] 
#             a[k]=a1[i]
#             #and the k which is for the actuall list is keep going on incresing
#             k=k+1
#             #and our i th which is for the a1 list index also keep going on increasing..
#             i=i+1  #since we have used i so we  have to move only i
        
#         #if a1 list first index is big no then the a2 list index then this works..    
#         else:
# #that a2 number is being stored in the a[k] 
#             a[k]=a2[j]
#             #and that k is keep going increasing 
#             k=k+1
#             #and j also keep going increasing since this j  is for indexing of list 2 
#             j=j+1


#     #the above if else works till the one complete list get becomes empty.. then it get stoped..because if one list was completed then we wont be having any two elements inorder to compare..,and the rest remaining elements get copied in the actual list.


# #if the elements of the first list get completed then rest which is in the list of j that get copied in the actual list..
#     while i<len(a1):
#         a[k]=a1[i]
#         k=k+1
#         i=i+1
#     while j<len(a2):
#         a[k]=a2[j]
#         k=k+1
#         j=j+1

# #NOTE:here we are assuming that inorder to store a1,a2 elements in a we have enough space in it ..



# def merge_sort(a):  #a means an array
#  #base case.. if the length is empty i.e 0 or only 1 element then return nothing ,or means any of this works fine..
#     if len(a)==0  or len(a)==1:   
#         return 
        
#     #first find the mid point with an integer division
#     mid=len(a)//2
#     #when i say mid it actually copies upto mid,and this below lines is for moving right and left from the mid
#     #from mid to the left..
#     a1=a[0:mid]
#     #from mid to the end i.e right side
#     a2=a[mid:]



# #calling our function on both a1,a2
#     merge_sort(a1)
#     merge_sort(a2)

#     #merging the two sorted arrays and making them into the original array.. we have,by calling another function.
#     merge(a1,a2,a)

# a=[10,5,3,1,7,9,4]
# merge_sort(a)
# print(a)

# #for dry run please look at the class notes..


# #small question from flm channel
# x=5 if float(10+10) == 20 else 0
# y=[1,2]+[x]
# z=y[::-1][-3]
# print(z)


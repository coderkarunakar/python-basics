#         # INTRO TO STRINGS....

# #case1:
# #NOTE:we can use single or double or triple quotes in strings both works fine...
# s="karunakar"
# print(s)
# s1='chembeti'
# print(s1)

# #the advantage of using the triple quotes are we can use multiple lines..which doesnot support for the single and double quotes ..
# s2=''' rao'''
# print(s2)

#case 2:
# same as lists here also indexing is there
s3='karunakar'
# print(s3[0])
# print(s3[1])
# print(s3[2])
# print(s3[3])
# print(s3[4])
# print(s3[5])

#Note:if u try to  give more index which is not in the string index then it would give u the index out  of range error

# #case3:same as positive indexing negative indexing is also there in this string concept
# print(s3[-1])
# print(s3[-2])
# print(s3[-3])
# print(s3[-4])
# print(s3[-5])
# #here also same if we try to give index out of range like which is not in the list then it would give error

#case 4:but in this case if we try to print (i.e in the multiline string(i.e thriple quotes)) for first line index it fetches and from 2nd line it wont show anything..
s4='''my  
name is
karunakar
hello 
mama'''
print(s4[3])
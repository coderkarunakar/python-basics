#creating a  empty list 
# empty=[]
# print(type(empty))
# L=[1,2,'karan',7.9,True,'karan']
# print(type(L))
# print((L))



# #creating a list with a list function list()
# L=list()
# print(type(L))





# nums=[1,2,3,55,6]  #this square braces are used to define list
# print(nums)  # we get   output as [1,2,3,55,6] 
# # here aslo we can find index value  , index starts with 1,2,3,...

# print(nums[0])  #we get output as 1
# print(nums[4])   #we get output as 6
# print(nums[1:4]) #always stops less than 1 value what we give at end
# print(nums[ :4])  #in this case prints from starting to end but less than 1
# print(nums[2: ]) #in this case it prints from index 2 to end since end not mentioned
# print(nums[-1])  # in this case we get from right side
# # strings in lists
# names =['karunakar','anusha','tharanya','friends']
# print(names) # [] quotes and commas are important 
# #in this it can have both integers and strings lets see
# values =[6.7,'tharanya','anusha']
# print(values)

# #creating new variable and fetching previous what we gave
# milap=[values,names]
# print (milap)  #here we get values and names what we assigned
# box=[10,23,5,4]


# print(box.insert(1,98))
# print(box)
# print(box.append(98))
# print(box)
# print(box.clear())
# print(box)
# #just like this we can print remove ,pop,del,extend,min,max,sum,sort....etc


#imp methods in list()
#sorting in strings in low to high

# L=['aman','rakesh','bhavi','carn']
# L.sort()
# print(L)


#sorting high to low i.e descending order
# l=[1,2,3,9,8]
# l.sort(reverse=True)
# print(l)



#reverse method to reverse a list

# d=[1,2,3,4,5,0,9,8,7,6]
# d.reverse()
# print(d)


#list inside a list

# k=['karan','ram',[1,0,9,8,7,6,['karan',[1,0,9,8,7]]]]
# print(type(k))
# print(k)


#List comprehension
# box=['altaf','aman','kundan','priya','ashok']
# a=[ word for word in box if word.startswith('a')]
# print(a)


#copying a list into another list
# k=['karan','tharanya','anusha','TRIVENI']
# L=k.copy()
# print(L)


#another method for copying list()
# k=['karan','tharanya','anusha','TRIVENI']
# L=k[:]  #it means start index at 0 and go till end and store it
# print(L)


#list unpacking
k=['karan','shamir']  #here k consist of 2 variables
m,n=k #k variable each one is assigned to each 
print(m)  # m as 'karan' 
print(n)   #n as 'shamir'

#Note : in this list unpacking 'k' variable should equal to k assign variable m,n 
#in this case 2 , 2 is used so matched else error might occur
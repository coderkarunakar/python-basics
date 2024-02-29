book=(1,2,3,3)
print(book) # this is  called as tuple ,it is represented as open braces()
#it is faster than list, here values cant be changed
#it has the following methods
print(book.count(3)) #it will count repeating of a no
print(book.index(3))# it will show the index of a no
box=(1,2,3)
print(book.__add__(box)) # it will add two tuples


#sets
combox={1,3,2,4,4,9,9} #this curly braces is set 
print(combox) #in this the sequence will be different if we print it .
print(combox.add(3))
print(combox)#even it do have certain operations like list,tuple...
#quiz:
nums=[25,36,95,14,12,26]
del nums[-4:-1]
print(nums)
#using pop method we can do only once
#print(nums.pop(2))
 #print(nums.pop(3))
#print(nums.pop(4))
#print(nums)   #if we use like this we get error since pop can perform once .pop index out of range





#practise List  problems
twinkle=[5,4,3,2,1]

#sort
#twinkle.sort()
#print(twinkle)

#append
#twinkle.append(45)
#print(twinkle)

#clear
#twinkle.clear()
#print(twinkle)

#insert
#twinkle.insert(3,99)
#print(twinkle)
#remove
#twinkle.remove(2)
#print(twinkle)

#pop
#twinkle.pop(3)
#print(twinkle)
#del twinkle[1:3]
#print(twinkle)

#extend
#oppo=[1,2,3,4,5,6,7]
#twinkle.extend(oppo)
#print(twinkle)

#min
#x=min(twinkle)
#print(x)

#max
#x=max(twinkle)
#print(x)


#SUM
#x=sum(twinkle)
#print(x)


#sort
#twinkle.sort()
#print(twinkle)
#dictionary data type {}
#represented as curly braces {}


#creating a empty  dictionary
# k={}
# l=dict()# it is a dictionary function dict()
# print(type(k))
# print(type(l))

#creating some key value pairs in  dict()
# l={'user name':'karunakar','password':'learn code'}#here (,)and (: )is very imp
# print(type(l))


#here key must be unique (i.e no duplicate) but value can be duplicate
#value :key is the format

# l={'user name':'karunakar','password':'12','user name':'anu'}
# print(l)


#note:here indexing cant be performed but key can  be found by []braces
# l={'user name':'karunakar','password':'12','user name':'anu'}
# print(l['user name'])

# #pop  it is used to  remove an element
# k={"username":"chaitu","password":"rambabu"}
# print(k.pop('username'))
# print(k)

#to fetch variable we can use get method 
# k={"username":"chaitu","password":"rambabu"}
# print(k.get('username'))

# print(k.get('password'))


# #Note:it fetches only keys by defining variables
# # another method for fetching is using 3rd variable
# temp=k.get('chaitu')
# print(temp) #hence here we got none


# #Note :if  the data is not available in the dictionary then it wont give error it gives None
# # print(k.get('kaka'))
# # #note:instead of getting none we can  get another also by defining like this
# # print(k.get('kaka','not found')) 


# #to clear everthing just use .clear()  then we get output as none
# ch={"username":"chaitu","password":"rambabu"}
# m=ch.clear()
# print(m)  #output as none


# j={'mama':'kodal','atha':'alludu'}
# #to get  all values at one place use .values()
# print(j.values())
# #to get  all keys at one place use .keys()
# print(j.keys())
# #to get  both values ,keys , we can use items
# print(j.items())



#note:for running loop in dictionary do like this

from tkinter.tix import tixCommand


jr={'mama':'kodal','atha':'alludu'}

# print(jr.items())
# for key,values in jr.items():
#     print(key,values)

#     #to get something in bt the,,,,,,use sep=" "
#     print(key,values, sep=" * ")




#adding keys in dictionary
j={'mama':'kodal','atha':'alludu'}
j['age']=20
j['atha']=6788
print(j)
'''#strings
s="hello bosu am mama"
print(s[1])
'''


#reversing a string
'''k='tharanya'

print(k[::-1])  #this :: this is used for reversing
k='tharanya'
int(k[-1::-1])
'''

'''k='tharanya'
print(k[::])'''

import abc


j='anusha'
print(j[-2::])


# IN REVERSING ONLY TWO POINTS [::]
# HERE NOTE ONE THING LEFT SIDE MEANS  PRINTS ASTISE
#RIGHT SIDE MEANS PRINTS ONLY DIFFERENCE 


#REPLACEMENT OPERATOR  {} AND NEVER FORGET" f "at the beggining

#NOTE WE USE THIS {} OPERATOR WHEN EVER  WE WANT TO FORMATE THE STRING

channel_name="Learn coding"
message=f"PLEASE SUBSCRIBE TO OUR CHANNEL:{channel_name}"
print(message)

#IT PERFORMS +,-,*....OPERATIONS ALSO
print(f"the sum of 2 and 8 is {2+8}")


#if we keep   "r"    instead of f we data astise  even if we use some special characters like \n ...
#print(r"the sum of 2 and 8 is \n{2+8}")

#print(f"the sum of 2 and 8 is \n{2+8}") #here we get 10 in new line




  

#SPLIT METHOD :IT SPLITS SEVERAL PARTS BASED ON A "PATTERN" AND RETURN A STRING
'''s=('Learn coding is our channel name,all subscribers are gems!,i need your support ')
k=s.split(',')
print(k)
'''


#JOIN() IT IS USED TO JOIN STRING BASED ON PATTERN 
l=['"hello world","welcome to our channel","please do subscribe"']
print(','.join(l))

#find('pattern','start','end')  find the position of out pattern . if pattern  is not found then it will return -1
# info ='a quick brown fox jumps over the lazy dog '
# print(info.find('fox'))


#index('pattern',start','end')   :it is same as like find() but the only diff is there if pattern not found 
#returns -1 but here returns 'error'


#count('pattern'):returns no of occurance of a specified 'character'

# s=('my name is karunakar')
# print(s.count('a',5))


#strip() it is used to remove front and back spaces

# s=('            my name is karunakar                    ')
# print(s.strip())


#replace() it will replace our current data as new operators

# s=('my name is karunakar')
# print(s.replace('a','*'))

#changing case low to high or vise versa


#upper()
# s=('my nAme is karunakar')
# print(s.upper())

#lower()  makes small letters

s=('MY NAME IS KAUNAKAR')
print(s.lower())

#TITLE()  ut makes evert first word as capital lettter

# s=('my nAme is karunakar')
# print(s.title())

#capitalize()  it makes capital of 1st letter in the sentence

# s=('my nAme is karunakar')
# print(s.capitalize())

#isupper() it checks all letters are caps or not if even a single letter is small returns False else True

# islower() vvise versa for isupper()
#in isupper(),islower() space is accepted remaining not accepted


# s=('my nAme is karunakar')
# print(s.isupper())#checks for all caps or not if all caps means True else False


# s=('my nme is karunakar')
# print(s.islower())#checks for small letters

# s='mynameiskarunakar'
# print(s.isalpha()) # checks for all is alphabets(a-z)
# s=('            ')
# print(s.isspace())  #checks for all is space or not


# s=('mynAmeiskarunakar')
# print(s.isalnum()) #checks for numbers (a-z)(0-9)('there shoud be no space)


#range:sequence of numbers ex:1-10,anything   
#range(start,end,difference)

# var=range(10)
# print(var)
# print(type(var))

# v=range(10)
# for data in v:
#     print(data)


v=range(10,30,3)#start,end, difference
for data in v:
     print(data)

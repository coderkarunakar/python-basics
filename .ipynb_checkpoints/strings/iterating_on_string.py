#NOTE:we can use 2 types in iterating a string i.e 
#1.using a range in for loop i.e s="hello world" for i in range(len(s)):
#2.using a simple loop in like for i in s: like this we can use iteration in strings
#if we give like 2nd loop also it iterates through all the elements..it wont leave any..

#CASE 1
#Question :how many times l appears in the string..

#1st way of solving the question i.e 1st way of approach..this way works on each character of the string 
s="Hello World"

# count=0
# for letter in s:
#     if (letter=='l'):
#         count=count+1
# print(count)

#2nd way of solving the question i.e way of approach..,this works like using a [],i.e index...

# count=0
# for i in range(len(s)):
#     if(s[i]=='l'):  #since this is an range doing using range ,so  it is done using index that's why we are using [] brackets...
#         count=count+1
# print(count)



#CASE 2:
# in and notin operation...STRING...(IT CHECKS WHEATHER A SUBSTRING EXIST OR NOT..)
# SUBSTING MEANS STARTING FROM ANY INDEX AND A CONTINOUS PART OF THE STRING.. 

#EXAMPLE:
# str=HELLO

#THIS BELOW IS AN EXAMPLE OF AN SUBSTRING..BUT NOT ONE THING WE CANNOT SKIP ANY AND MOVE TO OTHER WE NEED TO GO IN A AN SEQUENCE ORDER ONLY..


#H          E           L           L       O
# HE        EL          LL          LO
# HEL       ELL         LLO
# HELL      ELLO
# HELLO

#NOTE:WHEATHER THIS IS  A SUBSTRING OR NOT WE CAN CHECK BY USING in OPERATOR...

#EXAMPLE: (if hel in str:)  is the syntax to check the substring or not using (in )operator..
#similarly (not in )operator is used to see it is not a substring in the string it is used to check like that..

#substring means starting from any index and a continous part of the string...
#example 1: for  (in )
s="hello"
if 'hel' in s:
    print("yes it is an substring in the hello")
else:
    print("no man it is not an substring in the hello")

# #example 2 :for (not in ) this checks wheather it is not an substring...
# s="hello"
# if 'ho'  not in s:
#     print("yes it is not a substring")
# else:
#     print("arey no mama it is a substring...")

    
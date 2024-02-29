

#note:indexing in string always starts with 0,1,2...
#always remember that - i.e negative means reverse direction +means correct direction i.e left to right..
s="karunakar"
print(s[1:8])
print(s[1:8:2])

#NOTE:the  starting index should be smaller and ending index should be larger...in this case it gives u an error...

#Note:it also gives an negative indexing as well
print(s[-1])  #in negative indexing quite opposite it should have starting index should be larger and ending index should be smaller..
print(s[-7:-2])

#NOTE:here by default in negative indexing the if u don't give the starting value it takes by default as the starting value in the given string...

#in positive if u give end which is more index no then it wont give u error just it gives the string how much it is present...

#SPECIAL CASE 1:
#WE CAN GO IN REVERSE DIRECTION AS WELL BY  GIVING POSTIVE START AND END AND MENTIONING THE STEP AS NEGATIVE..
print(s[4:1:-1])  #in karunakar it gives u the 'nur' it goes in the reverse direction...


#SPECIAL CASE 2:
#WE  CAN GO  IN REVERSE DIRECTION LIKE THIS ALSO...,by default it takes end as starting value inn the string..
k="karunakar"
print(k[5::-1])  #this line gives u the 'anurak'  this starts from 5 from  left to  right and gives u 1 step since u mentioned negative it goes in the reverse direction...

#SPECIAL CASE 3:
print(k[:2:-1])  #here in this case the string by default start is from the last element in the string...this gives 'rakanu' here u is index 2

k=k[    5:: -1]
print(k)  #'anurak ' it gives u this..  here new string is created and k is refering to new string 

u="karunakar"
print(u[5:1:-2])  #this gives 'au' since end-1 and -2 means reverse direction with 2 as difference
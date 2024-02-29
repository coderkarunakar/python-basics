#COMPARISION OPERATOR ON STRING..I.E  >=,<=, <, >, == , !=, ALL THIS COMES UNDER THE COMPARISION OPERATORS.. IN PYTHON...


# #CASE1:
# #NOTE:this comparision operator always gives u the boolean value like true or false..

# a="karunakar" == "karunakar"  #this will compare character by character ,and gives u  the boolean value..
# print(a)  #this gives u the true as output since we have used comparision operator here..

#CASE 2:
a="ramesh">="karunakar"  #this gives u the output as true since it was compared using the ascii value as we know every alphabet has it's own ascii value..
print(a)   #true..


#ASCII VALUES ARE A-65, B-66 ,C-67, D-68, E-69, F-70.....Z-90
#ASCII VALUES ARE a-99 ,b-100, c-101 ...z-122 these are the ascii values
#if u  want more  clarity then please refer ascii table in google


#CASE 3:
a='RAGHU'>='karun'
print(a)  #this gives false since it has lower and upper character so which has less value like 65(upper value starts with), 99(lower value starts with


#CASE 4:
a="par" >= "parikh"
print(a)  #this gives u the error since it has less length..first 3 characters are similar but the length is less..

#CASE 5:
a="parikh ">="par"
print(a)   #true is the output since the length differs...

#CASE 6:
a="parikh"  >= "parikh"
print(a)  #this gives true since we have same length + > = operator..

#case 7:
a="parikh" > "parikh"
print(a)  #false this gives since we have used only the > symbol..

a="parikh" != "parikh"
print(a)  #this gives u the false..

a="par"  != "parikh"
print(a) #output is true since it is not equall...

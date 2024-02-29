#   QUESTION:COUNT VOWELS ,CONSONANTS,DIGITS,SPECIAL CHARACTERS  IN A STRING...
# NOTE:space is also an special character in a string ..,@$`?` all this are special characters in a string ..

def countinstring(str):
    #initially  we are assigning it as 0 for everything...
    vowels,consonants,digits,special=0,0,0,0
    #char is iterating in the str  (in ) is used to find  the sub string 
    for char in str:

        #it is just an condition for checking range from caps to small
        if (char>='a' and char <='z' or  char>='A' and char <='Z' ):

            #converting it to small numbers..
            char=char.lower()

            #checking ranging from a,e,i,o,u...
            if(char=='a' or char=='e' or char=='i' or char=='o' or char=='u' ):
                vowels=vowels+1

            else:
                consonants=consonants+1

#checking or digits ranging from 0 to 9 
        elif(char>='0' or char<='9'):  #here we took it as string since int wont work in string...  
            digits=digits+1

            #if all this fails then it is a special character...

        else:
            special=special+1


#finally return...
    return vowels,consonants,digits,special


# finally taking a string and calling a function
str="karunakarKARUNAKAR@ $ !"
vowels,consonants,digits,special=countinstring(str)
print(vowels,consonants,digits,special)


                                                #Recursion with strings


#Note:vv.imp ..the strings are immutable....

#replace char in a string using recursion..

def replacechar(s,a,b):
    #base case if the char has nothing then simply replace nothing i.e return empty  string ..
    if len(s)==0:
        return s
    
    #irrespective of first char we need to call the smalloutput 2nd,3rd, remains same and 1st arg is small string we can do slicing to get this
    smalloutput =replacechar(s[1:],a,b)
    #if the  starting index is a then replace it with b + our smalloutput..
    if s[0] ==a:
        return b+ smalloutput
    
    #if the starting index is not a then return starting index astise + small output..
    else:
        return s[0] +smalloutput
    
    #finally function calling..
print(replacechar('csc','c','x'))

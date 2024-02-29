                                #replace character in string 


def replace_char(str,char1,char2):  #str means our actual string and char 1 (what u want to replace)  char2(with what character u want to get replaced...)
    new_string=""  #in oreder store the new getting string so we declared a new string...
    for char in str:  #as we know in gives u  the substring in a given string ...
        if(char==char1):  #here char is just our index iterating value and if our iterating value  is equal to our searching char (i.e what u want to replace) 
            new_string=new_string+char2 #then replace it with char 2 (with what u wanna replace..)
        else:
            new_string=new_string+char  #here char means index then it returns what ever that is present in that specific index
    return new_string  #finally returns the our new string...




str="asjfasjfasjfa"
str=replace_char(str,'a','k')
print(str)
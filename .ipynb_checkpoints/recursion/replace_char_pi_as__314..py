#Replace char pi as 3.14 using recursion...

#here s means string..
def replace_pi(s):

    #if the len ==0 and len==1 simply return astise since inorder to perform this ..pi means 2 chars so even for 1 char len also we are returning astise..

    if len(s) ==0 or len(s) == 1:
        return s
#then here if the first two indexes are pi then retun 3.14 +smalloutput for the rest string.. and make smalloutput as leave 0,1 and start with 2 for the rest..
    if s[0] == 'p'  and s[1] == 'i':
        #if the starting 2 index are pi then making  it as 3.14 + smalloutput(i.e rest string..)
        smalloutput =replace_pi(s[2:])
        return "3.14" + smalloutput

#if the above condition doesnot satisfy then works..    
    else:
        smalloutput = replace_pi(s[1:])
        return s[0]+smalloutput
    
print(replace_pi("pi3.14 k pi"))
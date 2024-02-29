#a particular number is present in a list or not using recursion..

def number_check(a,si,x): #a is array si is start index x is search element
    if si>=len(a):
        return False
    if a[si]==x:  #at array a index of si
        return si,True
    else:
        return number_check(a,si+1,x) #here only  our induction hypothesis or recursion call works
    
a=[1,2,34,5]
print(number_check(a,0,34))
        
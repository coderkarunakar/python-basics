                                #binary search using recursion..
#a is for array x is for the search si is start index,ei is for endindex..
def binarysearch(a,x,si,ei):
#initially the startindex will be zero and endindex is len(a)-1 i.e array length -1
    #if the start index has crossed the end index then this has to be stopped this is the base case.then simply return -1 (if u find it return index if u dont find it simply return -1)
    #the startindex is less than the endindex..inorder to go to that statements of code..
    if si>ei:
        return -1
    
     
#now find the mid point as per the binary search condition..and we need the exact integer so we are doing integer division..
    mid=(si+ei)//2

#if u found search element then return that mid
    if a[mid]==x:
        return mid 
    
#this mean mid is bigger than search element..that means only  u can find no on the left side..,then si remains same but ei changes to mid -1
    elif a[mid]>x:
        return binarysearch(a,x,si,mid-1)
    
    #if the mid is smaller than search element ,now the si changes and ei get remains same now it checks at right..
    else:
        return binarysearch(a,x,mid+1,ei)

#note :the function need to be sorted since it is condition of the binary search..
print(binarysearch([1,2,3,4,5],3,0,9)) # a,si,ei


#NOte:please do the dry run for this..if the else condition also fails then we return -1..
#just pls make sure about the induction step +base case don't go too indepth like how each and every number..is working..
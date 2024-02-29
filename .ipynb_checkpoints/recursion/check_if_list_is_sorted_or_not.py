def issorted(a):
    l=len(a)
    if l==0 or l==1:  #here l means length bayya
        return True
    if a[0]>a[1]:
        return False
    smallerList=a[1:]  #here just copying all the elements and checks every 2 elements for the every recursion call
    isSmallerListSorted=issorted(smallerList)  #just because of this line function call takes place..and checks for every 2 elements in the array..
    if isSmallerListSorted:
        return True
    else:
        return False
    
a=[1,2,3,4,5]
print(issorted(a))


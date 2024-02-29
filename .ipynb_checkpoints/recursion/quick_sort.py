                                                #Quick_sort
#writing the partition function..
def partition(a,si,ei):
    pivot=a[si]    
    #find number of elements smaller than pivot,if we know this we can know how much to move pivot point(i,e exact position of pivot)
    c=0
    for i in range(si,ei+1):  #this range if of complete list
        #planning to keep  every thing less than pivot is left part and greater is right part..and equal elements go to the right part
        if a[i]<pivot:
            c=c+1
            #swap is happening,here c should not be swaped si+c should be swaped
    a[si+c],a[si]=a[si],a[si+c]
    pivot_index = si+c

    i=si
    j=ei
    while i<j:
        #if i and j are at the same element they are be the pivot element..
        if a[i]<pivot:
            i=i+1
            #incase the above is not true then 
        elif a[j]>=pivot:
            j=j-1
        else:
            #incase both the conditions are not met that means a[i] and a[j ] is at wrong place then u can swap 
            a[i],a[j]=a[j],a[i] #now both the elements are sapped
            i=i+1
            j=j-1

    return pivot_index


def quick_sort(a,si,ei):
#base case if the startindex is greater or equal to end index than it is sorted then return nothing..
    if si>=ei:
        return
    

    pivot_index=partition(a,si,ei) #this tells what area of partition is required..this function helps to tell me the pivot index,i.e our 0 index  set it's original value and this tells where has it gone too..,once if we have pivot index then call quick_sort,this quick sort helps to sort the left part and right part of the pivot elements..
    quick_sort(a,si,pivot_index-1)  #this is the first half
    quick_sort(a,pivot_index+1,ei)  #this is for the right half


a=[6,10,9,8,7,1,3,5,4,2]
quick_sort(a,0,len(a)-1)

print(a)
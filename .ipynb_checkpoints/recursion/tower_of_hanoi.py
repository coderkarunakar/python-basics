                                        #Tower of hanoi
def tower_hanoi(n,a,b,c): #here a,b,c are the name of the towers these are strings and n is an integer
    #base case we can take n==0 or n==1 here we are taking n==1 as a base case since 0 means nothing is there then no need to do anything if n==1 means only one is there
    if n==1:
        print("move 1st disk from ",a,"to", c) #simply moving the disk from a to c
        return  #in this case no need  to come down simply return and stop here only if not then come down
    tower_hanoi(n-1,a,c,b) #here moving a to b using c ,here n-1 has moved from a to b using c 
    print("move",n, "th disk from ", a ,"to",c )
#moving n-1 disk from b to c using a
    tower_hanoi(n-1,b,a,c)


tower_hanoi(3,"s","h","d")
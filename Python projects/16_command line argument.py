from sys import argv
print(argv)
print(type(argv))   #Note:by this command line arg we can get output as list 
                    #actually  we get what we saved , and while executing like some editors
                    #we use .py etc in that time what we give like ant thing xyz we get that
                    #in the list form i.e[xyz]
                    #this is the main use of command line argument
                    #ok let us see an small project using command line argument
number=int(argv[1])
for data in range(1,11):
    print(number*data)
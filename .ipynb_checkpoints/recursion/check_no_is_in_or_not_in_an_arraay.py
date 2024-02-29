                    #doubt..

#check wheather a number is present in an array or not 



# The beauty (and purpose) of recursion is that you do not need the loop:

def check(x, num, i):
    if not x[i:]:  # index past length
        return False
    if x[i] == num:
        return True
    return(check(x, num, i+1))




# def check(x, num):
#     if not x:
#         return False
#     return x[0] == num or check(x[1:], num
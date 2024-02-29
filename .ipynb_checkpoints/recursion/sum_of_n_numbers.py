#sum of n natural numbers
def sum_n(n):
    if n==0:
        return 0
    small_output=sum_n(n-1)
    output=small_output+n
    return output
n=int(input('enter the number'))
print(sum_n(n))
#printing the natural numbers from n to one 
def n_to_one(n):
    if n==0:
        return
    print(n)  #here first we are printing so it will print first then go to next function call which is reverse case compared to the one to n natural numbers..
    n_to_one(n-1)

n=int(input('enter the n natural number'))
(n_to_one(n))
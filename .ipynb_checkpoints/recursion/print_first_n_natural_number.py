#please check class notes as well please..

#print first n natural numbers using recursion..
def one_to_n_natural(n):
    if n==0:
        return 

    one_to_n_natural(n-1)
    print(n)
n=int(input('enter the till where u want ur natural numbers'))
(one_to_n_natural(n))

#here we are not returning our main logic so didn't used print in the calling statement just we have used the fucntion name..

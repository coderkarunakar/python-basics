#in some of the systems the recursion depth is so less i.e less than 1000 in my system so in order to increase depth we can set the limit like by importing the module sys as seen below and then also the depth is not going as we mention here but upto some limit we can go  this is mainly used to pass the test cases if we get such max recursion limit is exceeded...


# import sys
# sys.setrecursionlimit(3000)
# def fact(n):
#     if n==0:
#         return 1
#     return n*fact(n-1)

# n=int(input('enter the fact'))
# print(fact(n))

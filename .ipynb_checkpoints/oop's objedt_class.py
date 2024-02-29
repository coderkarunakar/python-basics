# class circle(object):
#     def __init__(self,radius) -> None:
#         self.radius=radius

        
# c=circle(4)
# print(c)

#NOTE:if  we execute this code we get some  binary format like 0*000 like that some that if we use constructor and object class
#so in order to avoid this confusion we can use this __str__() method function we can return some thing that will show instead of this binary code


class circle(object):
    def __init__(self,radius) -> None:
        self.radius=radius

    def __str__(self):
        return "this is an circle class which takes radius as an argument"

c=circle(4)
print(c)

#note: here instead of giving the __init__ constructor if we give this __str__ it works fine
#Note: this concept is just for our understanding purpose that instead of getting binaray code we can return like this also .


# now we wont get binary code we get only our return statement as we gave __str__function


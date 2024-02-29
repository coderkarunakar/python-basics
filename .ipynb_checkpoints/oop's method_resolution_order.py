#METHOD _RESOLUTION _ORDER..

class mother:
    def __init__(self) :
        self.name="manju"
        super().__init__()
    def print(self):
        print("the mothe name is ")
        


class father:
    def __init__(self) :
        self.name="tagore"
        super().__init__()
    def print(self):
        print("the father name is called ")
        


class child(mother,father):
    def __init__(self) :
        super().__init__()
    def print(self):
        print("the  name of the child ",self.name)


c=child()
c.print()
print(child.mro())



#note: we can see the order how it is going to acquire thea properties from it parent claass in an order


#note : if it does not show any thing means it is refering to an object just remember that 
# IT JUST GIVES U THE FLOW HOW IT IS GOING TO INTERLINK WHEN U CALL A FUCNTION...
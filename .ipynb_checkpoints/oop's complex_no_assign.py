
# #it is sir given oops'1 last complex theorey based assignment


#LITTLE DOUBT


class Complex:
   def __init__(self, real, imag):
      self.real = real
      self.imag = imag

   def __str__(self):      #this is just an dunder method it will return what ever u give here this is used when u are trying to print the object it will give u the object reference i.e in the binary format...
      return (f"{self.real}+i{self.imag}" if self.imag >= 0 else f"{self.real} -i{abs(self.imag)}")
                           #this is just like a condition i.e if imag>=0 real else imaginary...
   def plus(self, c):      #this is for plus
      self.real += c.real
      self.imag += c.imag
   
   def multiply(self, c):        #this is for multiply...
      real = (self.real * c.real) - (self.imag * c.imag)
      imag = (self.real * c.imag) + (self.imag * c.real)
      self.real = real
      self.imag = imag

 
a, b = map(int, input().split())    #this is for  input taking purpose
c, d = map(int, input().split())
opt = int(input())
c1 = Complex(a, b)         #this is for calling the class and giving values to the constructor..c1,c2,,,....
c2 = Complex(c, d)
if opt == 1:         #note:this two lines are for opting purpose..option 1,option 2
   c1.plus(c2)
elif opt == 2:
   c1.multiply(c2)
print(c1)      #this is for  final printing purpose
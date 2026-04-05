
from array import *

class a:

    x = array('i',[1,3,5,7,-7])
    y = array('u',['u','b','c'])

    def __init__(self):
        pass

    for i in x:
        print(i , end=' ')
    print()

    for i in range(len(y)):
        print(y[i])

    def __str__(self):
        return  str(self.x)  

    def __repr__(self):
        return  str(self.y)
    
    def __add__(self,other):
        return other.x,other.y   
    
obj = a()
print(obj) # tuple also behave like this  call the __str__
print({obj}) # this calls __repr__
print([obj]) # this calls __repr__
print(obj + obj)
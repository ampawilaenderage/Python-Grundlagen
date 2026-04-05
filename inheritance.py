class GParent:

    def func1(self):
        print('Hello..G')



class Parent(GParent):
    
    def func2(self):
        print('Hello Parent')



class Child(Parent):
    
    def func3(self):
        print('Hello Child')
       # super().func2()  # this call also func2()
        super()
    def func1(self): # overide the parent class method
        print('Child.....')


obj = Child()
obj.func2()
obj.func1()
obj.func3()

print('-------------------------------------------------------\n')

class Fruits():
    unitPrise : float
    numberOfItems : int

    def setValue(self,x,y):
        self.unitPrise = x
        self.numberOfItems = y

class Apple(Fruits): 

    def __init__(self,x,y):
        self.unitPrise = x
        self.numberOfItems = y
        print('Apples price is = ', self.unitPrise * self.numberOfItems )  

    def price(self):
        print('Apples price is = ', self.unitPrise * self.numberOfItems )

    
class Mango(Fruits): 
    def price(self,x,y):
        print('Mangoes price is = ', x * y )

class Orange(Fruits): 
    def price(self):
        print('Oranges price is = ', self.unitPrise * self.numberOfItems )       

 
apple = Apple(3,6)  # call via constructor
orange = Orange() # best way
mango = Mango()



#########################

orange.setValue(10,50) # use the inheritance and OOP is the best way
orange.price()

########################


mango.price(22,44) # direct call not recommonded
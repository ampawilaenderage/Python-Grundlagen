class Inheritance:

    a : int = 10
    # private variable
    __privb : int = 20

    def callPrivate(self):
        return self.__printPrivate()

    def printPrivate(self):
        return self.__privb
    
    # private method
    def __printPrivate(self):
        return self.a + self.__privb

myObj = Inheritance()
print(myObj.a)
#  print(myObj.__privb)  #AttributeError: 'Inheritance' object has no attribute '__privb'

print(myObj.printPrivate())
# print(myObj.__printPrivate())  AttributeError: 'Inheritance' object has no attribute '__printPrivate'. Did you mean: 'printPrivate'?

print(myObj.callPrivate())
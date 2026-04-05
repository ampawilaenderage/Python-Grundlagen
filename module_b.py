

print("module_b: __name__ =", __name__)
print("module_b: program continues...")

class details:

    name : str
    age : int
    

    def __init__(self):
        print('Constructor created')
    

    def printNameWithoutObj(name = 'Sajith') -> str:  # this method does not identify self values as this is not called via an object
        if name == 'Sajith':           
            age = 36
        else:
            age = 40
        return print(name, age)
    
    @staticmethod
    def printName( name = 'Sajith') -> str:
        if name == 'Sajith':           
            pass
        return print(name)


details1 = details()


details1.x = 40
details1.printName() # this method can identify self   # without staticmethod name = object (self)
details.printNameWithoutObj() 
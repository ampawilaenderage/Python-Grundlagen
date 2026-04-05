####

class magicMethods:
     
    def __init__(self, author=None, num_pages=None):
        self.author = author
        self.num_pages = num_pages

    def __str__(self): # print(book1)
        return f"{self.author}, by {self.num_pages} pages"
    
    def __eq__(self,other): # print(book1 == book2)
        return self.author == other.author and self.num_pages == other.num_pages

    def __gt__(self,other): # print(book1 > book2)
        return self.num_pages >= other.num_pages
    
    def __lt__(self,other):

        return self.num_pages < other.num_pages
    
    def __add__(self,other): #print(book1 + book2 )
        return self.author + other.author , self.num_pages + other.num_pages
    
    def __contains__(self, keyword):
        return keyword in self.author 

    def __hash__(self):
        return 9
    
    def __getitem__(self,key):
        if key == 'author':
            return self.author


    def __mul__(self, value):
        # self * value
        return [self] * value
    
    # def __repr__(self):
    #     return 'testtttttttttttt'

book1 = magicMethods('Tom Cruz', 250)
book2 = magicMethods('Ben', 300)
book3 = magicMethods('Alex', 400)


print(book1)
print()

print(book1 == book2)
print(book1 is book2)
print(book1 > book2)
print(book1 < book2)
print(book1 + book2 )


myset = set()
myset.add(book1)
print(myset)

print('Tosm' in book1)

print(book1['author'])
print(book1 * 2) # as book1 is in list it will call __repr__
print(book2)
# print(myset + book1) # TypeError: unsupported operand type(s) for +: 'set' and 'magicMethods'
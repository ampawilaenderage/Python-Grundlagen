t = (('a', 1) ,  (4, 2) , ('c', 3))

l = list(t)
d = dict(t)
s = set(t)

print(l)
print(d)
print(s)

t = tuple(d)
t = tuple(l)
print(t)

l2 = list(d)
print(l2) # only get dict keys

l3 = list(d.values()) # only get values
print(l3)

l4 = list(d.items()) # only get values
print(l4)


fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits  # can do this for list, sets , dict as well

print(green)
print(yellow)
print(red)

def apple(unit_price):
    return (lambda number_of_apples : number_of_apples*unit_price) # Lambda funtion

x = apple(40)
print(x(12))


qdrt = lambda x: x*x
print(qdrt)
print(qdrt(8))
print(qdrt(8.5))
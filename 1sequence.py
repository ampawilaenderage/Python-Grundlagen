#!/usr/bin/env python3



#
# Datentypen: list, tuple, set, dict, (array), ...
#


# eine Liste (list) kann zu jedem Zeitpunkt MEHR als einen Wert speichern
#       eine list ist indiziert
#       die Elemente in der Liste sind geordnet
#       die list ist veränderlich (mutable)

# [] ist das Syntax-Element für Listen (list)

liste = ['Audi', 'BMW', 'Mercedes']

# einfache Iteration OHNE Index
for car in liste:
    print(car)

for index, car in enumerate(liste):
    print(index, car)


#
# Tupel (tuple) - unveränderliche Liste | immutable list -> minimaler Overhead
#

# () ist das Syntax-Element für tuple
tup = (1, 2, 3)
print(tup)
print(type(tup))
print(tup[1])
print(tup[0:2])
print(tup[::2])


# tup[1] = 200            # TypeError: 'tuple' object does not support item assignment
print(tup)

tup = 1, 2, 3           # runde Klammer () ist beim Tupel optional, wenn sich aus dem Kontext eindeutig ein Tuple ergibt
print(tup)

print(1, 2, 3)
print( (1, 2, 3) )


a, b, c = 1, 2, 3       # Tupel-Zuweisung - das Tupel wird 'unpacked' und die einzelnen Werte des Tupels den Variablen zugewiesen
print(a, b, c)          # die Anzahl der Tupel-Elemente (rechts) muss mit der Anzahl der Ziel-Variablen (links) übereinstimmen

print(liste)
print(enumerate(liste))
print(list(enumerate(liste)))


print(a, b, c == 1, 2, 3)
print( (a, b, c) == (1, 2, 3) )         # Tupel-Vergleich: True, da inhaltlich gleich
print( (a, b, c) is (1, 2, 3) )         # False, da keine shared reference

print(tup == (1, 2, 3))                 # True, da inhaltlich gleich
print(tup is (1, 2, 3))                 # True, da (offensichtlich) shared-reference

print( (a, b, c) > (1, 2, 3) )
print( (a, b, c) >= (1, 2, 3) )

print( (2, 4, 6) > (1, 2, 3) )
print( (2, 1, 1) > (1, 2, 3) )
print( (1, 1, 9) > (1, 2, 3) )

print(a, b)
# hilf = a
# a = b
# b = hilf
a, b = b, a
print(a, b)



#
# set - Menge: mutable, nicht indiziert, ungeordnet, aber EINDEUTIG (es gibt keine Duplikate im set)
#

# {} ist das Syntax-Element für ein set
menge = {'A', 'D', 'A', 'C'}
print(menge)
print(menge)

# print(menge[1])         # TypeError: 'set' object is not subscriptable

for zeichen in menge:
    print(zeichen)

print(len(menge))

menge.add('*')
print(menge)





















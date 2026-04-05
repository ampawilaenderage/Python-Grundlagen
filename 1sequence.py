#!/usr/bin/env python3


import random
from array import array



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
#              immutable: frozenset

# {} ist das Syntax-Element für ein set
menge = {'A', 'D', 'A', 'C'}
print(menge)
print(menge)

# print(menge[1])         # TypeError: 'set' object is not subscriptable

for zeichen in menge:
    print(zeichen)

print(len(menge))

menge.add('*')              # fügt ein Element zum set hinzu ...
print(menge)

menge.add('*')              # ... wenn es noch nicht vorhanden ist !!!
print(menge)

print('*' in menge)
print('X' in menge)

menge.remove('*')
print(menge)

# menge.remove('*')           # KeyError: '*'
print(menge)

menge.discard('*')            # kein KeyError, wennd as zu entfernenden Element nicht (mehr) vorhanden ist
print(menge)

menge.clear()
print(menge)

# Elemente in einem set müssen 'hashable' sein !!!

### Exkurs: Ziehung der Lottozahlen
lottoListe = []
for i in range(6):
    zahl = random.randint(1, 49)
    if not zahl in lottoListe:
        lottoListe.append(zahl)
print(f'LottoZalen (list): {sorted(lottoListe)}')

lottoSet = set()
while len(lottoSet) < 6:
    lottoSet.add(random.randint(1, 49))
print(f'LottoZalen (set): {sorted(lottoSet)}')



#
# dict - Dictionary | Wörterbuch: assoziativen Array, Map, ... -> Schlüssel-Wert-Paare (key:value)
#

print('\ndict')
# {:} ist das Syntax-Element für ein dict
ampel = {
    'rot': 'anhalten',
    'gelb': 'aufpassen',
    'grün': 'fahren',
}

print(ampel)
print(len(ampel))

print(ampel['gelb'])
# print(ampel['blau'])            # KeyError: 'blau'

print(ampel.get('gelb'))
print(ampel.get('blau'))

ampel['gelb'] = 'achtung'
print(ampel)

ampel['rot-gelb'] = 'gleich geht es los'
print(ampel)

# die Typisierung der Schlüssel (key) und Werte (value) im dict ist recht flexibel
# der Schlüssel muss hashable sein (EINDEUTIG)
# der Wert kann jeden beliebigen Typ haben (Duplikate sind gestattet)

print(ampel.keys())
print(set(ampel.keys()))            # keys im dict sind unique - wie die Elemente im set

print(ampel.values())
print(list(ampel.values()))         # values im dict sind nicht unique - wie eine list

# über die Elemente eines dict iterieren - mit dict.items()
for key, value in ampel.items():
    print(key, '-', value)
print()

print( [key+'='+value for key, value in ampel.items()] )         # list comprehension
print( {key+'='+value for key, value in ampel.items()} )         # set comprehension

print(ampel)

ampel.pop('rot')
print(ampel)

# ampel.pop('rot')            # KeyError: 'rot'
print(ampel)




#
# Array | Feld
#

# from array import array

print('\narray')

arr = array('i', [1, 2, 3, 4, 5, 6, ])
#           typ   0  1  2  3  4  5

print(arr)
print(len(arr))
print(arr[3])

arr.append(10)
print(arr)

# arr.append('X')         # TypeError: 'str' object cannot be interpreted as an integer
# print(arr)

# arrays sind bei der Verwaltung sehr großer Datenmengen, etwas effizienter als Listen (list)
# => NumPy, SciPy, ...


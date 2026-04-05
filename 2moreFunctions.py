#!/usr/bin/env python3


import random


# Was gaht mit Funktionen?
#       def funktionsName():
#       Funktionen können (keinen, einen oder mehrere) Parameter definieren
#       Beim Aufruf einer Funktionen müssen den definierten Parametern Argumente übergeben werden
#       Funktionen können optionale Parameter definieren (Parameter mit default-Wert)
#       Funktionen können variable Parameter-Listen definieren (*-notation)
#       Funktionen können Daten zurück an den Aufrufer übergeben (return arg)


# Was geht noch mit Funktionen?
#   keyword arguments

def keywordArgs(p1, p2, p3='3', p4='4'):
    print(f'p1={p1}   -   p2={p2}   -   p3={p3}   -   p4={p4}')

keywordArgs('arg-1', 'arg-2')
keywordArgs('arg-1', 'arg-2', 'arg-3')
keywordArgs('arg-1', 'arg-2', 'arg-4')

keywordArgs('arg-1', 'arg-2', '3', 'arg-4')         # <-- NICHT zu empfehlen !!!
# bis hierher: positional arguments

# jetzt neu: keyword arguments
keywordArgs('arg-1', 'arg-2', p4='arg-4')

# auch required parameter können als keyword argument übergeben werden
keywordArgs(p1='arg-1', p2='arg-2', p4='arg-4')

# bei keyword arguments ist die Reihenfolge EGAL !!!
keywordArgs(p2='arg-2', p4='arg-4', p1='arg-1')
# keywordArgs(p2='arg-2', p4='arg-4')                     # TypeError: keywordArgs() missing 1 required positional argument: 'p1'

# wenn bei einem Funktions-Aufruf die Argumente positional UND mit keyword übergeben werden
# müssen ZUERST alle positional und erst DANACH die keyword arguments angegeben werden
# keywordArgs(p2='arg-2', p4='arg-4', 'arg-1')            # SyntaxError: positional argument follows keyword argument

keywordArgs('arg-1', p4='arg-4', p2='arg-2') 


print()
# Was geht noch mit Funktionen?
#   dictionary parameter

def dictIn(**kv):
    # **kv ist in der Funktion - ein dict
    # der aufruf erfolgt ausschließlich über keyword arguments
    for k, v in kv.items():
        print(k, v)
    print()

dictIn(rot='STOP')
dictIn(rot='STOP', gelb='ACHTUNG')
dictIn(rot='STOP', gelb='ACHTUNG', grün='FAHREN')
dictIn(rot='STOP', gelb='ACHTUNG', grün='FAHREN', antwort=42)
# dictIn('und jetzt?')                                            # TypeError: dictIn() takes 0 positional arguments but 1 was given
dictIn()


print()
# Was geht noch mit Funktionen?
#   variable Parameter-Liste in Verbindung mit dictionary parameter

def allIn(*v, **kv):
    # alle position arguments landen in v (tuple)
    # alle keyword arguments landen in kv (dict)
    print(v, kv, sep='\n')

allIn(123, 4711, 'ein String')
allIn(rot='STOP', grün='FAHREN')
allIn(123, 4711, 'ein String', rot='STOP', grün='FAHREN')
allIn()


print()
# Was geht noch mit Funktionen?
#   dictionary arguments

dictionary = {'rot': 'STOP', 'grün': 'FAHREN'}
allIn(dictionary)
allIn(**dictionary)

def ampel(rot, grün):
    print(rot, grün)

ampel(1, 2)
ampel(rot='---', grün='|||')
ampel(**dictionary)

liste = ['X', 'Y']
ampel(*liste)


print()
# Was geht noch mit Funktionen?
#   spezielle Parameter '/' und '*'
#   '/' - davor NUR positional arguments
#   '*' - danach NUR keyword arguments
#   (positional-only / positional or keyword * keyword-only)
#   '/' ist auch als letzter Parameter möglich                      def specialParams(p1, p2, p3, p4, p5, p6, /):
#   '*' ist auch als erster Parameter möglich                       def specialParams(*, p1, p2, p3, p4, p5, p6):
#   '/' und '*' dürfen auch zusammen stehen                         def specialParams(p1, p2, p3, /, *, p4, p5, p6):

def specialParams(p1, p2, /, p3, p4, *, p5, p6):
    print(p1, p2, p3, p4, p5, p6)

# specialParams('1', '1', '1', '1', '1', '1', )                         # TypeError: specialParams() takes 4 positional arguments but 6 were given
# specialParams(p1='2', p2='2', p3='2', p4='2', p5='2', p6='2', )       # TypeError: specialParams() got some positional-only arguments passed as keyword arguments: 'p1, p2'
specialParams('3', '3', p3='3', p4='3', p5='3', p6='3', )
specialParams('4', '4', '4', '4', p5='4', p6='4', )

#
# bis hierher: Funktionen im Stil von Prozeduren
#


#
# jetzt neu: 'echte' Funktionen, die einen Wert und einen Typ haben
#

print()
# Was geht noch mit Funktionen?
#   eine Rückgabe (return arg)

def quadrat(wert):
    q = wert * wert
    return q

eingabe = 5
quad = quadrat(eingabe)
print(f'Das Quadrat von {eingabe} beträgt {quad}')
print(f'Das Quadrat von 6 beträgt {quadrat(6)}')


print()
# Was geht noch mit Funktionen?
#   'mehrere' Rückgaben (return args)

def quadrat2(wert):
    q = wert * wert
    return wert, q          # 'mehrere' Rückgaben werden als tuple zurückgegeben

q2 = quadrat2(7)
print(q2, q2[0], q2[1])


print(allIn())          # Funktionen im Stil vom Prozeduren geben nichts (None) zurück
print(quadrat(8))


print()
# Was geht noch mit Funktionen?
#   mehrere Rückgaben (yield) / Generator

# Prozeduren            geben nichts zurück (None)
# Funktionen            geben einen Wert zurück (return)
# Generatoren           geben mehrere Werte zurück (yield)

print(range(10))
# bis Python 2 hat range() eine list zurückgegeben
# ab Python 3 ist range() ein Generator

print(list(range(10)))

liste = list(range(10))
print(liste)

for i in liste:             # die Liste (list) besteht aus 10 Elementen, die zum Start der Schleife komplett im Speicher vorliegen müssen
    print(i, end=' ')
print()

for i in range(10):         # der Generator liefert für jeden Schleifendurchlauf EIN neues Element
    print(i, end=' ')
print()


# ein eigener Generator - am Beispiel einer eigenen range() 0-n
def myRange(n):
    count = 0
    while count < n:
        yield count
        count += 1

print(myRange(10))
print(list(myRange(10)))

for i in myRange(10):
    print(i, end=' ')
print()

# wie kann man an die einzelnen Werte eines Generators herankommen?
myRangeVar = myRange(10)
print(myRangeVar)
while True:
    # i = next(myRangeVar)            # next() liefert das nächste Element des Generators (beginnend beim 1.)
    #                                 #        - oder eine StopIteration, wenn keine Werte mehr vorhanden sind
    i = next(myRangeVar, None)        # next() liefert das nächste Element des Generators (beginnend beim 1.)
                                      #        - oder None, wenn keine Werte mehr vorhanden sind
    # if not i: break                 # ungünstig, da bereits yield 0 die Schleife beendet
    if i is None: break
    print(i, end=' ')
print()


#
# kleines Beispiel für einen Generator, der zufällige int-Werte liefert
#

def myIntRandom(n = 10, start = 0, end = 99):
    # myIntRandom liefert n zufällige Werte vom Typ int
    # im Werte-Bereich von start bis end (inkl.)
    count = 0
    while count < n:
        yield random.randint(start, end)
        count += 1

for ri in myIntRandom(end=50):
    print(ri, end=' ')
print()


print()
# Was geht noch mit Funktionen?
#   type-annotations | Typ-Hinweise - OHNE Garantie !!!

def multi10(i: int) -> float:
    if not isinstance(i,int):
        print('Parameter-Typ ungültig:', type(i))
        return
    return i * 10.0

print(multi10(9))
print(multi10(9.0))
# print(multi10('9'))         # TypeError: can't multiply sequence by non-int of type 'float'
print(multi10('9')) 



print()
# Was geht noch mit Funktionen?
#   anonyme Funktionen (lambda) UND Funktions-Referenzen

# Lambda-Funktionen bestehen aus EINEM Ausdruck
#   lambda parameter: expression


# ist NICHT üblich, eine Lambda-Funktion direkt einer Variablen zuzuweisen !!!
qdrt = lambda x: x*x
print(qdrt)
print(qdrt(8))
print(qdrt(8.5))
# print(qdrt('X'))

# üblich ist, Lambdas als Argumente an Funktionen zu übergeben, die ein Callback (Callable) erwarten
def myComprehension(liste, clbl):
    return [clbl(x) for x in liste]

liste = [2, 4, 6, 8, ]
print(myComprehension(liste, lambda i: i+1))
print(myComprehension(liste, lambda i: i**3))
print(myComprehension(liste, lambda i: quadrat(i)))

liste = ['Audi', 'BMW', 'Mercedes']
print(myComprehension(liste, lambda s: s*2))
print(myComprehension(liste, lambda s: s.upper()))

# Funktions-Referenzen
#   Eine Funktion bekommt einen Namen
#   Eine Funktion wird aufgerufen über ihren Namen MIT ()
#   Wird ein Funktions-Bezeichner OHNE () verwendet, handelt es sich um eine Funktions-Referenz

print(quadrat(9))
print(quadrat)
q2 = quadrat
print(q2)
print(q2(10))

# Ein Callback (Callable) ist nichts anderes als eine Funktions-Referenz

liste = [2, 4, 6, 8, ]
print(myComprehension(liste, quadrat))
print()


# Was geht noch mit Funktionen?
#   Decorators (bezogen auf Funktionen)

#
# Beispiel für Funktions-Referenzen
#

def getPI():
    return 3.141

pi = getPI()
print(pi)

piFunc = getPI
print(getPI)
print(piFunc)

print(piFunc())



def first(text):
    return f'das ist ein ERSTER {text}'

def second(text):
    return f'das ist ein ZWEITER {text}'

def select(func):
    return func('Versuch')

print(select(first))
print(select(second))
print()


#
# Beispiele für innere Funktionen
#

def topLevel():
    print('Top-Level')
    
    def inner1():
        print('Inner 1')

    def inner2():
        print('Inner 2')

    inner1()
    inner2()

topLevel()
# inner1()
# inner2()
print()


#
# Innere Funktion mit RÜckgabe
#

def topLevelWithReturn(x):
    def inner1():
        print('Inner 1')

    def inner2():
        print('Inner 2')

    if x == 1:
        return inner1
    else:
        return inner2

first = topLevelWithReturn(1)
second = topLevelWithReturn(2)

first()
second()
print()


#
# Beispiel für einen EINFACHEN Dekorator
#

def myDecorator(func):
    def wrapper():
        print('before wrap')
        func()
        print('after wrap')
    return wrapper

def doIt():
    print('ich tue etwas')

doIt()

# Der Einsatz des Decorators - manuell
doIt = myDecorator(doIt)
doIt()
print()

#  Der Einsatz des Decorators - mit Decorator-Syntax
@myDecorator
def doMore():
    print('ich tue mehr')

doMore()
print()

# @myDecorator
# def doSomething(task):
#     print(f'ich mache was: {task}')

# doSomething('bügeln')
# TypeError: myDecorator.<locals>.wrapper() takes 0 positional arguments but 1 was given


# Decorator with Args
def myDecoratorArgs(func):
    def wrapper(*args, **kwargs):
        print('before wrap')
        func(*args, **kwargs)
        print('after wrap')
    return wrapper

@myDecoratorArgs
def doSomething(task):
    print(f'ich mache was: {task}')

doSomething('bügeln')
print()


# TODO Decorator with Return


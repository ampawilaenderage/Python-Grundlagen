#!/usr/bin/env python3


from dataclasses import dataclass

#
# Dataclasses (ab 3.7)
#


# @dataclass liefert Standard-Implementierungen für
#   __init__(), __repr__() und __eq__()

# @dataclass(order=True) | Default: (order=False)
#   __lt__(), __le__()  => dann KEINE eigene Implementierung möglich

# @dataclass(frozen=True) | Default: (frozen=False)
#   __hash__()          => macht die Klasse hashable UND immutable

# @dataclass
# @dataclass(order=True)
@dataclass(order=True, frozen=True)
class Point:
    x: int          # Deklaration der Attribute - inkl. Typisierung (OHNE Garantie) - NOTWENDIG
    y: int = 10     # Die Deklaration der Attribute ergibt DIREKT die Parameter-Liste des Konstruktors
                    #   def __init__(self, x: int, y: int = 10):
    
    # einen eigenen Konstruktor zu programmieren ist möglich, aber sinnlos

    # eine eigene __str__() zusätzlich zu implementieren, ist möglich
    def __str__(self) -> str:
        return f'{self.x}/{self.y}'


p1 = Point(15, 20)
print(p1)

# p1.x = 17
# p1.y = 22

print(p1)
print(p1.x, p1.y)

p2 = Point(12)
print(p2)

p3 = Point('A', 'B')
print(p3)

p4 = Point(15, 20)
print(p1, p4)
print(p1 == p4)
print(p1 is p4)

print(p1, p2)
print(p1 > p2)


punktMenge = {p1, p2, p4}
print(punktMenge)
# TypeError: cannot use 'Point' as a set element (unhashable type: 'Point')

# hashable bedeutet __eq__() und __hash__() synchron implementiert
#   entweder KEINE
#   oder BEIDE



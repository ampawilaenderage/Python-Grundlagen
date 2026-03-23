#!/usr/bin/env python3

#
# Objektorientierte Programmierung OOP
#


# Warum OO-Programmierung?
#
#   Für uns - Menschen - sind Objekte die Dinge des täglichen Lebens
#
#   Objekte haben Eigenschaften     ==> Attribute | Variablen
#   Objekte haben Verhalten         ==> Operation | Methoden (def)
#
#   - wir programmieren KEINE Objekte
#   - wir programmieren KLASSEN
#
#   Klassen
#   ... beschreiben Objekte
#   ... sind in sich geschlossene Einheiten
#   ... haben EINEN exakt definierten Funktionsumfang
#   ... Objekte sind von aussen über eine definierte Schnittstelle ansprechbar

# Tipp zum Lesen: https://openbook.rheinwerk-verlag.de/oop/

# -----------------------------------------------------------------------------
# wir programmieren KLASSEN

# Jede Klassen-Definition ist zugleich auch eine Typ-Definition

class Auto:
    # die Klasse Auto besteht aus einem Bock (eingerückt)
    pass

    # 1. Attribute - Objekte haben Eigenschaften
    marke: str
    speed: int

    # 2. Konstruktor - wird ausgeführt, wenn ein Objekt erzeugt wird
    def __init__(self, marke: str, speed: int = 0):
        # print('ein Auto-Objekt wird erzeugt')
        self.marke = marke
        self.speed = speed


# -----------------------------------------------------------------------------
# wir verwenden Objekte

a1 = Auto('BMW', 150)         # damit wird ein Objekt der Klasse Auto erzeugt - und dessen Referenz auf die Variable a1 zugewiesen
print(a1)
print(type(a1))
print(isinstance(a1, Auto))

# der '.' ist der Objekt-Operator - darüber wird auf den Inhalt des Objektes zugegriffen
# a1.marke = 'BMW'
# a1.speed = 150


a2 = Auto('Mercedes')
# a2.marke = 'Mercedes'
# a2.speed = 45


print(f'Das Auto (a1) ist ein {a1.marke} und fährt {a1.speed} km/h')
print(f'Das Auto (a2) ist ein {a2.marke} und fährt {a2.speed} km/h')


# print(a1.model)         # AttributeError: 'Auto' object has no attribute 'model'
a1.model = '330e'       # hier wurd ein dynamisches Attribut zu DIESEM Auto-Objekt hinzugefügt - NICHT ZU EMPFEHLEN !!!
print(a1.model)
# print(a2.model)















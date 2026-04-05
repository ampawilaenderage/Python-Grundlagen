#!/usr/bin/env python3


from typing import ClassVar


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
    _marke: str
    __speed: int          # Definition: -50 bis 300

    # Klassen-Attribute gehören zur Klasse (static) - nicht zum Objekt
    count: ClassVar[int] = 0

    # 2. Konstruktor - wird ausgeführt, wenn ein Objekt erzeugt wird
    def __init__(self, marke: str, speed: int = 0):
        # print('ein Auto-Objekt wird erzeugt')
        self._marke = marke
        # self.__speed = speed            # OHNE Plausibilität
        self.speed = speed                # MIT Plausibilität
        Auto.count += 1

        # self. referenziert das aktuelle Objekt
        # Auto. (Klassen) referenziert die Klasse -> Klassen-Attribut

    # 3. Methoden - Objekte haben Verhalten
    # 3a. Business-Methoden
    def beschleunigen(self, diff: int = 10):
        # 'self' ist in JEDER Objekt-Methode als ERSTER Parameter zu deklarieren !!!
        # self.__speed += diff            # direkter Attribut-Zugriff -> OHNE Plausibilität
        self.speed += diff              # self.speed = self.speed + diff -> MIT Plausibilität

    # 3b. technische Hilfs-Methoden
    # accessors: getter/setter

    # # Python-Style getter
    # def marke(self) -> str:
    #     return self._marke
    
    # def speed(self) -> int:
    #     return self.__speed


    # Property-Methoden
    @property                       # @ - decorator
    def marke(self) -> str:
        print('aufruf der property-Methode: marke')
        return self._marke
    
    @property                       # durch property-decorator ist speed ohne runde Klammern zu verwenden
    def speed(self) -> int:
        return self.__speed

    def get_speed(self):
        return self.__speed
        #return a1._Auto__speed
    
    @speed.setter                   # der setter-decorator muss NACH der property definiert werden
    def speed(self, speed: int):
        if -50 <= speed <= 300:
            self.__speed = speed
        else:
            if speed > 300:
                self.__speed = 300
            else:
                self.__speed = -50

# -----------------------------------------------------------------------------
# wir verwenden Objekte


# Wie viele Auto-Objekte wurden bisher erzeugt?
print(f'die Anzahl der Auto-Objekte {Auto.count}')


# a1 = Auto()
a1 = Auto('BMW', 150)         # damit wird ein Objekt der Klasse Auto erzeugt - und dessen Referenz auf die Variable a1 zugewiesen
# print(a1)
# print(type(a1))
# print(isinstance(a1, Auto))

# # der '.' ist der Objekt-Operator - darüber wird auf den Inhalt des Objektes zugegriffen
# # a1.marke = 'BMW'
# # a1.speed = 150


a2 = Auto('Mercedes')
# # a2.marke = 'Mercedes'
# # a2.speed = 45


# print(f'Das Auto (a1) ist ein {a1.marke} und fährt {a1.speed} km/h')
# print(f'Das Auto (a2) ist ein {a2.marke} und fährt {a2.speed} km/h')


# # print(a1.model)         # AttributeError: 'Auto' object has no attribute 'model'
# a1.model = '330e'       # hier wurde ein dynamisches Attribut zu DIESEM Auto-Objekt hinzugefügt - NICHT ZU EMPFEHLEN !!!
# print(a1.model)
# # print(a2.model)

# # Namensräume enthalten alle Attribute einer Klasse / eines Objektes
# # ansehen mit vars()
# print(vars(a1))
# print(vars(a2))
# print(vars(Auto))


# # Wie viele Auto-Objekte wurden bisher erzeugt?
# print(f'die Anzahl der Auto-Objekte {Auto.count}')


# # Ein Auto-Objekt kann beschleunigt werden
# a1.beschleunigen()
# print(f'Das Auto (a1) ist ein {a1.marke} und fährt {a1.speed} km/h')

# # object.method()
# a1.beschleunigen(25)
# print(f'Das Auto (a1) ist ein {a1.marke} und fährt {a1.speed} km/h')

# # Alternativer - aber nicht üblicher - Nethoden-Aufruf
# # Class.method(object)
# Auto.beschleunigen(a1)
# print(f'Das Auto (a1) ist ein {a1.marke} und fährt {a1.speed} km/h')

# Auto.beschleunigen(a1, 25)
# print(f'Das Auto (a1) ist ein {a1.marke} und fährt {a1.speed} km/h')


# a1.speed = 9999
# print(f'Das Auto (a1) ist ein {a1.marke} und fährt {a1.speed} km/h')

# Kapselung bedeutet: Objekte dürfen ausschließlich über eine definierte Schnittstelle angesprochen werden
#                     Implementierungs-Details bleiben verborgen
#                     Attribute sind IMMER Implementierungs-Details
#
#       üblich (objektorientierte Theorie): Access-Level
#           private         nur in der Klasse verfügbar
#           protected       ... und zusätzlich in Sub-Classes
#           package         nur im Paket verfügbar
#           public          überall verfügbar
#
#       Attribute sollten IMMER private sein - direkter Zugriff nur innerhlab der Klasse
#
#
#       Python unterstützt KEINE Access-Level !!!
#       in Python ist alles public !!!
#
#       Die Lösung in Python: Konventionen
#           1. Ein Unterstrich vor dem Bezeichner gilt als 'private' (_marke)
#           2. Zwei Unterstriche vor dem Bezeichner gilt als 'even more private' (__speed)
#               -> wird intern zu: _KlassenName__abbtributBezecihner (name mangeling)

# mit 'krimineller Energie' ist ein direkter Attribut-Zugriff immer noch möglich
print(f'Das Auto (a1) ist ein {a1._marke} und fährt {a1._Auto__speed} km/h')
a1.beschleunigen()
print(f'Das Auto (a1) ist ein {a1._marke} und fährt {a1.get_speed()} km/h')
# # Abruf der Attribut-Werte über Python-Style getter
# print(f'Das Auto (a1) ist ein {a1.marke()} und fährt {a1.speed()} km/h')

# Abruf der Attribut-Werte über Python-Style getter
print(f'Das Auto (a1) ist ein {a1.marke} und fährt {a1.speed} km/h')

a1.speed = 9999
print(f'Das Auto (a1) ist ein {a1.marke} und fährt {a1.speed} km/h')


print(f'Das Auto (a1) ist ein {a1.marke} und fährt {a1.speed} km/h')

# wenn kein setter zu einer Property existiert: de facto immutable, read-only
# a1.marke = 'Mini'
# print(f'Das Auto (a1) ist ein {a1.marke} und fährt {a1.speed} km/h')

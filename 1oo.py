#!/usr/bin/env python3


from typing import ClassVar

#
# Objektorientierte Programmierung in Python (OOP)
#


# Auffrischiung OOP
# 
#   Programmier-Paradigmen
#       prozedurale Programmierung / imperative Programmierung      (Trennung von Daten und Funktionalität)
#       objektorientierte Programmierung                            (Zusammenfassung von Daten und Funktionalität)
#       funktionale Programmierung
#       logische Programierung

# Warum OO-Programmierung?
#
#       Für uns - als Menschen - sind Objekte die Dinge des täglichen Lebens !!!
#
#       Objekte haben Eigenschaften     ==> Attribute | Variablen
#       Objekte haben Verhalten         ==> Operation | Methode (def)
#
#       - wir programmieren KEINE Objekte
#       - wir programmieren KLASSEN
#
#       Klassen
#       ... beschreiben Objekte
#       ... sind in sich geschlossene Einheiten
#       ... haben EINEN exakt definierten (begrenzten) Funktionsumfang
#       Objekte sind über eine definierte Schnittstelle ansprechbar
#
# Vorteile der OO-Programmierung?
#       Wiederverwendbarkeit (dry - don't repeat yourself) - geringere Fehleranfälligkeit, verbesserte Wartbarkeit
#       Erweiterbarkeit - Vererbung
#       Polymorphie (poly: Viel - Morph: Form)
#       Sicherheit - (Daten)-Kapselung - Attribute sind nur INNERHLB der Klasse verfügbar

# Tipp zum Lesen: https://openbook.rheinwerk-verlag.de/oop/


# ----------------------------------------------------------------------------------------
# - wir programmieren KLASSEN

# Jede Klassen-Definition ist eine Typ-Definition

# eine Klassendefinition beginnt mit dem Schlüsselwort 'class'
# gefolgt von einem syntaktisch korrekten Bezeichner 'Auto'
#   (Konvention: KlassenNamen beginnen mit einem großen Buchstaben, Substantiv, Singular)
# gefolgt von einer runden Klammer (optional)
# dann :
class Auto:
    # die Klasse Auto besteht aus einem Block (eingerückt)
    pass

    # 1. Attribute - Objekte haben Eigenschaften
    _marke: str
    __speed: int      # Definition: -50 bis 300
    
    # Klassen-Attribute gehören zur Klasse (static) - nicht zum Objekt
    count: ClassVar[int] = 0

    # 2. Konstruktor - wird ausgeführt, wenn ein Objekt erzeugt wird
    def __init__(self, marke: str, speed: int = 0):
        # print('es wird ein Auto-Objekt erzeugt')
        self._marke = marke
        # self.__speed = speed
        self.speed = speed
        Auto.count += 1

        # self. referenziert das aktuelle Objekt
        # Auto. (KlassenNamen) referenziert die Klasse -> Klassen-Attribut
    
    # 3. Methoden - Objekte haben Verhalten
    # 3a. Business-Methoden
    def beschleunigen(self, diff: int = 10):
        # 'self' ist in JEDER Objekt-Methode als ERSTER Parameter zu deklarieren
        # 'self' referenziert das OBjekt auf dem die Methode aufgerufen wird
        # self.__speed += diff            # direkte Veränderung des Attributes - OHNE Plausibilität
        self.speed += diff                # self.speed = self.speed + diff - MIT Plausibilität

    # 3b. technische Hilfs-Methoden
    # accessors: getter/setter

    # def marke(self) -> str:
    #     return self._marke
    
    # def speed(self) -> int:
    #     return self.__speed

    @property                   # @ - decorator
    def marke(self) -> str:
        print('aufruf der property-methode: marke')
        return self._marke
    
    @property                   # durch property-decorator ist speed ohne rune Klammer () zu verwenden
    def speed(self) -> int:
        return self.__speed
    
    @speed.setter               # der setter-decorator muss NACH der property definiert werden
    def speed(self, speed: int):
        if -50 <= speed <= 300:
            self.__speed = speed
        else:
            if speed > 300:
                self.__speed = 300
            else:
                self.__speed = -50

# ----------------------------------------------------------------------------------------
# - wir verwenden Objekte

# Wie viele Auto-Objekte wurden erzeugt?
print(f'es gibt {Auto.count} Auto-Objekte')

# a1 = Auto()     # hier wird ein Auto-Objekt erzeugt (auf dem Heap gespeichert) und dessen Referenz auf die a1 zugewiesen 
a1 = Auto('BMW', 150)
print(a1)
print(type(a1))
print(isinstance(a1, Auto))

# der '.' ist der Objekt-Operator. Darüber wird auf den Inhalt des Objektes zugegriffen. 
# a1.marke = 'BMW'
# a1.speed = 150


a2 = Auto('Mercedes')
# a2.marke = 'Mercedes'
# a2.speed = 48


# print(f'Das Auto (a1) ist ein {a1.marke} und fährt {a1.speed}')
# print(f'Das Auto (a2) ist ein {a2.marke} und fährt {a2.speed}')


# # print(a1.model)             # AttributeError: 'Auto' object has no attribute 'model'
# a1.model = '750iL'            # hier wird ein dynamisches Attribut zum Auto-Objekt hinzugefügt - NICHT ZU EMPFEHLEN !!!
# print(a1.model)
# # print(a2.model)

# # Namensräume enthalten alle Attribute einer Klasse / eines Objektes
# print(vars(a1))
# print(vars(a2))
# print(vars(Auto))


# # Wie viele Auto-Objekte wurden erzeugt?
# print(f'es gibt {Auto.count} Auto-Objekte')     # das Klassen-Attribut
# print(f'es gibt {a1.count} Auto-Objekte')       # im Namensraum des Objektes ist count nicht vorhanden => dann wird der Namensraum der Klasse verwendet

# a1.count = 99               # hier wird ein dynamisches Attribut zum Auto-Objekt hinzugefügt - NICHT ZU EMPFEHLEN !!!

# print(f'es gibt {Auto.count} Auto-Objekte')
# print(f'es gibt {a1.count} Auto-Objekte')


# a1.beschleunigen()
# print(f'Das Auto (a1) ist ein {a1.marke} und fährt {a1.speed}')

# a1.beschleunigen(30)
# print(f'Das Auto (a1) ist ein {a1.marke} und fährt {a1.speed}')

# # Standard-Methoden-Aufruf:         object.method()
# # alternativer Methoden-Aufruf:     Class.method(object)                - aber nicht sehr üblich !!!

# Auto.beschleunigen(a1)
# print(f'Das Auto (a1) ist ein {a1.marke} und fährt {a1.speed}')

# Auto.beschleunigen(a1, 30)
# print(f'Das Auto (a1) ist ein {a1.marke} und fährt {a1.speed}')


# a1.speed = 12345
# print(f'Das Auto (a1) ist ein {a1.marke} und fährt {a1.speed} km/h')


# Kapselung bedeutet: Objekte dürfen ausschließlich über eine definierte Schnittstelle angesprochen werden
#                     Implementierungs-Details bleiben verborgen
#                     Attribute sind Implementierungs-Details
#
#   üblich (objektorientierten Theorie): Access-Level
#       private         nur in der Klasse verfügbar
#       protected       ... und zusätzlich in Sub-Klassen
#       package         nurim Paket verfügbar
#       public          für alle verfügbar
#
#   Attribute sollten IMMER private sein
#
#
#   Python unterstützt keine Access-Level
#   in Python ist alles public !!!
#
#   Die Lösung in Python: Konventionen
#       1. Ein Unterstrich vor dem Bezeichner gilt als 'private' (_marke)
#       2. Zwei Unterstricher vor dem Bezeichner gilt als 'even more private' (__speed)
#           -> wird intern zu: _KlassenName__attributBezeichner (name mangeling)

# mit 'krimineller Energie' ist ein direkter Attribut-Zugriff möglich
print(f'Das Auto (a1) ist ein {a1._marke} und fährt {a1._Auto__speed} km/h')

# Python-Style getter
# print(f'Das Auto (a1) ist ein {a1.marke()} und fährt {a1.speed()} km/h')

# Properties
print(f'Das Auto (a1) ist ein {a1.marke} und fährt {a1.speed} km/h')

a1.speed = 12345
print(f'Das Auto (a1) ist ein {a1.marke} und fährt {a1.speed} km/h')


a1.beschleunigen()
print(f'Das Auto (a1) ist ein {a1.marke} und fährt {a1.speed} km/h')

# wenn kein setter zu einer property existiert: de facto immutable, read-only
# a1.marke = 'Mini'
# print(f'Das Auto (a1) ist ein {a1.marke} und fährt {a1.speed} km/h')


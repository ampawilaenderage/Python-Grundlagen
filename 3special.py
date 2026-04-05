#!/usr/bin/env python3


#
# Special Methods | spezielle Methoden (magic methods)
#


class Auto:

    # 1. Attribute
    # 2. Konstruktor (__init__())
    # 3. Methoden
    # 3a. Business-Methoden
    # 3b. technische Hilfs-Methoden#
    #   - property/setter
    #   - weitere special methods

    __marke: str
    __speed: int

    def __init__(self, marke: str, speed: int = 0):
        self.__marke = marke
        self.speed = speed

    def beschleunigen(self, diff: int = 10):
        self.speed += diff

    @property
    def marke(self) -> str:
        return self.__marke
    
    @property
    def speed(self) -> int:
        return self.__speed

    @speed.setter
    def speed(self, speed: int):
        if -50 <= speed <= 300:
            self.__speed = speed
        else:
            if speed > 300:
                self.__speed = 300
            else:
                self.__speed = -50
    
    # --- special methods (dunder methods) ----------------------------------------

    def __str__(self):
        # gibt einen String (str) zurück, der eine textliche Repränsentation des Objektes beinhaltet
        # user friendly
        # wenn diese fehlt, wird __repr__() verwendet
        return f'{self.marke}/{self.speed}'

    def __repr__(self):
        # gibt einen String (str) zurück, der eine textliche Repränsentation des Objektes beinhaltet
        # technisch
        # so, dass dieser String, sollte er als Python-Code ausgeführt werden, das Objekt reproduziert
        # return f"Auto('{self.marke}', {self.speed})"
        return f"Auto(marke='{self.marke}', speed={self.speed})"
    
    def __del__(self):
        # wird ausgeführt, wenn ein Objekt gelöscht wird - Destruktor
        # hier wird aufgeräumt
        # ==> besser mit with/as arbeiten
        print(f'Tschüss {self.marke}')

    # --- operator overloading ----------------------------------------------------

    def __eq__(self, other):
        # self == other
        # prüft, ob self und other inhaltlich gleich sind (ob die Attribute gleiche Werte haben)
        # wenn diese Methode fehlt, wird bei == ein is-Vegleich durchgeführt
        if self is other: return True
        if not isinstance(other, Auto): return False
        # return self.marke == other.marke and self.speed == other.speed
        # return (self.marke, self.speed) == (other.marke, other.speed)
        return self.marke == other.marke

    def __hash__(self) -> int:
        # __eq__() und __hash__() sollten immer gemeinsam implementiert werden - oder gar nicht
        # nur dann gilt die Klasse - deren Objekte - als hashable
        # wenn diese Methode fehlt, wird ein eindeutiger Wert je Objekt geliefert
        # Implementierungs-Vorgaben:
        #       Zwei Objekte, die nach __eq__() gleich sind, MÜSSEN als hash den selben int-wert liefern
        #       Zwei Objekte, die nach __eq__() NICHT gleich sind, SOLLTEN als hash unterschiedliche int-Werte liefern (nicht zwingend)
        #       Attribute, die für __eq__() und __hash__() verwendet werden MÜSSEN immutable sein (OHNE setter)
        # return len(self.marke) * self.speed
        # return len(self.marke)                  # mögliche, aber nicht optimale Implementierung
        # return 99                               # entspicht - leider - der Implementierungs-Vorgabe
        # return hash( (self.marke, self.speed) ) 
        return hash(self.marke)                 # Empfehlung !!!
    
    # --- more operator overloading -----------------------------------------------

    def __lt__(self, other) -> bool:
        # self < other - lt - less than - kleiner als
        if self is other: return False
        if not isinstance(other, Auto):
            raise TypeError("'<' not supported between instances of 'Auto' and another type")
        return (self.marke, self.speed) < (other.marke, other.speed)
        
    def __le__(self, other) -> bool:
        # self <= other - le - less than or equal - kleiner oder gleich
        if self is other: return True
        if not isinstance(other, Auto):
            raise TypeError("'<=' not supported between instances of 'Auto' and another type")
        return (self.marke, self.speed) <= (other.marke, other.speed)
        
    def __add__(self, other):
        # self + other - add - plus
        if isinstance(other, int):
            self.beschleunigen(other)
            return self
        if not isinstance(other, Auto):
            raise TypeError("unsupported operand type(s) for +: 'Auto' and another type")
        return Auto(self.marke + other.marke, self.speed + other.speed)

    def __mul__(self, value):
        # self * value
        return [self] * value
    
# ---------------------------------------------------------------------------------

a1 = Auto('BMW', 150)

print(f'Das Auto (a1) ist ein {a1.marke} und fährt {a1.speed} km/h')

print(a1)           # wenn ein Objekt mit print() ausgegeben wird, wird die __str__()-Methode aufgerufen
                    # der Standard-Output: <__main__.Auto object at 0x000002500F0086E0>

autoString = a1.__str__()           # möglich, aber nicht üblich
print(autoString)

autoString = str(a1)                # besser: Typ-Umwandlung
print(autoString)


liste = [a1]                        # in einer Liste werden die Werte der __repr__()-Methode dargestellt
print(liste)                        # der Standard-Output: <__main__.Auto object at 0x0000018E354986E0>

a2 = a1


# Wann wird ein Obvjekt gelöscht?
#   wenn es seine Referenzierbarkeit verliert

# Das Auto-Objekt hat 3 Referenzen:
# 1. a1 = Auto('BMW', 150)
# 2. liste = [a1]
# 3. a2 = a1

print(a1)
print(liste[0])
print(a2)

a1.beschleunigen()

print(a1)
print(liste[0])
print(a2)


# a1 = None           # Das Auto-Objekt verliert eine Referenz - verbleiben 2
# liste = []          # Das Auto-Objekt verliert eine Referenz - verbleibt 1
# a2 = None           # Das Auto-Objekt verliert seine letzte Referenz

# "die Ausführung der __del__()-Methode ist nicht in jedem Fall garantiert"


print(a1, a2)
print(a1 == a2)
print(a1 is a2)

aNeu = Auto('BMW', 150)
print(a1, aNeu)
print(a1 == aNeu)       # == macht einen inhaltlichen Wert-Vergleich - gemäß der __eq__()-Methode
print(a1 is aNeu)       # is macht einen Referenz-Vergleich


print(a1 == 'XYZ')


# TypeError: cannot use 'Auto' as a set element (unhashable type: 'Auto')
# Objekte in einem set müssen hashable sein
# hashable bedeutet: __eq__() und __hash__() müssen synchron implementiert werden
# entweder __eq__() und __hash__() sind beide NICHT implementiert
# oder BEIDE müssen implementiert werden
autoSet = {a1, a2, aNeu, Auto('Audi', 45)}
print(autoSet)

aNeu.beschleunigen()
print(autoSet)



# Welches Auto ist größer?
print(a1, aNeu)
print(a1 < aNeu)
# TypeError: '<' not supported between instances of 'Auto' and 'Auto'

# print(a1 < 'XYZ')       # TypeError: '<' not supported between instances of 'Auto' and another type


print(a1 <= aNeu)
# TypeError: '<=' not supported between instances of 'Auto' and 'Auto'


print(a1 > aNeu)            # __gt__()              oder            not __le__()
print(a1 >= aNeu)           # __ge__()                              not __lt__()
print(a1 != aNeu)           # __ne__()                              not __eq__()


print()


# + Operatotr wird realisiert durch __add__()
print(20 + 30)
print('Berlin' + '-Steglitz')
print(a1 + aNeu)
# TypeError: unsupported operand type(s) for +: 'Auto' and 'Auto'

a1 + 40
print(a1)


# * Operator wird realiisert durch __mul__()
print(10 * 5)
print('Xyz' * 5)
print(a1 * 5)
# TypeError: unsupported operand type(s) for *: 'Auto' and 'int'

# https://docs.python.org/3/reference/datamodel.html
# 3. Data Model
#	...
#	3.3 Special Mehtods

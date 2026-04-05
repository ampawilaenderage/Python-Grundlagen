#!/usr/bin/env python3


from typing import List
from abc import ABC, abstractmethod
# abc - abstact base class | abstrakte Basis-Klasse


#
# Polymorphie (poly: viel, morph: form)
#   ein Objekt kann viele Formen haben
#


#
#                      object
#                                                                               Fleischfresser
#                        Tier
#
#       Hund            Katze           Vogel               Baer
#
#                                                   Grizzly     Panda


# interface | Schnittstelle - 100% abstract
class Fleischfresser(ABC):
    @abstractmethod
    def eatMeat(self): pass


# abstract class - abstrakte Klasse => KEINE Objekterzeugung - NUR Vererbung
class Tier(ABC):

    # Gegenüberstllung: abstrakte Klasse - keine Objekterzeugung möglich
    #                                      kann konkrete Inhalte haben
    #                                      auch abstrakte Inhalte möglich
    #
    #                   konkrete Klasse  - Objeterzeugung möglich
    #                                      hat ausschließlich konkrete Inhalte
    #                                      KEINE abstrakte Inhalte möglich

    name: str

    def __init__(self, name: str):
        self.name = name
    
    # das Original - konkrete Methode
    # def eat(self):
    #     print(f'Das Tier {self.name} frisst irgendetwas')

    @abstractmethod
    def eat(self): pass

    def sleep(self):
        print(f'Das Tier {self.name} schläft')


class Hund(Tier):
    pass

    # Vererbung, Erweiterung
    #   Tier        Super-Klasse        Eltern-Klasse       allgemeinen Klasse      Oberklasse      ...
    #   Hund        Sub-Klasse          Kind-Klasse         spezifische Klasse      Unterklasse

    # Wann ist eine Vererbung sinnvoll / zu empfehlen?
    #   Frage:      IS-A                | IST-EIN
    #               is a kind of        | ist eine Art von
    #               Hund IS-A Tier?       JA

    # Klassen können auch Assoziationen (Verbindungen) miteinander eingehen
    #               HAS-A               | HAT-EIN
    #               => realisiert durch Attribute (Auto HAT-EIN Motor)

    master: str

    def __init__(self, master: str, name: str):
        super().__init__(name)
        self.master = master
    
    # hier wird die Methode eat() aus der Super-Klasse Tier überSCHRIEBEN
    # Regeln:
    # 1. der Name muss identisch sein
    # 2. die Parameter-Liste muss identisch aufrufbar sein
    #       def eat(self, food: str = ''): wäre möglich - ist aber nicht üblich !!!
    # 3. die Rückgabe (Typ/Wert) muss zum Original passen
    def eat(self):
        print(f'Der Hund {self.name} frisst Knochen')
        # super().eat()


# Mehrfachvererbung - bedeutet: eine Klasse hat DIREKT merhere Super-Klassen
#   funktioniert in             OO, C++, Python, ...
#   funktoniert nicht in        Java, PHP, C#, ...

class Katze(Tier, Fleischfresser):

    noise: str

    def __init__(self, noise: str, name: str):
        super().__init__(name)
        self.noise = noise
    
    def eat(self):
        print(f'Die Katze {self.name} schlabbert Milch')

    def eatMeat(self):
        print(f'die Katze {self.name} frisst ein Steak')


class Vogel(Tier):
    
    # Gegenüberstellung:     Eine Methode überschreibt eine konkrete Methode der Super-Klasse
    #                        Eine Methode implementiert eine abstrakte Methode der Super-Klasse

    def eat(self):
        print(f'der Vogel {self.name} pickt Körner')


# ------------------------------------------------------------------------------

class Pflanze(ABC):
    pass

class Sonnentau(Pflanze, Fleischfresser):

    def eatMeat(self):
        print('Sonnetau frisst Insekten')


class Auto(ABC):
    pass

class Christine(Auto, Fleischfresser):

    def eatMeat(self):
        print('Christine frisst Fußgänger')

# ------------------------------------------------------------------------------

print('\nhier beginnt der Zoo')

tiere: List[Tier] = [
    # Tier('Igor'),
    Hund('Eberhard', 'Waldi'),
    Katze('miau', 'Minka'),
    Vogel('Tweety'),
]

for tier in tiere:
    print(f'das Tier heißt {tier.name}')

    # if isinstance(tier, Katze):
    #     print(f'die Katze macht {tier.noise}')

    tier.eat()
    tier.sleep()


print('\nFleischfressers:')

fleischfressers: List[Fleischfresser] = [
    Katze('miau', 'Minka'),
    Sonnentau(),
    Christine(),
]

for ff in fleischfressers:
    ff.eatMeat()

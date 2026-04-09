#!/usr/bin/env python3


from typing import List


#
# Polymorphie (Vererbung)
#


class Tier:

    name: str

    def __init__(self, name: str):
        self.name = name
    
    def eat(self):
        print(f'das Tier {self.name} frist etwas')

    def sleep(self):
        print(f'das Tier {self.name} schläft')


class Hund(Tier):
    pass

    # Vererbung | Erweiterung
    #       Tier        Super-Klasse        Eltern-Klasse       Oberklasse      allgemeine Klasse
    #       Hund        Sub-Klasse          Kind-Klasse         Unterklasse     spezifische Klasse

    # Wann ist eine Vererbung sinnvoll / zu empfehlen?
    #       Frage:      IS-A            | IST-EIN
    #                   is a kind of    | ist eine Art von
    #                   Hund IS-A Tier?   JA!

    # Klasse können auch Assoziationen (Verbindungen) miteinander eingehen
    #       Frage:      HAS-A           | HAT-EIN
    #       => realisiert durch Attribute (Auto HAT-EIN Motor)

    master: str

    def __init__(self, master: str, name: str):
        super().__init__(name)
        self.master = master
    
    # überSchreiben der Methode eat() aus der Klasse Tier
    # Regeln beim ÜberSchreiben
    #   1. der Name muss identisch sein 
    #   2. die Parameter-Liste muss identisch aufrufbar sein
    #           def eat(self, food: str = ''): - wäre möglich, ist aber nicht üblich
    #   3. die Rückgabe (Typ/Wert) muss zum Original passen
    def eat(self):
        print(f'der Hund {self.name} frisst Knochen')


class Katze(Tier):

    noise: str

    def __init__(self, noise: str, name: str):
        super().__init__(name)
        self.noise = noise

# -------------------------------------------------------------------

print('\nhier beginnt der Zoo')

tiere: List[Tier] = [
    Tier('Igor'),
    Hund('Eberhard', 'Waldi'),
    Katze('miau', 'Minka'),
]

for tier in tiere:
    print(f'das Tier heißt {tier.name}')

    # if isinstance(tier, Katze):
    #     print(f'fie Katze macht {tier.noise}')

    tier.eat()
    tier.sleep()

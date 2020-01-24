from Homework.Homework17.carnivores import Carnivores


class Mammals(Carnivores):
    def __init__(self,carnivores, primates, seals, rodents, whales, herbivores):
        self._carnivores = carnivores
        self._primates = primates
        self._seals = seals
        self._rodents = rodents
        self._whales = whales
        self._herbivores = herbivores

    def mammal(self):
        return "I am from Mammals - Mammals means breast in latin"


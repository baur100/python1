
class Mammals:
    def __init__(self,carnivores, primates, seals, rodents, whales, herbivores):
        self._carnivores = carnivores
        self._primates = primates
        self._seals = seals
        self._rodents = rodents
        self._whales = whales
        self._herbivores = herbivores

    def breathe(self):
        return f"I am from Mammals - Mammals means breast in latin"


    def get_info(self):
        return f" Hello I am method  from the  Mammals  class ..... "


from Homework.Homework17.vertebrates import Vertebrates


class Carnivores (Vertebrates):
    def __init__(self, lion, wolf, blueWhale):
        self._lion = lion
        self._wolf = wolf
        self._blueWhale = blueWhale

    def carniv(self):
        return "I am from Carnivores - A carnivore is an organism that mostly eats meat, or the flesh of animals."


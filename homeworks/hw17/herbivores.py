from homeworks.hw17.mammals import Mammals
from homeworks.hw17.vertebrate import Vertebrates
from homeworks.hw17.animals import Animals
from homeworks.hw17.life import Life


class Herbivores(Mammals, Vertebrates, Animals, Life):
    type = "Herbivores"
    eat = "Plant material"

    def __init__(self, name):
        super().__init__(name)

    def __str__(self):
        return f"{self.name} are {self.type}" \
               f"they {self.eat}, and can {self.all_func()}"

from homeworks.hw17.mammals import Mammals
from homeworks.hw17.vertebrate import Vertebrates
from homeworks.hw17.animals import Animals


class Carnivores(Mammals, Vertebrates, Animals):
    type = "Mammals"

    def __init__(self, name):
        super().__init__(name)

    def __str__(self):
        return f"{self.name} are a {self.type}" \
               f"they can {self.all_func()}" \
               f"and they {self.eat()} - meat"
from homeworks.hw17.life import Life
from homeworks.hw17.mammals import Mammals
from homeworks.hw17.vertebrate import Vertebrates
from homeworks.hw17.animals import Animals

class Blue_whale(Mammals, Vertebrates, Animals, Life):
    type = "whale"
    suborder = "Mysticeti"
    length = "30 meters"

    def __init__(self, name):
        super().__init__(name)

    def __str__(self):
        return f"{self.name} is a {self.type} and {self.suborder}" \
               f"they {self.all_func()}" \
               f"their length is - {self.length}"
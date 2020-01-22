from homeworks.hw17.mammals import Mammals
from homeworks.hw17.vertebrate import Vertebrates
from homeworks.hw17.animals import Animals
from homeworks.hw17.life import Life


class Rodens(Mammals, Vertebrates, Animals,Life):
    type = "Rodens"
    order = "Rodentia"

    def __init__(self, name):
        super().__init__(name)

    def __str__(self):
        return f"{self.name} - are {self.type} of the {self.order}" \
               f"They can {self.all_func()}"
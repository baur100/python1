from homeworks.hw17.mammals import Mammals
from homeworks.hw17.vertebrate import Vertebrates
from homeworks.hw17.animals import Animals
from homeworks.hw17.life import Life


class Whales(Mammals, Vertebrates, Animals,Life):
    type = "Whale"
    group = "Aquatic"

    def __init__(self, name):
        super().__init__(name)


    def __str__(self):
        return f" The {self.name} - {self.type} - are {self.group}" \
               f"they can {self.all_func()}"

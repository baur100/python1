from homeworks.hw17.mammals import Mammals
from homeworks.hw17.vertebrate import Vertebrates
from homeworks.hw17.animals import Animals
from homeworks.hw17.life import Life


class Primates(Mammals, Vertebrates, Animals,Life):
    type = "Primates"

    def __init__(self, name):
        super().__init__(name)

    def __str__(self):
        return f"A {self.name} is a eutherian mammal constituting the taxonomic order\n" \
               f"{self.type}\n" \
               f"They can  {self.all_func()}"

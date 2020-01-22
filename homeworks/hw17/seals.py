from homeworks.hw17.mammals import Mammals
from homeworks.hw17.vertebrate import Vertebrates
from homeworks.hw17.animals import Animals
from homeworks.hw17.life import Life


class Seals(Mammals, Vertebrates, Animals,Life):
    type = "Seals"
    group = "Pinnipeds"
    mean = "Fin-footed"


    def __init__(self, name):
        super().__init__(name)

    def which(self):
        return f"{self.type} are Semiaquatic"

    def __str__(self):
        return f"They {self.all_func()}\n" \
               f" {self.type} - are {self.which()}, {Mammals} that are\n" \
               f"in a group called {self.group} - meaning {self.mean}"

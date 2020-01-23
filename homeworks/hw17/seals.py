from homeworks.hw17.mammals import Mammals


class Seals(Mammals):
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

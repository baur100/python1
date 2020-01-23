from homeworks.hw17.mammals import Mammals


class Herbivores(Mammals):
    type = "Herbivores"
    eat = "Plant material"

    def __init__(self, name):
        super().__init__(name)

    def __str__(self):
        return f"{self.name} are {self.type}" \
               f"they {self.eat}, and can {self.all_func()}"

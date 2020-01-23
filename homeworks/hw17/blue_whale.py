from homeworks.hw17.carnivores import Carnivores


class Blue_whale(Carnivores):
    type = "whale"
    suborder = "Mysticeti"
    length = "30 meters"

    def __init__(self, name):
        super().__init__(name)

    def __str__(self):
        return f"{self.name} is a {self.type} and {self.suborder}" \
               f"they {self.all_func()}" \
               f"their length is - {self.length}"

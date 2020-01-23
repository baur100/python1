from homeworks.hw17.mammals import Mammals


class Rodens(Mammals):
    type = "Rodens"
    order = "Rodentia"

    def __init__(self, name):
        super().__init__(name)

    def __str__(self):
        return f"{self.name} - are {self.type} of the {self.order}" \
               f"They can {self.all_func()}"

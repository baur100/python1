from homeworks.hw17.carnivores import Carnivores


class Lion(Carnivores):
    type = "Lion"
    family = "Felidae"
    subtype = "cat"

    def __init__(self, name):
        super().__init__(name)

    def __str__(self):
        return f"{self.name} are {self.type}" \
               f"of the family {self.family}" \
               f"of the subtype {self.subtype}" \
               f"and the can {self.all_func()}"

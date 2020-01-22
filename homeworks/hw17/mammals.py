from homeworks.hw17.vertebrate import Vertebrates


class Mammals(Vertebrates):
    type = "Mammals"

    def __init__(self, name):
        super().__init__(name)

    def __str__(self):
        return f"The {self.type} can {self.all_func()}"


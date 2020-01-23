from homeworks.hw17.mammals import Mammals


class Whales(Mammals):
    type = "Whale"
    group = "Aquatic"

    def __init__(self, name):
        super().__init__(name)


    def __str__(self):
        return f" The {self.name} - {self.type} - are {self.group}" \
               f"they can {self.all_func()}"

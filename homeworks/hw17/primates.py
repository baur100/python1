from homeworks.hw17.mammals import Mammals


class Primates(Mammals):
    type = "Primates"

    def __init__(self, name):
        super().__init__(name)

    def __str__(self):
        return f"A {self.name} is a eutherian mammal constituting the taxonomic order\n" \
               f"{self.type}\n" \
               f"They can  {self.all_func()}"

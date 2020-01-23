from HW17.mammals import Mammal
from HW17.scientific_classification import Scientific_Classification
class Rodent(Mammal, Scientific_Classification):
    def __init__(self, dep, cl, family, genus, sp, name):
        super().__init__(True)
        super().init(dep, cl, family, genus, sp, name)

    def __repr__(self):
        return f"I'm a Rodent. That's mean I don't like mouse traps.\n" \
               f"{super().__repr__()}" \
               f"{super().repr()}"

    def year(self):
        print(f"Did you know, that this year is my year???!!! ")


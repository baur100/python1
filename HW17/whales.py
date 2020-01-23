from HW17.mammals import Mammal
from HW17.scientific_classification import Scientific_Classification
class Whales(Mammal, Scientific_Classification):
    def __init__(self, dep, cl, family, genus, sp, name):
        super().__init__(True)
        super().init(dep, cl, family, genus, sp, name)

    def __repr__(self):
        return f"I'm a Whale. That's mean I live in the Ocean.\n" \
               f"{super().__repr__()}" \
               f"{super().repr()}"

    def size(self):
        print(f"I'm the biggest animal in the planet!!! ")


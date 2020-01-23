from HW17.mammals import Mammal
from HW17.scientific_classification import Scientific_Classification
class Herbivores(Mammal, Scientific_Classification):
    def __init__(self, dep, cl, family, genus, sp, name):
        super().__init__(True)
        super().init(dep, cl, family, genus, sp, name)

    def __repr__(self):
        return f"I'm a Herbivore. That's mean I eat grass.\n" \
               f"{super().__repr__()}" \
               f"{super().repr()}"

    def sound(self):
        print(f" MUUUUUUU")


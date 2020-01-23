from HW17.mammals import Mammal
from HW17.scientific_classification import Scientific_Classification
class Primates(Mammal, Scientific_Classification):
    def __init__(self, dep, cl, family, genus, sp, name):
        super().__init__(True)
        super().init(dep, cl, family, genus, sp, name)

    def __repr__(self):
        return f"I'm a Primate. That's mean I'm a monkey.\n" \
               f"{super().__repr__()}" \
               f"{super().repr()}"

    def eat(self):
        print(f"Banana! Banana! I'm not a minion, but.... BANANA!!!")


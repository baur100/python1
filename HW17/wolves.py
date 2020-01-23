from HW17.carnivores import Carnivores
from HW17.scientific_classification import Scientific_Classification
class Wolves(Carnivores, Scientific_Classification):
    def __init__(self, dep, cl, family, genus, sp, name):
        super().__init__()
        super().init(dep, cl, family, genus, sp, name)

    def __repr__(self):
        return f"I'm a Wolve. That's mean I live in a forest.\n" \
               f"{super().__repr__()}" \
               f"{super().repr()}"

    def moon(self):
        print(f"MOON! WOW WOW WOW!WOOOOOOOOOO! ")


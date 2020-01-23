from HW17.mammals import Mammal
from HW17.scientific_classification import Scientific_Classification
class Seals(Mammal, Scientific_Classification):
    def __init__(self, dep, cl, family, genus, sp, name):
        super().__init__(True)
        super().init(dep, cl, family, genus, sp, name)

    def __repr__(self):
        return f"I'm a Seal. That's mean I love to lay down, and sleep. \n" \
               f"{super().__repr__()}" \
               f"{super().repr()}"

    def eatFish(self):
        print(f"Fish!!! I eat Fish!!! A lot of Fish!!!")


from HW17.carnivores import Carnivores
from HW17.scientific_classification import Scientific_Classification
class BlueWhales(Carnivores, Scientific_Classification):
    _weight=0
    def __init__(self, dep, cl, family, genus, sp, name):
        super().__init__()
        super().init(dep, cl, family, genus, sp, name)

    @property
    def weight(self):
        return f"I weight {self._weight} lb."

    @weight.setter
    def weight(self, value):
        self._weight=value

    def __repr__(self):
        return f"I'm a Lion. That's mean I live in a prepie.\n" \
               f"{super().__repr__()}" \
               f"{super().repr()}"

    def change_weight(self, w):
        if w<500:
            raise ValueError("I'm tooo light!!!")
        self._weight= w
        print(f"My weight is now {w} lb.!!! ")


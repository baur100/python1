from HW17.carnivores import Carnivores
from HW17.scientific_classification import Scientific_Classification
class Lions(Carnivores, Scientific_Classification):
    _number_wives=0
    def __init__(self, dep, cl, family, genus, sp, name):
        super().__init__()
        super().init(dep, cl, family, genus, sp, name)

    @property
    def number_of_wifes(self):
        return f"I have garem of {self._number_wives} lioness"

    @number_of_wifes.setter
    def number_of_wifes(self, value):
        self._number_wives=value

    def __repr__(self):
        return f"I'm a Lion. That's mean I live in a prepie.\n" \
               f"{super().__repr__()}" \
               f"{super().repr()}"

    def sound(self):
        print(f"Roaaaaar!!! ")


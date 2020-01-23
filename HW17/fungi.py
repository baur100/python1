from HW17.life import Life
from HW17.scientific_classification import Scientific_Classification

class Fungi(Life, Scientific_Classification):
    _one_cell=True
    _mycelium=""
    # _division=""
    # _clas=""
    # _family=""
    # _genus=""
    # _species=""
    # _name=""
    eatable=""

    def __init__(self, one_cell, mycelium, dep, cl, family, genus, sp, name):
        super().__init__( ["organic"], "", True, "top", ("silence"), "spore", 1)
        self._one_cell=one_cell
        self._mycelium=mycelium
        super().init(dep, cl, family, genus, sp, name)

    @property
    def one_cell(self):
        if self._one_cell:
            return "I'm unicellular"
        else:
            return "I'm multicellular"

    @one_cell.setter
    def one_cells(self, value):
        self._one_cell=value

    @property
    def mycelium(self):
        return f"I have mycelium. Ha!"

    @mycelium.setter
    def mycelium(self, value):
        self._mycelium=value
    @property
    def division(self):
        return f"Division: {self._division}\n"

    def __repr__(self):
        return f"I'm a Fungi. That's mean {super().__repr__()}\n" \
               f"{self.one_cell}, {self.mycelium} " \
               f"\n{super().repr()}\n" \


    def eat_me(self):
        self.eatable=input("Specify if you can eat me and in what condition:")

    def print_eatable(self):
        print(self.eatable)

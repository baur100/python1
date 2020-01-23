from HW17.vertebrates import Vertebrates
class Mammal(Vertebrates):
    _tail=True

    def __init__(self, tail):
        super().__init__({"digestive", "breathing", "circulatory", "nervous", "excretory"}, "run", ["meat", "grass"], "metabolism", True, "getting bigger", "bite", "viviparous", 100)
        self._tail=tail

    @property
    def tail(self):
        if self._tail:
            return f"I have a tail "

    @tail.setter
    def tail(self, value):
       self._tail=value

    def __repr__(self):
        return f"I'm a Mamnmal. That's mean I'm born alive, not in the egg.\n" \
               f" {self.tail}" \
               f"{super().__repr__()}"

    def get_info(self):
        raise NotImplemented("Can't be initiated as an object")

    def drink(self):
        print(f"I drink my mom's milk. Yammm!")

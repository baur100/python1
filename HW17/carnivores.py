from HW17.mammals import Mammal
class Carnivores(Mammal):
    def __init__(self):
        super().__init__(True)

    def __repr__(self):
        return f"I'm a Carnivore. That's mean I love animals .... to eat.\n" \
               f"{super().__repr__()}"

    def get_info(self):
        raise NotImplemented("Can't be initiated as an object")

    def hunt(self, prey):
        print(f"I hunt today and got a delicious lunch: {prey}!")


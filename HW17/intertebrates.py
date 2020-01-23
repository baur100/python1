from HW17.animal import Animal
class Invertebrates(Animal):
    _skeleton=False

    def __init__(self, organs, move, nutrition, metabolism, breath, growth, irritability, reproduction, death):
        super().__init__(organs, move, nutrition, metabolism, breath, growth, irritability, reproduction, death)

    def __repr__(self):
        return f"I'm a Invertebrate Animal because I don't have a skeleton. \n" \
               f"{super().__repr__()}"

    def get_info(self):
        raise NotImplemented("Can't be initiated as an object")


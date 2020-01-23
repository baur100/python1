from HW17.animal import Animal
class Vertebrates(Animal):
    _skeleton=True

    def __init__(self, organs, move, nutrition, metabolism, breath, growth, irritability, reproduction, death):
        super().__init__(organs, move, nutrition, metabolism, breath, growth, irritability, reproduction, death)

    def __repr__(self):
        return f"I'm a Vertebrate Animal because I have skeleton. \n" \
               f"{super().__repr__()}"

    def get_info(self):
        raise NotImplemented("Can't be initiated as an object")

    def Ihave_skeleton(self):
        print("I have a skeleton!!! ha -ha -ha ")



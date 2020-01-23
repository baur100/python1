from HW17.life import Life

class Animal(Life):
    _organs={}
    _move=""


    def __init__(self, organs, move, nutrition, metabolism, breath, growth, irritability, reproduction, death):
        super().__init__(nutrition, metabolism, breath, growth, irritability, reproduction, death)
        self._organs = organs
        self._move = move

    @property
    def organs(self):
        return self._organs

    @organs.setter
    def organs(self, value):
        self._organs=value

    @property
    def move(self):
        return f"I can move by  {self._move}"

    @move.setter
    def move(self, value):
        self._move=value

    def __repr__(self):
        return f"I'm an Animal. That's mean I have organs: \n" \
               f"{self.organs}\n and {self.move}\n" \
               f"{super().__repr__()}"

    def get_info(self):
        raise NotImplemented("Can't be initiated as an object")

    def Im_moving(self):
        print("I can move")


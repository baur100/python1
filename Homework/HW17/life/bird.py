from Homework.HW17.life.vertebrate import Vertebrate
from Homework.HW17.life.animal import Animal

class Bird(Vertebrate, Animal):
    type = "bird"

    def __init__(self, name):
        super().__init__(name)

    def feather(self):
        return "I have feathers"

    def __str__(self):
        return f"*************************\n" \
            f"Hi! I am a {self._name}.\nAs a living being I can {self.breathe()}, {self.eat()}, {self.spawn()}.\n" \
            f"As an {Animal.type} I can {self.think()}.\n" \
            f"As a {Vertebrate.type} {self.backbone()}.\n" \
            f"As an {self.type} {self.feather()}."



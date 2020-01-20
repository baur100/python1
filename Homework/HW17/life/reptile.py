from Homework.HW17.life.vertebrate import Vertebrate
from Homework.HW17.life.animal import Animal

class Reptile(Vertebrate, Animal):
    type = "reptile"

    def __init__(self, name):
        super().__init__(name)

    def cold_blood(self):
        return "I am cold blooded"

    def __str__(self):
        return f"*************************\n" \
            f"Hi! I am a {self._name}.\nAs a living being I can {self.breathe()}, {self.eat()}, {self.spawn()}.\n" \
            f"As an {Animal.type} I can {self.think()}.\n" \
            f"As a {Vertebrate.type} {self.backbone()}.\n" \
            f"As a {self.type} {self.cold_blood()}."



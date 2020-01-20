from Homework.HW17.life.vertebrate import Vertebrate
from Homework.HW17.life.animal import Animal

class Fish(Vertebrate, Animal):
    type = "fish"

    def __init__(self, name):
        super().__init__(name)

    def live(self):
        return "I live in water"

    def __str__(self):
        return f"*************************\n" \
            f"Hi! I am a {self._name}.\n" \
            f"As a living being I can {self.breathe()}, {self.eat()}, {self.spawn()}.\n" \
            f"As an {Animal.type} I can {self.think()}. As a {Vertebrate.type} {self.backbone()}.\n" \
            f"As a {self.type} {self.live()}."



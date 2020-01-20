from Homework.HW17.life.vertebrate import Vertebrate
from Homework.HW17.life.animal import Animal
from Homework.HW17.life.mammal import Mammal

class Rodent(Mammal, Vertebrate, Animal):
    type = "rodent"

    def __init__(self, name):
        super().__init__(name)

    def teeth(self):
        return "I have ever growing teeth"

    def __str__(self):
        return f"*************************\n" \
            f"Hi! I am a {self._name}.\n" \
            f"As a living being I can {self.breathe()}, {self.eat()}, {self.spawn()}.\n" \
            f"As an {Animal.type} I can {self.think()}.\n" \
            f"As a {Vertebrate.type} {self.backbone()}.\n" \
            f"As a {Mammal.type} {self.milk()}.\n" \
            f"As a {self.type} {self.teeth()}."




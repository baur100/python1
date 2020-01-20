from Homework.HW17.life.animal import Animal

class Vertebrate(Animal):
    type = "vertebrate"

    def __init___(self, name):
        super().__init__(name)

    def backbone(self):
        return "I have backbone"

    def __str__(self):
        return f"*************************\n" \
            f"Hi! I am a {self._name}. As a living being I can {self.breathe()}, {self.eat()}, {self.spawn()}.\n" \
            f"As an {Animal.type}, I can {self.think()}.\n" \
            f"As a {self.type} {self.backbone()}"


from Homework.HW17.life.life import Life


class Plant(Life):
    type = "plant"

    def __init__(self, name):
        super().__init__(name)

    def breathe(self):
        return "breathe"

    def eat(self):
        return "eat"

    def spawn(self):
        return "spawn"

    def photosynthesis(self):
        return "do photosynthesis and use carbon dioxide"

    def __str__(self):
        return f"*************************\n" \
            f"Hi! I am a {self._name}.\n" \
            f"As a living organism I can {self.breathe()}, {self.eat()}, {self.spawn()}.\n" \
            f"As a {self.type} I can {self.photosynthesis()}."

    # @property
    # def name(self):
    #     return self._name
    #
    # @name.setter
    # def name(self, value):
    #     self._name = value
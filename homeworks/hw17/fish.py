from homeworks.hw17.vertebrate import Vertebrates
from homeworks.hw17.life import Life


class Fish(Vertebrates,Life):
    type = "Fish"

    def __init__(self, name):
        super().__init__(name)

    def __str__(self):
        return f"{self.name} is a {self.type}\n" \
               f"they {self.all_func()} and glow under a certain light conditions"

from homeworks.hw17.life import Life


class Animals(Life):
    type = "Animals"

    def __init__(self, name):
        super().__init__(name)

    def snake(self):
        return f"{self.name}"

    def __str__(self):
        return f"{self.type} {self.name} can {self.proliferate()}\n" \
               f"as well as {self.see()} and {self.breathe()}\n" \
               f"and they {self.proliferate()} sexually"

    def shed(self):
        return f"{self.name} sheds every 4-6 weeks"

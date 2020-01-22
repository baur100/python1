from homeworks.hw17.animals import Animals


from homeworks.hw17.animals import Animals


class Invertebrates(Animals):
    type = "Invertebrate"

    def __init__(self, name):
        super().__init__(name)

    def bone(self):
        return "Not having a backbone"

    def info(self):
        return f"being a {self.type} means {self.bone()}\n" \
               f"and it can {self.all_func()}"
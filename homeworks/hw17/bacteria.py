from homeworks.hw17.life import Life


class Bacteria(Life):
    def __init__(self, name):
        super().__init__(name)

    def proliferate(self):
        return "Binary fiction"

    def __all_info__(self):
        return f"Being a {self.name},\n" \
               f"I reproduce by {self.proliferate()}"
from homeworks.hw17.life import Life


class Fungi(Life):
    def __init__(self, name):
        super().__init__(name)

    def proliferate(self):
        return f"{self.proliferate()}" \
               f"fragmentation, budding or producing spores"

    def __all_info__(self):
        return f" {self.name},\n" \
               f"It can {self.all_func()}\n" \
               f"and {self.proliferate()}"

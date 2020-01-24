from Homework.Homework17.life import Life


class Animals(Life):
    def __init__(self, vertebrates, invertebrates):
        self._vertebrates = vertebrates
        self._invertebrates = invertebrates

    def breathe(self):
        return "we breathe class Animals"

    def swim(self):
        return " we swim class Animals"

    def fly(self):
        return " we fly class Animals"

    def run(self):
        return "we run class Animals"

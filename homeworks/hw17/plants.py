from homeworks.hw17.life import Life


class Plants(Life):
    type = "Plants"

    def __init__(self, name):
        super().__init__(name)

    def __str__(self):
        return f"This is {self.name}, as a {type}\n" \
               f"{type} {self.proliferate()} - asexually, through cultivation, and\n" \
               f" sexually, through the exchange of pollen between\n" \
               f" male and female reproductive systems.\n" \
               f" A single tree can produce both male and female flowers,\n" \
               f" relying on adaptations such as different\n" \
               f" blooming times to prevent self-pollination."

    def produce(self):
        return "Trees produce oxygen"


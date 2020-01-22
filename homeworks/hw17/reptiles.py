from homeworks.hw17.vertebrate import Vertebrates

class Reptiles(Vertebrates):
    type = "Reptiles"

    def __init__(self, name):
        super().__init__(name)

    def __str__(self):
        return f"{self.type} - are tetrapod animals,\n" \
               f"they can {self.all_func()}\n" \
               f"and {self.proliferate()} sexually."

    def crawl(self):
        return f"They {self.crawl()}"

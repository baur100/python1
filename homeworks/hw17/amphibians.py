from homeworks.hw17.vertebrate import Vertebrates


class Amphibians(Vertebrates):
    type = "Amphibians"

    def __init__(self, name):
        super().__init__(name)

    def __str__(self):
        return f"As a {self.type} they cay {self.all_func()}\n" \
               f"and they could survive in the water or outside"

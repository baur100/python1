from homeworks.hw17.vertebrate import Vertebrates


class Birds(Vertebrates):
    type = "Birds"

    def __init__(self, name):
        super().__init__(name)

    def __str__(self):
        return f"{self.name} are {self.type}\n" \
               f"they {self.all_func()} as others, their habitat usually in cold temperatures"
    
from Homework.Homework17.Animals import Animals


class Vertebrates:

    def __init__(self, fish, amphibians, birds, mammals):
        self._fish = fish
        self._amphibians = amphibians
        self._birds = birds
        self._mammals = mammals

    def breathe(self):
        return f"I am from Vertebrates class Nearly half of all vertebrates are fish. "

    def get_info(self):
        return f" Hello I am method  from the  Vertebrates  class.....  "

# we_can_swim = Animals(1,2)
# print(we_can_swim.swim())
#
# we_can_fly = Animals(1,2)
# print(we_can_fly.fly())


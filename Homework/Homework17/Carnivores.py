from Homework.Homework17.Animals import Animals


class Carnivores:
    def __init__(self, lion, wolf, blueWhale):
        self._lion = lion
        self._wolf = wolf
        self._blueWhale = blueWhale

    def breathe(self):
        return f"I am from Carnivores - A carnivore is an organism that mostly eats meat, or the flesh of animals."

    def get_info(self):
        return f" Hello I am method  from the  Carnivores  class representing animals like  {self._lion},{self._wolf}, {self._blueWhale}  "


# can_swim = Animals("whale", "shark")
# print(can_swim.swim())
#
# can_run = Animals("tiger", "horse")
# print(can_run.run())

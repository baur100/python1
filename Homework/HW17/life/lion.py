from Homework.HW17.life.vertebrate import Vertebrate
from Homework.HW17.life.animal import Animal
from Homework.HW17.life.mammal import Mammal
from Homework.HW17.life.carnivore import Carnivore

class Lion(Carnivore):
    type = "lion"

    def __init__(self, name, age, gender):
        super().__init__(name)
        self._age = age
        self._gender = gender

    def africa(self):
        return "I live in Africa"

    def __str__(self):
        return f"*************************\nHi! I am a {self._name}. As a living being I can {self.breathe()}, {self.eat()}, {self.spawn()}.\n" \
            f"As a {Animal.type} I can {self.think()}.\n" \
            f"As a {Vertebrate.type} {self.backbone()}.\n" \
            f"As a {Mammal.type} {self.milk()}.\n" \
            f"As a {Carnivore.type} {self.meat()}\n" \
            f"As a {self.type} {self.africa()}.\n" \
            f"I am {self.age} years old and I am a {self.gender}."

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        self._age = value

    @property
    def gender(self):
        return self._gender

    @gender.setter
    def gender(self, value):
        self._gender = value




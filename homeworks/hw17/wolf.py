from homeworks.hw17.life import Life
from homeworks.hw17.carnivores import Carnivores
from homeworks.hw17.mammals import Mammals
from homeworks.hw17.vertebrate import Vertebrates
from homeworks.hw17.animals import Animals


class Wolf(Carnivores, Mammals, Vertebrates, Animals, Life):
    type = "Wolf"
    male_weight = "40 kg"
    female_weight = "37kg"
    len = "105-160cm"

    def __init__(self, name):
        super().__init__(name)

    def __str__(self):
        return f"{self.name} - are {self.type}" \
               f"male weight is -{self.male_weight}" \
               f"and female weight is - {self.female_weight}" \
               f"their length is - {self.len}" \
               f"and they can {self.all_func()}"

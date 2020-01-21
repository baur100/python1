from Homework.Homework17.Animals import Animals
from Homework.Homework17.Life import Life
from Homework.Homework17.Vertebrates import Vertebrates
from Homework.Homework17.Mammals import Mammals
from Homework.Homework17.Carnivores import Carnivores

all_life = Life(1, 1, 1, 1)
tiger = Carnivores("тигр", " волк", "акула")
fox = Vertebrates(1, 2, 3, 4)
human = Mammals(1, 2, 3, 4, 5, 6)
all_animals = Animals(1, 2)

print(all_life.get_info())
print(tiger.get_info())
print((fox.get_info()))
print(human.get_info())
print(all_animals.get_info())

print(all_life.breathe())
print(tiger.breathe())
print((fox.breathe()))
print(human.breathe())
print(all_animals.breathe())

can_swim = Animals("whale", "shark")
print(can_swim.swim())

can_run = Animals("tiger", "horse")
print(can_run.run())

we_can_fly = Animals("eagle", "ворона")
print(we_can_fly.fly())

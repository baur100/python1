from Homework.HW17.life.fungi import Fungi
from Homework.HW17.life.bacteria import Bacteria
from Homework.HW17.life.plant import Plant
from Homework.HW17.life.animal import Animal
from Homework.HW17.life.vertebrate import Vertebrate
from Homework.HW17.life.invertebrate import Invertebrate
from Homework.HW17.life.reptile import Reptile
from Homework.HW17.life.fish import Fish
from Homework.HW17.life.amphibian import Amphibian
from Homework.HW17.life.bird import Bird
from Homework.HW17.life.mammal import Mammal
from Homework.HW17.life.carnivore import Carnivore
from Homework.HW17.life.primate import Primate
from Homework.HW17.life.seal import Seal
from Homework.HW17.life.rodent import Rodent
from Homework.HW17.life.whale import Whale
from Homework.HW17.life.herbivore import Herbivore
from Homework.HW17.life.lion import Lion
from Homework.HW17.life.wolf import Wolf
from Homework.HW17.life.blue_whale import BlueWhale

mushroom = Fungi("mushroom")
lactobacteria = Bacteria("lactobacteria")
pine = Plant("pine")
horse = Animal("horse")
koala = Vertebrate("koala")
mollusk = Invertebrate("mollusk")
snake = Reptile("snake")
salmon = Fish("salmon")
frog = Amphibian("frog")
owl = Bird("owl")
cow = Mammal("cow")
tiger = Carnivore("tiger")
chimpanzee = Primate("chimpanzee")
sea_lion = Seal("sea lion")
mouse = Rodent("mouse")
bowhead_whale = Whale("bowhead whale")
deer = Herbivore("deer")

congo_lion = Lion("Congo lion", 12, "female")
grey_wolf = Wolf("grey wolf", 5, "male")
blue_whale = BlueWhale("blue whale", 2, "male")

living_being_list = [mushroom, lactobacteria, pine, horse, koala, mollusk, snake, salmon, frog, owl, cow, tiger, chimpanzee, sea_lion, mouse, bowhead_whale, deer, congo_lion, grey_wolf, blue_whale]

# We can print info about all species from the list
# for species in living_being_list:
#     print(species)

# We can pick any species from the list and print info about it
print(grey_wolf)
print(congo_lion)
print(blue_whale)

#We can print any characteristic of the species separately
print(f"Grey wolf gender: {grey_wolf.gender}")
print(f"Congo lion age: {congo_lion.age}")
print(f"Blue whale weight: {blue_whale.weight}")




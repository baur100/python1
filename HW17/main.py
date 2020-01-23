
from HW17.fungi import Fungi
from HW17.bacteria import Bacteria
from HW17.reptilies import Reprilies
from HW17.fish import Fish
from HW17.amphibians import Amphibians
from HW17.bird import Bird
from HW17.primates import Primates
from HW17.seals import Seals
from HW17.rodents import Rodent
from HW17.whales import Whales
from HW17.herbivores import Herbivores
from HW17.lions import Lions
from HW17.wolves import Wolves
from HW17.blueWhale import BlueWhales


# 1. проект царство животных
# =======================
# Each class must have specific method!
# Example
# def breathe:
#     return f"I can breathe"
# Class - Life
# in Life
#     Fungi
#     Bacteria
#     Plants
#     Animals
# in Animals
#     Vertebrates
#     Invertebrates
# in Vertebrates
#     Reptilies
#     Fish
#     Amphibians
#     Birds
#     Mammals
# in Mammals
#     Carnivores
#     Primates
#     Seals
#     Rodents
#     Whales
#     Herbivores
# in Carnivores
#
# class - Lion
# class - Wolf
# class - BlueWhale
#
# придумайте по краней мере один метод для каждого класса в иерархии
# начиная от Life и реализуйте их в трех классах, вызовите все методы
#
# инстаншиируйте объекты всех трех классов;
#
# 2 Создайте класс Farm
# у фермы есть земля, скот, техника (трактора)
# когда мы складываем две фермы - все имущество складывается
# придумайте еще 2 других __метода__ которые можно применить к ферме

mashroom = Fungi(True, "", "Basidiomycota", "Agaricomycetes", "Boletaceae", "Leccinum", "Leccinum Scabrum", "Birch Bolete")
print(mashroom)
# mashroom.eat_me()
# mashroom.print_eatable()
print("---------------")
bacteria=Bacteria("parasite",  "spirillas", "", "Betaproteobacteria" , "Spirillaceae", "Spirillum", "Spirillum minus", "Fever")
print(bacteria)
print(f"My shape is {bacteria.form} which is {bacteria.explaining_form()}")
print("--------------")
lizard=Reprilies("scales", "Chirdata", "Reptilia", "Afamidae", "Pogona", "Pogona Vitticeps", "Bearded Dragon")
print(lizard)
print("-----------------------")
print("Since I'm a living organism, ", end="")
lizard.Im_alive()
print("Since I'm an Animal, ", end="")
lizard.Im_moving()
print("Since I'm a vertebrate, ", end="")
lizard.Ihave_skeleton()
print("And since I'm a reptile, ", end="")
lizard.my_digestive_system()
print("-------------------")
Dory=Fish(True, "Chordata", "Actinopterygii", "Acanthurinae", "Paracanthurus", "Paracanthurus hepatus", "Dory")
print(Dory)
print("-----------------------")
print("Since I'm a living organism, ", end="")
Dory.Im_alive()
print("Since I'm an Animal, ", end="")
Dory.Im_moving()
print("Since I'm a vertebrate, ", end="")
Dory.Ihave_skeleton()
print("And since I'm a fish, ", end="")
Dory.swim()
print("-------------------")
frog=Amphibians("kva", "Chordata", "Amphibia", "Ranidae", "Lithobates", "Lithobates clamitans", "Green Frog")
print(frog)
print("-----------------")
print("Since I'm a living organism, ", end="")
frog.Im_alive()
print("Since I'm an Animal, ", end="")
frog.Im_moving()
print("Since I'm a vertebrate, ", end="")
frog.Ihave_skeleton()
print("And since I'm a amphibian, ", end="")
frog.tongue()
print("-------------------")
bird=Bird("Chordata", "Aves", "Psittacidae", "Arini", "Ara", "Peanut")
print(bird)
print("-----------------")
print("Since I'm a living organism, ", end="")
bird.Im_alive()
print("Since I'm an Animal, ", end="")
bird.Im_moving()
print("Since I'm a vertebrate, ", end="")
bird.Ihave_skeleton()
print("And since I'm a bird, ", end="")
bird.fly()
print("-------------------")
monkey=Primates("Chordata", "Mammalia", "Simiiformes", "Cebinae", "Cebus", "Capuchin")
print(monkey)
print("-----------------")
print("Since I'm a living organism, ", end="")
monkey.Im_alive()
print("Since I'm an Animal, ", end="")
monkey.Im_moving()
print("Since I'm a vertebrate, ", end="")
monkey.Ihave_skeleton()
print("Since I'm a mammal, ", end="")
monkey.drink()
print("And since I'm a Primate, ", end="")
monkey.eat()
print("-----------------")

seal=Seals("Chordata", "Mammalia", "Otariidae", "Callorhinus", "Callorhinus ursinus", "Northern Fur Seal")
print(seal)
print("-----------------")
print("Since I'm a living organism, ", end="")
seal.Im_alive()
print("Since I'm an Animal, ", end="")
seal.Im_moving()
print("Since I'm a vertebrate, ", end="")
seal.Ihave_skeleton()
print("Since I'm a mammal, ", end="")
seal.drink()
print("And since I'm a seal, ", end="")
seal.eatFish()
print("-----------------")

rat=Rodent("Chordata", "Mammalia", "Muridae", "Mus", "Mus musculus", "Jerry")
print(rat)
print("-----------------")
print("Since I'm a living organism, ", end="")
rat.Im_alive()
print("Since I'm an Animal, ", end="")
rat.Im_moving()
print("Since I'm a vertebrate, ", end="")
rat.Ihave_skeleton()
print("Since I'm a mammal, ", end="")
rat.drink()
print("And since I'm a rodent, ", end="")
rat.year()
print("-----------------")

whale=Whales("Chordata", "Mammalia", "Delphinidae", "Orcinus", "Orcinus Orca", "Willy")
print(whale)
print("-----------------")
print("Since I'm a living organism, ", end="")
whale.Im_alive()
print("Since I'm an Animal, ", end="")
whale.Im_moving()
print("Since I'm a vertebrate, ", end="")
whale.Ihave_skeleton()
print("Since I'm a mammal, ", end="")
whale.drink()
print("And since I'm a Whale, ", end="")
whale.size()
print("-----------------")

cow=Herbivores("Chordata", "Mammalia", "Bovinae", "Bos", "Bos Taurus", "Cattle or Cow")
print(cow)
print("-----------------")
print("Since I'm a living organism, ", end="")
cow.Im_alive()
print("Since I'm an Animal, ", end="")
cow.Im_moving()
print("Since I'm a vertebrate, ", end="")
cow.Ihave_skeleton()
print("Since I'm a mammal, ", end="")
cow.drink()
print("And since I'm a Herbivore, ", end="")
cow.sound()
print("-----------------")

lion=Lions("Chordata", "Mammalia", "Felidae", "Panthera", "Panthera Leo", "Simba")
print(lion)
print("-----------------")
print("Since I'm a living organism, ", end="")
lion.Im_alive()
print("Since I'm an Animal, ", end="")
lion.Im_moving()
print("Since I'm a vertebrate, ", end="")
lion.Ihave_skeleton()
print("Since I'm a mammal, ", end="")
lion.drink()
print("And since I'm a Lion, ", end="")
lion.sound()
print("-----------------")

wolf=Wolves("Chordata", "Mammalia", "Canidae", "Canis", "Canis Lupus", "Akella")
print(wolf)
print("-----------------")
print("Since I'm a living organism, ", end="")
wolf.Im_alive()
print("Since I'm an Animal, ", end="")
wolf.Im_moving()
print("Since I'm a vertebrate, ", end="")
wolf.Ihave_skeleton()
print("Since I'm a mammal, ", end="")
wolf.drink()
print("And since I'm a wolf, ", end="")
wolf.moon()
print("-----------------")

blueWhale=BlueWhales("Chordata", "Mammalia", "Balaenopteridae", "Balaenopteridae", "Balaenoptera musculus", "Blue Whale")
print(blueWhale)
print("-----------------")
print("Since I'm a living organism, ", end="")
blueWhale.Im_alive()
print("Since I'm an Animal, ", end="")
blueWhale.Im_moving()
print("Since I'm a vertebrate, ", end="")
blueWhale.Ihave_skeleton()
print("Since I'm a mammal, ", end="")
blueWhale.drink()
print("And since I'm a Blue Whale, ", end="")
blueWhale.change_weight(38000)
print("-----------------")

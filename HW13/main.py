from HW13.pokemon import Pokemon
from HW13.panda import Panda
from HW13.fractions import Fraction

p1 = Pokemon()
p1.name="Pikachu"
p1.abilities=["static", "lightning rod"]
p1.type = "Electric"
p1.species = "Mouse Pokemon"
p1.hp=35
p1.generation=1

p1.print_info()
print("-----------")
try:
    p1.attack("storm")
except TypeError:
    print("wrong Type  entered")
except ValueError:
    print("Wrong ability")

p1.attack("lightning rod")
p1.hp=40
print("-----------")
p2=Pokemon()
p2.name="Charmander"
p2.abilities=["blaze", "solar power"]
p2.type = "Fire"
p2.species = "Lizard Pokemon"
p2.hp=40
p2.generation=1

p2.print_info()
print("-----------")
print(f"This Pokemon is {p2.get_name()}")
p2.add_abilities("flames")
print("Abilities: ", end="")
i=0
while i<(len(p2.abilities)-1):
    print(f"{p2.abilities[i]}, ", end="")
    i+=1
print(f"and {p2.abilities[i]}")
print("Done with Pokemons...... :-)")
print("")


panda1=Panda()
panda1.name="Masha"
panda1.weight=130
panda1.age=10
panda1.kids=2
panda1.country="China"

panda1.print_info()
try:
    panda1.gain_weight(270)
except ValueError:
    print("Wrong gain mass value.")
panda1.gain_weight(50)
print(f"{panda1.get_name()}'s weight is {panda1.weight}")
print("--------------")
panda2=Panda()
panda2.name="Alex"
panda2.weight=190
panda2.age=6
panda2.country="Australia"

panda2.print_info()
panda2.change_age()
print("One year later......")
panda2.kids=1
panda2.gain_weight(100)
panda2.print_info()

print("----------------------------------------------")

fr1=Fraction()
fr1.denominator=5
fr1.numerator=4
fr1.print_fraction()
print("We add 2/3 to the fraction:")
fr1.add_fraction(2, 3)
fr1.print_fraction()
if fr1.check_ProperFr():
    print(f"fraction is a proper fraction")
else:
    print("Fraction is improper")
print("")
fr2=Fraction()
fr2.whole=5
fr2.numerator=1
fr2.denominator=3
fr2.print_fraction()
fr2.add_whole(3)
print("We add 3")
fr2.print_fraction()
try:
    fr2.change_den(0)
except ZeroDivisionError:
    print("Denominator cannot be 0!!!!")
fr2.change_den(7)

fr2.print_fraction()
fr2.numerator=11
fr2.print_fraction()
if fr2.isFraction():
    print("This is a fractional number")
else:
    print("Is not a fraction")



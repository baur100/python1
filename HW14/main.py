from HW14.pokemon import Pokemon
from HW14.panda import Panda
from HW14.fractions import Fraction

p1 = Pokemon("Pikachu", "Electric", 1, "Mouse Pokemon", ["static", "lightning rod"], 35)
print("Use p1.print_info():")
p1.print_info()
print("-----------")
try:
    p1.attack("storm")
except TypeError:
    print("wrong Type  entered")
except ValueError:
    print("Wrong ability")
print("-------------")
print("Use print(p1):")
print(p1)
print("----------")
p1.attack("lightning rod")
p1.hp=40
print("-----------")

p2=Pokemon("Charmander", "Fire", 1, "Lizard Pokemon", ["blaze", "solar power"], 40)

print(p2)
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


panda1=Panda("Masha", 130, 10, 2, "China")
print("Use panda1.print_info():")
panda1.print_info()
print("-----------------")
try:
    panda1.gain_weight(270)
except ValueError:
    print("Wrong gain mass value.")
panda1.gain_weight(50)
print(f"{panda1.get_name()}'s weight is {panda1.weight}")
print("--------------")
print("Use print(panda1):")
print(panda1)
print("-------------")
panda2=Panda("Alex", 190, 6, 0, "Australia")
print(panda2)
panda2.change_age()
print("One year later......")
panda2.kids=1
panda2.gain_weight(100)
panda2.print_info()

print("----------------------------------------------")

fr1=Fraction(0, 5, 4)
fr1.print_fraction()
print("Use print(fr1):", end="")
print(fr1)

print("We add 2/3 to the fraction:")
fr1.add_fraction(2, 3)
fr1.print_fraction()
if fr1.check_ProperFr():
    print(f"fraction is a proper fraction")
else:
    print("Fraction is improper")
print("")
fr2=Fraction(5, 1, 3)
print(fr2)
fr2.add_whole(3)
print("We add 3")
print(fr2)
try:
    fr2.change_den(0)
except ZeroDivisionError:
    print("Denominator cannot be 0!!!!")
fr2.change_den(7)

print(fr2)
fr2.numerator=11
print(fr2)
if fr2.isFraction():
    print("This is a fractional number")
else:
    print("Is not a fraction")

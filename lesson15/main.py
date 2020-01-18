from lesson15.car import Car
from lesson15.person import Person

volvo = Car(4,"x-90","Volvo")
volvo.year = 199
print(volvo)

volvo.set_year(2020)
print(volvo)
#
print(volvo.get_year())

volvo.year = 1979
print(volvo.year)

print(volvo.__dict__)

vasya = Person()
print(vasya)

vasya.first_name = "Vasya"
vasya.last_name = "Bukin"
vasya.year = 1930

print(vasya)
print(vasya.__dict__)


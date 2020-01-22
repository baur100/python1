from homeworks.hw17.farm.farm import Farm

the_farm1 = Farm("Crack", 15000, "goats", "Tractors")
print(the_farm1)
the_farm2 = Farm("Pied piper", 10000, "Cows", "Trucks")
print(the_farm2)

# __add__
added_farm = the_farm1 + the_farm2
print(added_farm)

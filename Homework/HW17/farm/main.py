from Homework.HW17.farm.farm import Farm

my_farm1 = Farm("Florida Farm",934, 300, 20)
print(my_farm1)

my_farm2 = Farm("Georgia Farm",1050, 199, 15)
print(my_farm2)

new_farm = my_farm1 + my_farm2

print(new_farm)
print(f"Farm acreage is {len(new_farm)} acres")

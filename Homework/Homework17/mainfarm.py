from Homework.Homework17.farm import Farm



farm1 = Farm("the farm #1",10,5,20,1000)
print(farm1)
print(len(farm1))

farm2 = Farm("the farm #2",20,8,40,2000)
print(farm2)
print(len(farm2))


farm3 = Farm("the farm #3",35,45,77,4000)
print(farm3)
print(len(farm3))


all_farms = farm1 + farm2 + farm3
print(all_farms)


# new_farm = my_farm1 + my_farm2
#
# print(new_farm)
# print(f"Farm acreage is {len(new_farm)} acres")

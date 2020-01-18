from homeworks.homework15.car import Car

print("Honda\n")
print("Class Car --->")

car1 = Car("Honda", "Accord", 2018, 2, 6, 230)
print(car1)
print(car1.__dict__)

print("Subaru\n")
car2 = Car("Subaru", "WRX STI", 2020, 4, 6, 340)
print(car2)
print(car2.__dict__)

print("Toyota\n")
car3 = Car("Toyota", "Camry XSE", 2018, 2, 4, 235)
print(car3)
print(car3.__dict__)

print("Dodge\n")
car4 = Car("Dodge", "Challenger SRT", 2008, 4, 8, 680)
print(car4)
print(car4.__dict__)

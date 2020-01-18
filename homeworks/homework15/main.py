from homeworks.homework15.car import Car
from homeworks.homework15.employees import Employee

                # Class Car
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



                # Class Employee
print("Employee1\n")
print("Class Employee")

emp1 = Employee("Ty", "McFarland", 42, "Frontend developer")
print(emp1)
print(emp1.__dict__)

print("Employee2\n")
print("Class Employee")

emp2 = Employee("Ashe", "Astrarie", 33, "Software engineer")
print(emp2)
print(emp2.__dict__)

print("Employee3\n")
print("Class Employee")

emp3 = Employee("Taras", "Podolskiy", 26, "QA Engineer")
print(emp1)
print(emp3.__dict__)


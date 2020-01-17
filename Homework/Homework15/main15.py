
from Homework.Homework15.Kindergarten15 import Kindergarten
from Homework.Homework15.Bank15 import Bank
from Homework.Homework15.Dealership15 import Dealership

print("")
print("class_Bank")
print("")

customer_1 = Bank("Dima", "Nikolaev", 3000, " checking , savings ,  investment, retiring  ")
print(customer_1)
print(customer_1.__dict__)

customer_2 = Bank("John", "Smith", 7000, " checking  and  savings   ")
print(customer_2)
print(customer_2.__dict__)

print("")

customer_2._first_name_on_account = "Edvard"
customer_2._second_name_on_account = "Williams"
customer_2.balance = -100
customer_2._all_accounts = "all closed"

print(customer_2)

print("")
print("class  Kindergarten")
print("")

child_1 = Kindergarten("Michael", "Smith", 2018, " yogurt   ")
print(child_1)

child_1.dob = 2022
child_1._first_name = "Vitalik"
print(child_1)
print(child_1.__dict__)


child_2 = Kindergarten("Jeniffer", "Johnson", 2016, " cookies, chips   ")
print(child_2)

print("")
print("class_Dealership")
print("")



car_1 = Dealership("BMW", "2018", "white", " moonroof ,Intelligent 4 Wheel Drive, Voice-Activated Touchscreen Navigation System ", "53.000.0")
print(car_1)

car_2 = Dealership("FORD", "2015", "red", "   sunroof ,adaptive CC ,sport package ", "15.000.0")
print(car_2)


car_1._color = "green"
print(car_1)


print("")
print("THE END")






# customer_1 = Bank()
# customer_1.first_name_on_account = " John"
# customer_1.second_name_on_account = "Ivanov"
# customer_1.balance = 5000
# customer_1.change_balance(3000)
# customer_1.all_accounts = ["checking ,", " savings ,", "investment ,", "retiring account "]
#
# customer_2 = Bank()
# customer_2.first_name_on_account = " Michael "
# customer_2.second_name_on_account = "Petrov"
# customer_2.balance = 7000
# customer_2.change_balance(-500)
# customer_2.all_accounts = ["checking ,", " savings"]
#
# customer_1.print_info()
# print("")
#
# customer_2.print_info()


# print("")
# print("class2")
# print("")
#
# child_1 = Kindergarden()
# child_1.first_name = "Dima"
# child_1.second_name = "Ivanov"
# child_1.DOB = 2017
# child_1.favorite_food = ["cookies ,", "apple"]
#
# child_2 = Kindergarden()
# child_2.first_name = "Nikolai"
# child_2.second_name = "Terentiev"
# child_2.DOB = 2016
# child_2.favorite_food = ["outmeal ,", "yogurt"]
#
# child_1.print_info()
# print("")
#
# child_2.print_info()
#
# print("")
# print("class3")
# print("")
#
# car_1 = Dealership()
# car_1.brand = "BMW"
# car_1.color = "white"
# car_1.options = ["sunroof ,", "adaptive CC ,", "sport package"]
# car_1.price = 62500.00
# car_1.production_year = 2018
#
# car_2 = Dealership()
# car_2.brand = "Ford"
# car_2.color = "red"
# car_2.options = ["moonroof ,", "Intelligent 4 Wheel Drive,", "Voice-Activated Touchscreen Navigation System"]
# car_2.price = 23999.00
# car_2.production_year = 2019
#
#
# car_1.print_info()
# print("")
#
# car_2.print_info()

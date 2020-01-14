from Homework.homework13.class1 import Bank
from Homework.homework13.class2 import Kindergarden
from Homework.homework13.class3 import Dealership


print("")
print("class1")
print("")


customer_1 = Bank()
customer_1.first_name_on_account = " John"
customer_1.second_name_on_account = "Ivanov"
customer_1.balance = 5000
customer_1.change_balance(3000)
customer_1.all_accounts = ["checking ,", " savings ,", "investment ,", "retiring account "]

customer_2 = Bank()
customer_2.first_name_on_account = " Michael "
customer_2.second_name_on_account = "Petrov"
customer_2.balance = 7000
customer_2.change_balance(-500)
customer_2.all_accounts = ["checking ,", " savings"]



customer_1.print_info()
print("")

customer_2.print_info()

print("")
print("class2")
print("")


child_1 = Kindergarden()
child_1.first_name = "Dima"
child_1.second_name = "Ivanov"
child_1.DOB = 2017
child_1.favorite_food = ["cookies ,", "apple"]

child_2 = Kindergarden()
child_2.first_name = "Nikolai"
child_2.second_name = "Terentiev"
child_2.DOB = 2016
child_2.favorite_food = ["outmeal ,","yogurt"]


child_1.print_info()
print("")

child_2.print_info()

print("")
print("class3")
print("")

car_1 = Dealership()
car_1.brand = "BMW"
car_1.color = "white"
car_1.options = ["sunroof ," , "adaptive CC ," , "sport package"]
car_1.price = 62500.00
car_1.production_year = 2018

car_2 = Dealership()
car_2.brand = "Ford"
car_2.color = "red"
car_2.options = ["moonroof ," , "Intelligent 4 Wheel Drive," , "Voice-Activated Touchscreen Navigation System"]
car_2.price = 23999.00
car_2.production_year = 2020


car_1.print_info()
print("")

car_2.print_info()

try:
    car_1.print_info()
except ValueError:
    print("WRONG DATA!")

try:
    car_2.print_info()
except ValueError:
    print("Wrong data entered!")




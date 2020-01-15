from Homework.HW14.order import Order
from Homework.HW14.item import Item
from Homework.HW14.customer import Customer


# Customers
customer_001 = Customer("001", "Leonardo DiCaprio", "1350 Charleston rd Mountain View CA", "Visa", ["0001", "0008"])
customer_002 = Customer("002","Jennifer Enniston", "Main str 200 Malibu Los Angeles", "Paypal", ["0002", "0011", "0017"])
customer_003 = Customer("003","Ellen DeGeneres", "100 Beverly Hills Los Angeles", "MasterCard", ["0003", "0015", "0019"] )

print(customer_001)
print(customer_002)
print(customer_003)

# Items
item_01 = Item("Pants","Men", ["Black", "White", "Red", "Green"],39.99, ["XS","S","M","L","XL"], "Adidas", "Adidas Soccer apparel is designed to keep you comfortable for the entire 90 minutes on the field and beyond")
item_02 = Item("Blouse","Women",["Black", "White", "Red"],59.99, ["XS","S","M","L","XL"], "ECOWISH", "Best Choice for Casual, Office, Party, Dating, Cocktail, Club, Wedding, Holiday or Daily Wear. Perfect for Spring, Summer and Autumn")
item_03 = Item("Shirt", "Men", ["Black", "White", "Blue"], 77.99, ["M","L","XL"], "Wrangler", "Made with comfort and function in mind, this two-sided brushed fleece will keep you warm all season long. Your new wardrobe favorite" )
item_04 = Item("T-shirt", "Women", ["Black", "White", "Blue"], 179.99, ["XS","S","XL"], "ED Ellen DeGeneres", "SUPER SOFT blend of cotton/polyester with V-NECKLINE, SHORT SLEEVES.")
item_05 = Item("Sneakers", "Women", ["Brown"], 179.99, ["8","9","10"], "ED Ellen DeGeneres", "Embrace the elements with the casual-chic ED Ellen DeGeneres™ Chaska Sneaker.")

print(item_01)
print(item_02)
print(item_03)
print(item_04)
print(item_05)

# Orders
order_0001 = Order(customer_001.orders[0],customer_001.name,customer_001.address, 220.08,{item_02.name: 1, item_04.name: 2},"01/10/2020", "Shipped")
order_0002 = Order(customer_002.orders[2],customer_002.name,customer_002.address, 136.69,{item_03.name: 1, item_04.name: 2},"01/03/2020", "Delivered")
order_0003 = Order(customer_003.orders[1],customer_003.name,customer_003.address, 1200.30, {item_01.name: 1, item_02.name:1}, "01/08/2020", "Pending")

try:
    print(order_0001)
except ValueError:
    print("WRONG DATA!")

try:
    print(order_0002)
except ValueError:
    print("Wrong data entered!")

try:
    print(order_0003)
except ValueError:
    print("Wrong data entered!")


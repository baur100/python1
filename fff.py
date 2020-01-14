
from Homework.HW13.order import Order
from Homework.HW13.item import Item
from Homework.HW13.customer import Customer

# Customers
customer_001 = Customer()
customer_001.number = "001"
customer_001.name = "Leonardo DiCaprio"
customer_001.address = "1350 Charleston rd Mountain View CA"
customer_001.payment = "Visa"
customer_001.orders = ["0001", "0008"]

customer_002 = Customer()
customer_002.number = "002"
customer_002.name = "Jennifer Enniston"
customer_002.address = "Main str 200 Malibu Los Angeles"
customer_002.payment = "Paypal"
customer_002.orders = ["0002", "0011", "0017"]

customer_003 = Customer()
customer_003.number = "002"
customer_003.name = "Ellen DeGeneres"
customer_003.address = "100 Beverly Hills Los Angeles"
customer_003.payment = "MasterCard"
customer_003.orders = ["0003", "0015", "0019"]

customer_001.print_customer_info()
customer_002.print_customer_info()
customer_003.print_customer_info()

# Items
item_01 = Item()
item_01.name = "Pants"
item_01.sex = "Men"
item_01.colors = ["Black", "White", "Red", "Green"]
item_01.price = 39.99
item_01.sizes = ["XS", "S", "M", "L", "XL"]
item_01.color = "Black"
item_01.brand = "Adidas"
item_01.description = "Adidas Soccer apparel is designed to keep you comfortable for the entire 90 minutes on the field and beyond"

item_02 = Item()
item_02.name = "Blouse"
item_02.sex = "Women"
item_02.colors = ["Black", "White", "Red"]
item_02.price = 59.99
item_02.sizes = ["XS", "S", "M", "L", "XL"]
item_02.brand = "ECOWISH"
item_02.description = "Best Choice for Casual, Office, Party, Dating, Cocktail, Club, Wedding, Holiday or Daily Wear. Perfect for Spring, Summer and Autumn"

item_03 = Item()
item_03.name = "Shirt"
item_03.sex = "Men"
item_03.colors = ["Black", "White", "Blue"]
item_03.price = 77.99
item_03.sizes = ["M", "L", "XL"]
item_03.brand = "Wrangler"
item_03.description = "Made with comfort and function in mind, this two-sided brushed fleece will keep you warm all season long. Your new wardrobe favorite"

item_04 = Item()
item_04.name = "T-shirt"
item_04.sex = "Women"
item_04.colors = ["Black", "White", "Blue"]
item_04.price = 179.99
item_04.sizes = ["XS", "S", "XL"]
item_04.brand = "ED Ellen DeGeneres "
item_04.description = "SUPER SOFT blend of cotton/polyester with V-NECKLINE, SHORT SLEEVES."

item_05 = Item()
item_05.name = "Sneakers"
item_05.sex = "Women"
item_05.colors = ["Brown"]
item_05.price = 179.99
item_05.sizes = ["8", "9", "10"]
item_05.brand = "ED Ellen DeGeneres "
item_05.description = "Embrace the elements with the casual-chic ED Ellen DeGeneres™ Chaska Sneaker."

item_01.print_item_info()
item_02.print_item_info()
item_03.print_item_info()
item_04.print_item_info()
item_05.print_item_info()

# Orders
order_0001 = Order()

order_0001.number = customer_001.orders[0]
order_0001.customer_name = customer_001.name
order_0001.shipping_address = customer_001.address
order_0001.total = "220.08"  # ERROR IS HERE. TYPE SHOUD BE FLOAT
order_0001.items = {item_02.name: 1, item_04.name: 2}
order_0001.date = "01/10/2020"
order_0001.status = "Shipped"

order_0002 = Order()

order_0002.number = customer_002.orders[1]
order_0002.customer_name = customer_002.name
order_0002.shipping_address = customer_002.address
order_0002.total = 368.99
order_0002.items = {item_05.name: 1, item_04.name: 1}
order_0002.date = "01/02/2020"
order_0002.status = "Delivered"

order_0003 = Order()

order_0003.number = customer_003.orders[2]
order_0003.customer_name = customer_003.name
order_0003.shipping_address = customer_003.address
order_0003.total = 1200.30
order_0003.items = {item_01.name: 1, item_02.name: 1}
order_0003.date = "01/08/2020"
order_0003.status = "Pending"

try:
    order_0001.order_info()
except ValueError:
    print("WRONG DATA!")

try:
    order_0002.order_info()
except ValueError:
    print("Wrong data entered!")

try:
    order_0003.order_info()
except ValueError:
    print("Wrong data entered!")


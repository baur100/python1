class Order:
    number = ""
    customer_name = ""
    shipping_address = ""
    total = 0.00
    items = {}
    quantity = 0
    date = ""
    status = ""

    def print_items(self):
        count = 0
        for i in self.items:
            count +=1
            print(f"{count}. {i} - {self.items[i]} pcs.")

    def order_info(self):
        print("")
        print("****** ORDER INFO *******")
        print(f"Order number: {self.number}")
        print(f"Customer_name: {self.customer_name}")
        print(f"Shipping address: {self.shipping_address}")
        print(f"Order total: ${self.total:,}")
        self.print_items()
        print(f"Order date: {self.date}")
        print(f"Order status: {self.status}")






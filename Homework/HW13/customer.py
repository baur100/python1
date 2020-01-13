class Customer:
    number = ""
    name = ""
    address = ""
    payment = ""
    orders = []

    def print_orders(self):
        print("Orders: ", *self.orders)


    def print_customer_info(self):
        print("")
        print("****** CUSTOMER INFO *******")
        print(f"Customer #: {self.number}")
        print(f"Customer name: {self.name}")
        print(f"Customer address: {self.address}")
        print(f"Customer payment method: {self.payment}")
        self.print_orders()
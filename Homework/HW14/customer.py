class Customer:
    def __init__(self, id, name, address, payment, orders):
        self.id = id
        self.name = name
        self.address = address
        self.payment = payment
        self.orders = orders

    def __repr__(self):
        return f"\n****** CUSTOMER INFO *******\n" \
            f"Customer ID: {self.id}\n" \
            f"Customer name: {self.name}\n" \
            f"Customer address: {self.address}\n" \
            f"Customer payment method: {self.payment}\n" \
            f"Customer odrers: {self.orders}"
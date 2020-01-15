class Order:
    def __init__(self, order_id, customer_name, shipping_address, total,items,date,status):
        self.order_id = order_id
        self.customer_name = customer_name
        self.shipping_address = shipping_address
        self.total = total
        self.items = items
        self.date = date
        self.status = status

    def print_items(self):
        count = 0
        for i in self.items:
            count +=1
            return f"{count}. {i} - {self.items[i]} pcs."

    def __repr__(self):
        return f"\n****** ORDER INFO *******\n" \
            f"Order ID: {self.order_id}\n" \
            f"Customer_name: {self.customer_name}\n" \
            f"Shipping address: {self.shipping_address}\n" \
            f"Order total: ${self.total}\n" \
            f"Items: {self.items}\n" \
            f"Order date: {self.date}\n" \
            f"Order status: {self.status}"






class Order:
    def __init__(self, order_id="0001", customer_name="", shipping_address="", total=0,items={},date="",status=""):
        if order_id == None:
            raise ValueError("Order ID doesn't exist")
        self._order_id = order_id
        self._customer_name = customer_name
        self._shipping_address = shipping_address
        self._total = total
        self._items = items
        self._date = date
        self._status = status

    def __repr__(self):
        return f"\n****** ORDER INFO *******\n" \
            f"Order ID: {self._order_id}\n" \
            f"Customer_name: {self._customer_name}\n" \
            f"Shipping address: {self._shipping_address}\n" \
            f"Order total: ${self._total}\n" \
            f"Items: {self._items}\n" \
            f"Order date: {self._date}\n" \
            f"Order status: {self._status}"

    @property
    def order_id(self):
        return self._order_id

    @order_id.setter
    def order_id(self, value):
        self._order_id = value

    @property
    def customer_name(self):
        return self._customer_name

    @customer_name.setter
    def customer_name(self, value):
        self._customer_name = value

    @property
    def shipping_address(self):
        return self._shipping_address

    @shipping_address.setter
    def shipping_address(self, value):
        self._shipping_address = value

    @property
    def total(self):
        return self._total

    @total.setter
    def total(self, value):
        self._total

    @property
    def items(self):
        return self._items

    @items.setter
    def items(self, value):
        self._items = value

    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, value):
        self._date

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status






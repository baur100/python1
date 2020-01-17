class Customer:

    def __init__(self, id="001", name="", address="", payment=0, orders=[]):
        if id == None:
            raise ValueError("Customer ID doesn't exist")
        self._id = id
        self._name = name
        self._address = address
        self._payment = payment
        self._orders = orders

    def __repr__(self):
        return f"\n****** CUSTOMER INFO *******\n" \
            f"Customer ID: {self._id}\n" \
            f"Customer name: {self._name}\n" \
            f"Customer address: {self._address}\n" \
            f"Customer payment method: {self._payment}\n" \
            f"Customer odrers: {self._orders}"

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, value):
        self._address = value

    @property
    def payment(self):
        return self._payment

    @payment.setter
    def payment(self, value):
        self._payment = value

    @property
    def orders(self):
        return self._orders

    @orders.setter
    def orders(self, value):
        self._orders = value
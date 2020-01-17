class Item:
    def __init__(self, name="", sex="", colors=[], price=0, sizes=[], brand="", description=""):
        self._name = name
        self._sex = sex
        self._colors = colors
        if price < 0:
            raise ValueError("Price is not defined")
        self._price = price
        self._sizes = sizes
        self._brand = brand
        self._description = description

    def __repr__(self):
        return f"\n****** MERCHANDISE INFO *******\n" \
            f"Name: {self._name}\n" \
            f"For {self._sex}\n" \
            f"Price: ${self._price:}\n" \
            f"Sizes: {self._sizes}\n" \
            f"Colors: {self._colors}\n" \
            f"Brand: {self._brand}\n" \
            f"Description: {self._description}"

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def sex(self):
        return self._sex

    @sex.setter
    def sex(self, value):
        self._sex = value

    @property
    def colors(self):
        return self._colors

    @colors.setter
    def colors(self, value):
        self._colors = value

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        self._price = value

    @property
    def sizes(self):
        return self._sizes

    @sizes.setter
    def sizes(self, value):
        self._sizes = value

    @property
    def brand(self):
        return self._brand

    @brand.setter
    def brand(self, value):
        self._brand

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, value):
        self._description

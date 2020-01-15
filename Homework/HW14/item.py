class Item:
    def __init__(self, name, sex, colors, price, sizes, brand, description):
        self.name = name
        self.sex = sex
        self.price = price
        self.sizes = sizes
        self.colors = colors
        self.brand = brand
        self.description = description

    def __repr__(self):
        return f"\n****** MERCHANDISE INFO *******\n" \
            f"Name: {self.name}\n" \
            f"For {self.sex}\n" \
            f"Price: ${self.price:}\n" \
            f"Sizes: {self.sizes}\n" \
            f"Colors: {self.colors}\n" \
            f"Brand: {self.brand}\n" \
            f"Description: {self.description}"


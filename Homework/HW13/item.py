class Item:
    name = ""
    sex = ""
    price = 0.00
    sizes = []
    colors = []
    brand = ""
    description = ""

    def print_sizes(self):
        print("Available sizes:", *self.sizes) # print in a row

    def print_colors(self):
        print("Available colors:", *self.colors) # print in a row

    def print_item_info(self):
        print("")
        print("****** MERCHANDISE INFO *******")
        print(f"Name: {self.name}")
        print(f"For {self.sex}")
        print(f"Price: ${self.price:,}")
        self.print_sizes()
        self.print_colors()
        print(f"Brand: {self.brand}")
        print(f"Description: {self.description}")



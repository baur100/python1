class Dealership:
    brand = ""
    production_year = 0
    color = ""
    options = []
    price = 0





    def __init__(self, brand, production_year,color,options,price):
        self.brand = brand
        self.production_year = production_year
        self.color = color
        self.options = options
        self.price = price



    def __repr__(self):
        return (f"brand - {self.brand}, production year {self.production_year}, color - {self.color}, OPTIONS: {self.options}, price = $ {self.price} ")


















    # def print_info(self):
    #     print(f"    brand - {self.brand} ")
    #     print(f"    production  year - {self.production_year} ")
    #     print(f"    color - {self.color} ")
    #     print(f"    price - ${self.price} ")
    #     print(f"    your car is  {self.get_car_age()}" + "   years old ")
    #
    #     self.get_options()
    #
    # def get_options(self):
    #     print("    options  -  ", *self.options)
    #
    # def get_car_age(self):
    #
    #     if self.date - self.production_year < 0 or self.date - self.production_year >100:
    #         raise ValueError("НЕВЕРНЫЕ ИСХОДНЫЕ ДАННЫЕ")
    #
    #     else:
    #         return self.date - self.production_year

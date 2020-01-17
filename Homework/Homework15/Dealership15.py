class Dealership:

    def __init__(self, brand, production_year,color,options,price):
        self._brand = brand
        self._production_year = production_year
        self._color = color
        self._options = options
        self._price = price

    @property
    def production_year(self):
        return self._production_year

    @production_year.setter
    def production_year(self, a):
        if a > 2020:
            print("wrong age   ")
        if a < 1950:
            print("too old")
        self._production_year = a



    def __repr__(self):
        return (f"brand - {self._brand}, production year {self._production_year}, color - {self._color}, OPTIONS: {self._options}, price = $ {self._price} ")


















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

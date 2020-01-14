class Dealership ():
    brand = ""
    production_year = 0
    date = 2020
    color = ""
    options = []
    price = 0




    def print_info(self):
        print ( f"    brand - {self.brand} ")
        print ( f"    production  year - {self.production_year} ")
        print ( f"    color - {self.color} ")
        print ( f"    price - ${self.price} ")
        print (f"    your car is  {self.get_car_age() }" + "   years old ")

        self.get_options()

    def get_options(self):
        print("    options  -  ", *self.options)

    def get_car_age(self):
        return self.date - self.production_year





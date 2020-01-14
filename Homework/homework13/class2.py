class Kindergarden ():
    first_name = ""
    second_name = ""
    DOB = 0
    year = 2020
    favorite_food = []


    def print_info (self):
        print ( f"    first name on account - {self.first_name} ")
        print ( f"    second name on account - {self.second_name} ")
        print (f"    the age is - {self.get_age()}")
        self.print_favorite_food()


    def get_age(self):
        return self.year - self.DOB

    def print_favorite_food(self):
        print("    favorite food is  -  ", *self.favorite_food)


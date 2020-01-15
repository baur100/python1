class Kindergarden:
    first_name = ""
    second_name = ""
    DOB = 0
    favorite_food = []

    def __init__(self, first_name, second_name, dob,favorite_food):
        self.first_name = first_name
        self.second_name = second_name
        self.DOB = dob
        self.favorite_food = favorite_food

    def __repr__(self):
        return (f"{self.first_name} {self.second_name} , date of birth {self.DOB} ,  favorite food is - {self.favorite_food}  ")









    # def print_info (self):
    #     print ( f"    first name on account - {self.first_name} ")
    #     print ( f"    second name on account - {self.second_name} ")
    #     print (f"    the age is - {self.get_age()}")
    #     self.print_favorite_food()
    #
    #
    # def get_age(self):
    #     return self.year - self.DOB
    #
    # def print_favorite_food(self):
    #     print("    favorite food is  -  ", *self.favorite_food)


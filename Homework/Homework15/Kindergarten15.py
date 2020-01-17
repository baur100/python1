class Kindergarten:

    def __init__(self, first_name, second_name, dob, favorite_food):

        self._first_name = first_name
        self._second_name = second_name
        self._DOB = dob
        self._favorite_food = favorite_food

    @property
    def dob(self):
        return self._DOB

    @dob.setter
    def dob(self, w):
        if w > 2020:
            print("wrong age   ")
        if w < 2014:
            print("too old")
        self._DOB = w

    def __repr__(self):
        return f"{self._first_name} {self._second_name} , date of birth {self._DOB} ,  favorite food is - {self._favorite_food}  "

    # def __init__(self, first_name, second_name, dob,favorite_food):
    #     self.first_name = first_name
    #     self.second_name = second_name
    #     self.DOB = dob
    #     self.favorite_food = favorite_food
    #
    # def __repr__(self):
    #     return (f"{self.first_name} {self.second_name} , date of birth {self.DOB} ,  favorite food is - {self.favorite_food}  ")

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


class Person:
    def __init__(self, first_name, last_name, gender, age):
        self._first_name = first_name
        self._last_name = last_name
        self._gender = gender
        self._age = age
    def __repr__(self):
        return f"{self._first_name} {self._last_name} {self._gender} {self._age}"

    def getInfo(self):
        return f"Hello = my name is {self._first_name} and my age is {self._age} - I'm a person"

    def get_my_gender_and_age(self):
        return f"{self._gender}+++{self._age}"

    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, value):
        self._first_name = value

    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, value):
        self._last_name = value

    @property
    def gender(self):
        return self._gender

    @gender.setter
    def gender(self, value):
        self._gender = value

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        self._age = value

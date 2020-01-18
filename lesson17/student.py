
from lesson17.person import Person
from lesson17.college import College

class Student(Person,College):
    def __init__(self, first_name, last_name, gender, age, major):
        super().__init__(first_name, last_name, gender, age)
        self._major = major
    def __repr__(self):
        return f"{self._first_name} {self._last_name} {self._gender} {self._age} my major = {self._major}"

    def get_major(self):
        return self._major

    @property
    def major(self):
        return self._major

    @major.setter
    def major(self, value):
        self._major = value

    # def getInfo(self):
    #     return f"Hello = my name is {self._first_name} and my age is {self._age} - I'm a student"


class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f'cats name is {self.name} and cats age is {self.age} years'


class Panda:

    def __init__(self, name, weight, age, kids, country):
        self.name = name
        self._weight = weight
        self._age = age
        self.kids = kids
        self._country = country

    def print_info(self):
        print(f"This lovely panda {self.name} is {self._age} years old. ")
        if not self.kids:
            print(f"It lives in {self._country} with no babies.")
        else:
            print(f"It lives in {self._country} with {self.kids} baby(ies).")
        print(f"{self.name} weights {self._weight} pounds.")
    def gain_weight(self, x):
        if self._weight+x>350:
            raise ValueError("The panda cannot weight thaaaat much!!!")
        if x<=0:
            raise ValueError("Panda gaining the weight or what?")
        self._weight+=x
    def change_age(self):
        self._age+=1
    def get_weight(self):
        return self._weight
    def get_name(self):
        return self.name

    def __repr__(self):
        return f'{self.name} is a panda, {self.age} years old, \n weights {self.weight}lb, has {self.kids}, and live in {self.country}'

    @property
    def weight(self):
        return self._weight

    @weight.setter
    def weight(self, value):
        if value>350 or value<10:
            raise ValueError("OOOPS! Wrong weight")
        self._weight=value

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if value>20 or value<0:
            raise ValueError("OOPS! Wrong age. The pandas born at age of 0 and usually live 20 years")
        self._age=value

    @property
    def country(self):
        return self._country

    @country.setter
    def country(self, value):
        if type(value) is not str:
            raise TypeError("OOOS! There is no such a country ")
        self._country=value

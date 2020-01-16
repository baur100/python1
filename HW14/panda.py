class Panda:

    def __init__(self, name, weight, age, kids, country):
        self.name = name
        self.weight = weight
        self.age = age
        self.kids = kids
        self.country = country

    def print_info(self):
        print(f"This lovely panda {self.name} is {self.age} years old. ")
        if not self.kids:
            print(f"It lives in {self.country} with no babies.")
        else:
            print(f"It lives in {self.country} with {self.kids} baby(ies).")
        print(f"{self.name} weights {self.weight} pounds.")
    def gain_weight(self, x):
        if self.weight+x>350:
            raise ValueError("The panda cannot weight thaaaat much!!!")
        if x<=0:
            raise ValueError("Panda gaining the weight or what?")
        self.weight+=x
    def change_age(self):
        self.age+=1
    def get_weight(self):
        return self.weight
    def get_name(self):
        return self.name

    def __repr__(self):
        return f'{self.name} is a panda, {self.age} years old, \n weights {self.weight}lb, has {self.kids}, and live in {self.country}'
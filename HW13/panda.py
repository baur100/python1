class Panda():
    name = ""
    weight=""
    age=0
    kids=0
    country=""

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
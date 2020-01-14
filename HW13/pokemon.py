class Pokemon():
    name=""
    type=""
    generation=0
    species=""
    abilities=[]
    hp=0

    def print_info(self):
        print(f"name - {self.name}")
        print(f"type - {self.type}")
        print(f"generation - {self.generation}")
        print(f"part of  {self.species} Sprecies")
        print(f"Abilities - {self.abilities}")
        print(f"HP - {self.hp}")

    def attack(self, ab):
        if type(ab) is not str:
              raise TypeError("Ability must be string")
        if ab not in self.abilities:
            raise ValueError(f"{self.name} doesn't have this ability")
        print(f"{self.name} attacks with {ab}.")



    def get_name(self):
        return self.name

    def add_abilities(self, new_ab):
        self.abilities.append(new_ab)
class Pokemon:
    def __init__(self, name, type, gen=0, species="", abilities=[], hp=10):
        self._name=name
        self.type=type
        self._generation=gen
        self._species=species
        self.abilities=abilities
        self.hp=hp

    def print_info(self):
        print(f"name - {self.name} ")
        print(f"type - {self.type} ")
        print(f"generation - {self.generation} ")
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

    def __repr__(self):
        return f'Pokemon: {self.name} \n' \
               f'Type: {self.type} \n' \
               f'Generation: {self.generation}\n' \
               f'Species: {self.species}\n' \
               f'HP: {self.hp}\n' \
               f'Abilities: {self.abilities}'

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name=value

    @property
    def species(self):
        return self._species

    @species.setter
    def species(self, value):
        if type(value) is not str:
            raise TypeError("OOPS! Wrong Species")
        self._species=value
    @property
    def generation(self):
        return self._generation

    @generation.setter
    def generation(self, value):
        if value<1 and value>4:
            raise ValueError("OOOPS! Generation supposed to be 0-4")
        self._generation=value

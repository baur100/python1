class Farm:
    def __init__(self, name, land, livestock, equipment):
        self.name = name
        self.land = land
        self.livestock = livestock
        self.equipment = equipment

    def __repr__(self):
        return f"Farm name is - {self.name()}" \
               f"Land area is {self.land} km2" \
               f"Cows are the only {self.livestock}" \
               f"Current equipment {self.equipment}"

    def machines(self):
        return f"in the {self.name} there are many {self.equipment}"

    def __add__(self, other):
        return Farm(f"{self.name} and {other.name}"
                    f"{self.land} and {other.land}"
                    f"{self.livestock} and {other.livestock}"
                    f"{self.equipment} and {other.equipment}")

    @property
    def name (self):
        return self.name

    @name .setter
    def name (self, value):
        self.name = value

    @property
    def land(self):
        return self.land

    @land.setter
    def land(self, value):
        self.land = value

    @property
    def livestock(self):
        return self.livestock

    @livestock.setter
    def livestock(self, value):
        self.livestock = value

    @property
    def equipment(self):
        return self.equipment

    @equipment.setter
    def equipment(self, value):
        self.equipment = value

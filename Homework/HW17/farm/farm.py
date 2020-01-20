class Farm:
    def __init__(self, name, acreage, livestock, machinery):
        self._name = name
        self._acreage = acreage
        self._livestock = livestock
        self._machinery = machinery

    def __repr__(self):
        return f"{self._name} is {self._acreage} acres, has livestock {self._livestock} animals and machinery {self._machinery} items. "

    def __len__(self):
        return self._acreage

    def __add__(self,other):
        return Farm(f"{self._name[0]}&{other._name[0]} farm", self._acreage+other._acreage, self._livestock+other._livestock, self._machinery+other._machinery)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def acreage(self):
        return self._acreage

    @acreage.setter
    def acreage(self, value):
        self._acreage = value

    @property
    def livestock(self):
        return self._livestock

    @livestock.setter
    def livestock(self, value):
        self._livestock = value

    @property
    def machinery(self):
        return self._machinery

    @machinery.setter
    def machinery(self, value):
        self._machinery = value
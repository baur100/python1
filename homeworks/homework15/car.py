class Car:
    def __init__(self, make, model, year, wheel_dr, cyl, hp):
        self._make = make
        self._model = model
        self._year = year
        if wheel_dr != 4:
            raise ValueError("Only 4 wheelie please")
        self._wheel_dr = wheel_dr
        if cyl < 6:
            raise ValueError("Weak af")
        if cyl > 8:
            raise ValueError("Not that rich boy")
        self._cyl = cyl
        self._hp = hp

    def __repr__(self):
        return (
            f"This is {self._make} - {self._model}, the year of {self._year} and it's a {self._wheel_dr} wheelie with a {self._cyl} cylinders and {self._hp} horsepower")

    @property
    def make(self):
        return self._make

    @make.setter
    def make(self, value):
        self._make = value

    @property
    def model(self):
        return self._model

    @make.setter
    def make(self, value):
        self._make = value

    @property
    def year(self):
        return self.year

    @year.setter
    def year(self, value):
        self._year = value

    @property
    def wheel_dr(self):
        return self._wheel_dr

    @wheel_dr.setter
    def wheel_dr(self, value):
        self._wheel_dr = value

    @property
    def cyl(self):
        return self._hp

    @cyl.setter
    def cyl(self, value):
        self._cyl = value

    @property
    def hp(self):
        return self._hp

    @hp.setter
    def hp(self, value):
        self._hp = value

    @model.setter
    def model(self, value):
        self._model = value
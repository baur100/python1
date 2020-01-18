class Person:
    def __init__(self,first_name="",last_name="", year=1921):
        self._first_name = first_name
        self._last_name = last_name
        if year > 2020 or year < 1920:
            raise ValueError("Wrong Year")
        self._year = year

    def __repr__(self):
        return f"{self._first_name} - {self._last_name} - {self._year}"

    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, value):
        self._first_name = value

    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, value):
        self._last_name=value

    @property
    def year(self):
        return self._year

    @year.setter
    def year(self, value):
        if value >2020 or value <1920:
            raise ValueError("Wrong Year")
        self._year=value






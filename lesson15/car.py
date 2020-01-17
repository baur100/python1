class Car:
    def __init__(self,number_of_door,model,producer):
        self.nod = number_of_door
        self.model = model
        self.producer = producer
        # if year > 2020 or year < 1970:
        #     raise ValueError("wrong year")
        # self._year = year

    def __repr__(self):
        return f"{self.model} - {self._year}"

    # def get_year(self):
    #     return self._year
    #
    # def set_year(self,year):
    #     if year > 2020 or year < 1970:
    #         raise ValueError("wrong year")
    #     self._year = year

    @property
    def year(self):
        return self._year

    @year.setter
    def year(self,value):
        if value > 2020 or value < 1970:
            raise ValueError("wrong year")
        self._year = value

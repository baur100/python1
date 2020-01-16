class Apartment:
    def __init__(self, state, city, street, apt_num):
        self.state = state
        self.city = city
        self.street = street
        self.apt_num = apt_num

    def __repr__(self):
        return f"{self.state}, {self.city}, {self.street}, {self.apt_num}"
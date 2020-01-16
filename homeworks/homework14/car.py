class Car:
    def __init__(self, make, model, age, transmission, odometer):
        self.make = make
        self.model = model
        self.age = age
        self.transmission = transmission
        self.odometer = odometer

    def __repr__(self):
        return f"The make is - {self.make} and the model is - {self.model}"

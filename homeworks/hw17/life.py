class Life:
    def __init__(self, name):
        self._name = name

    def proliferate(self):
        raise NotImplementedError("Subclass must implement this method")

    def eat(self):
        raise NotImplementedError("Subclass must implement this method")

    def see(self):
        raise NotImplementedError("Subclass must implement this method")

    def breathe(self):
        raise NotImplementedError("Subclass must implement this method")

    def all_func(self):
        return f"{self.eat()}\n" \
               f"{self.see()}\n" \
               f"{self.breathe()}" \
               f"{self.proliferate()}"

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

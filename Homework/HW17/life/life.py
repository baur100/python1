class Life:
    def __init__(self,name ):
        self._name = name


    def breathe(self):
        raise NotImplementedError("Subclass must implement this method!")

    def eat(self):
        raise NotImplementedError("Subclass must implement this method!")

    def spawn(self):
        raise NotImplementedError("Subclass must implement this method!")

    def __str__(self):
        raise NotImplementedError("Subclass must implement this method!")

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
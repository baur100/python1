class Animal:
    def __init__(self,spicy,place, department):
        self._spicy = spicy
        self._place = place
        self._department = department

    def get_info(self):
        raise NotImplemented("Cant instanciate class")
class Animals:
    def __init__(self, vertebrates, invertebrates):
        self._vertebrates = vertebrates
        self._invertebrates = invertebrates

    def breathe(self):
        return f"I am from Animals class all animals can breathe"

    def get_info(self):
        return f" Hello I am method from Animals class ........    "


    def swim(self):
        return f" {self._vertebrates} , {self._invertebrates}  -   we can swim (from Animals class)"

    def fly(self):
        return f" {self._vertebrates} , {self._invertebrates}  -   we can fly (from Animals class)"

    def run(self):
        return f" {self._vertebrates} , {self._invertebrates}  - we can run (from Animals class)"
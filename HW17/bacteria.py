from HW17.life import Life
from HW17.scientific_classification import Scientific_Classification


class Bacteria(Life, Scientific_Classification):
    _type_getting_food = ""  # parasite, saprophyte, symbiont
    _form = ""  # cocci, bacilli, vibrios, spirillas, streprococcus, staphylococci

    def __init__(self, type, form, dep, cl, family, genus, sp, name):
        super().__init__(["organic"], "", True, "top", ("silence"), "division", 100000)
        self._type_getting_food = type
        self._form = form
        super().init(dep, cl, family, genus, sp, name)

    @property
    def type_getting_food(self):
        return f"I'm {self._type_getting_food}"

    @type_getting_food.setter
    def type_getting_food(self, value):
        self._type_getting_food = value

    @property
    def form(self):
        return f"I have a form of {self._form}"

    @form.setter
    def form(self, value):
        self._form = value

    def explaining_form(self):
        expl = {
            "cocci": "spherical",
            "bacilli": "rod-shaped",
            "vibrios": "curved",
            "spirillas": "spiral",
            "streprococcus": "chain form",
            "staphylococci": "clusters"
        }
        return expl[self._form]

    def __repr__(self):
        return f"I'm a Bacteris. That's mean {super().__repr__()} \n{super().repr()}\n" \
               f"{self.form}, {self.type_getting_food} "




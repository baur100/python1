class Scientific_Classification:
    _division = ""
    _clas = ""
    _family = ""
    _genus = ""
    _species = ""
    _name = ""

    def init(self, dep, cl, family, genus, sp, name):
        self._division = dep
        self._clas = cl
        self._family = family
        self._genus = genus
        self._species = sp
        self._name = name

    @property
    def division(self):
        return f"Division: {self._division}\n"

    @division.setter
    def division(self, value):
        self._division = value

    @property
    def clas(self):
        return f"Class: {self._clas}\n"

    @clas.setter
    def clas(self, value):
        self._clas = value

    @property
    def family(self):
        return f"Family: {self._family}\n"

    @family.setter
    def family(self, value):
        self._family = value

    @property
    def genus(self):
        return f"Genus: {self._genus}\n"

    @genus.setter
    def genus(self, value):
        self._genus = value

    @property
    def species(self):
        return f"Species: {self._species}\n"

    @species.setter
    def species(self, value):
        self._species = value

    @property
    def name(self):
        return f"Common name: {self._name}\n"

    @name.setter
    def name(self, value):
        self._name = value

    def repr(self):
        return f"My specification: \n" + self.division + self.clas + self.family + self.genus + self.species + self.name


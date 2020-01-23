class Life:
    _nutrition=[] #diet
    _metabolism="" #type of metabolism
    _breath=True
    _growth="" #way of growing
    _irritability=()
    _reproduction="" #way of reproduction
    _death=0 #max age of death

    def __init__(self, nutrition=[], metabolism="", breath=True, growth="", irritability=(), reproduction="", death=0):
        self._nutrition=nutrition
        self._metabolism=metabolism
        self._breath=breath
        self._growth=growth
        self._irritability=irritability
        self._reproduction=reproduction
        self._death=death

    def get_info(self):
        raise NotImplemented("Can't be initiated as an object")

    @property
    def nutrition(self):
        return f"My diet is: {self._nutrition}"

    @nutrition.setter
    def nutrition(self, value):
        self._nutrition=value

    @property
    def metabolism(self):
        return f"I have metabolism"

    @metabolism.setter
    def metabolism(self, value):
        self._metabolism=value

    @property
    def breath(self):
        return f"I breath!!!"

    @breath.setter
    def breath(self, value):
        self._breath=value

    @property
    def growth(self):
        return f"I grow through {self._growth}"

    @growth.setter
    def growth(self, value):
        self._growth=value

    @property
    def irritability(self):
        return f"I have my favorite connection with surrounding!\n" \
               f"Which is {self._irritability}"

    @irritability.setter
    def irritability(self, value):
        self._irritability=value

    @property
    def reproduction(self):
        return f"I have my babies by {self._reproduction}"

    @reproduction.setter
    def reproduction(self, value):
        self._reproduction=value

    @property
    def death(self):
        return f"I die at age of {self._death}"

    @death.setter
    def death(self, value):
        self._death=value

    def __repr__(self):
        return f"I'm living organism, that's why I can eat, \n" \
               f"{self.nutrition}\n" \
               f"{self.metabolism}\n" \
               f"{self.breath} and {self.growth}\n" \
               f"{self.irritability}\n" \
               f"{self.reproduction}\n" \
               f"and finally, {self.death}"

    def Im_alive(self):
        print("I'm alive!!!")




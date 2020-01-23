from HW17.vertebrates import Vertebrates
from HW17.scientific_classification import Scientific_Classification
class Reprilies(Vertebrates, Scientific_Classification):
    _body={"head", "body", "tail", "2 pair legs" }
    _skin=""

    def __init__(self, skin, dep, cl, family, genus, sp, name):
        super().__init__({"digestive", "breathing", "circulatory", "nervous"}, "crawling" , ["warms", "rodents", "crickets"], "diagest", True, "exuviate", "venom", "laying eggs", 60)
        self._skin=skin
        super().init(dep, cl, family, genus, sp, name)

    @property
    def body(self):
        return f"My body parts: {self._body}"

    @body.setter
    def body(self, value):
       pass
    @property
    def skin(self):
        return self._skin

    @skin.setter
    def skin(self, value):
        self._skin=value

    def __repr__(self):
        return f"I'm a Reptile. That's mean I'm cold-blooded\n" \
               f" {self.body} \n" \
               f"My skin is a {self._skin}" \
               f"{super().__repr__()}" \
               f"{super().repr()}"


    def my_digestive_system(self):
        print(f"My digestive tract is mouth - pharynx - esophagus - stomack - intedtines - cesspool")

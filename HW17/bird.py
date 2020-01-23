from HW17.vertebrates import Vertebrates
from HW17.scientific_classification import Scientific_Classification
class Bird(Vertebrates, Scientific_Classification):
    _body={"head", "body", "tail", "wings", "legs"}


    def __init__(self, dep, cl, family, genus, sp, name):
        super().__init__({"digestive", "breathing", "circulatory", "nervous"}, "flying" , ["warms", "bread", "meat"], "diagest", True, "get bigger", "bite", "laying eggs", 80)
        super().init(dep, cl, family, genus, sp, name)

    @property
    def body(self):
        return f"My body parts: {self._body}"

    @body.setter
    def body(self, value):
       pass

    def __repr__(self):
        return f"I'm a bird. That's mean I habe feathers.\n" \
               f" {self.body} \n" \
               f"{super().__repr__()}" \
               f"{super().repr()}"


    def fly(self):
        print(f"I'm flying like a BIRD! Oh.... I'm a BIRD!!!!")

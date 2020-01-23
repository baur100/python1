from HW17.vertebrates import Vertebrates
from HW17.scientific_classification import Scientific_Classification

class Amphibians(Vertebrates, Scientific_Classification):
    _body={"head", "body", "limbs" }
    _sound=""

    def __init__(self, sound, dep, cl, family, genus, sp, name):
        super().__init__({"digestive", "breathing", "circulatory", "nervous", "excretory"}, "swimming, crawling" , ["warms", "bread", "moskitoes"], "diagest", True, "get bigger", "bite, run", "laying eggs", 36)
        self._sound=sound
        super().init(dep, cl, family, genus, sp, name)

    @property
    def body(self):
        return f"My body parts: {self._body}"

    @body.setter
    def body(self, value):
       pass
    @property
    def sound(self):
        if self._sound:
            return f"I can do {self._sound} - {self._sound} "
        else:
            return f"I don't speak "

    @sound.setter
    def sound(self, value):
        self._sound=value

    def __repr__(self):
        return f"I'm a Amphibians. That's mean I live everywhere.\n" \
               f" {self.body} \n" \
               f" {self.sound}" \
               f"{super().__repr__()}" \
               f"{super().repr()}"

    def tongue(self):
        print("I have the longest tongue :-P ")



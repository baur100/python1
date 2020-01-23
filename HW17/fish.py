from HW17.vertebrates import Vertebrates
from HW17.scientific_classification import Scientific_Classification
class Fish(Vertebrates, Scientific_Classification):
    _body={"head", "body", "tail", "fins" }
    _buble=True

    def __init__(self, bubble, dep, cl, family, genus, sp, name):
        super().__init__({"digestive", "breathing", "circulatory", "nervous", "excretory"}, "swimming" , ["warms", "bread", "peopele"], "diagest", True, "get bigger", "bite", "laying eggs", 15)
        self._bubble=bubble
        super().init(dep, cl, family, genus, sp, name)

    @property
    def body(self):
        return f"My body parts: {self._body}"

    @body.setter
    def body(self, value):
       pass
    @property
    def bubble(self):
        if self._bubble:
            return f"I have a swim bladder "
        else:
            return f"I don't have a swim bladder "

    @bubble.setter
    def bubble(self, value):
        self._bubble=value

    def __repr__(self):
        return f"I'm a Fish. That's mean I live in the water.\n" \
               f" {self.body} \n" \
               f" {self.bubble}" \
               f"{super().__repr__()}" \
               f"{super().repr()}"



    def swim(self):
        print(f"Just keep swimming. Just keep swimming! Swimming! Swimming! Swimming!")

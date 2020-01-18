from lesson16.person import Person
class Teacher(Person):
    def __init__(self, first_name, last_name, gender, age, subject, wage):
        super().__init__(first_name, last_name, gender, age)
        self._subject = subject
        self._wage = wage

    def __repr__(self):
        return f"{self._first_name} {self._last_name} {self._gender} {self._age} subject = {self._subject}"

    @property
    def subject(self):
        return self._subject

    @subject.setter
    def subject(self, value):
        self._subject=value

    @property
    def wage(self):
        return self._wage

    @wage.setter
    def wage(self, value):
        self._wage=value


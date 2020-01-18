from lesson16.person import Person
class Doctor(Person):
    def __init__(self,first_name, last_name, gender, age, prof):
        super().__init__(first_name, last_name, gender, age)
        self._prof = prof

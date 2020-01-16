class Student():
    first_name=""
    last_name=""
    year_of_birth = 0
    list_of_subject = []
    major =""
    _ballans=-1000

    def print_info(self):
        print(f"first name - {self.first_name}")
        print(f"last name - {self.last_name}")
        print(f"year of birth - {self.year_of_birth}")
        print(f"major {self.major}")

    def print_subjects(self):
        for x in self.list_of_subject:
            print(x)

    def change_ballans(self, x):
        self._ballans+=x

    def get_ballans(self):
        return self._ballans

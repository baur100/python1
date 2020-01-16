class Teacher:
    first_name=""
    last_name=""
    year_of_birth=0
    subject=""
    hours = 0
    pay = 0

    def get_salary(self):
        return self.hours*self.pay

    def print_info(self):
        print(f"first name - {self.first_name}")
        print(f"last name - {self.last_name}")
        print(f"year of birth - {self.year_of_birth}")
        print(f"subject {self.subject}")
class Employee():
    first_name = ""
    last_name = ""
    dob = ""
    occupation = ""
    stack = []

    def print_info(self):
        print(f"First name - {self.first_name}")
        print(f"Last name - {self.last_name}")
        print(f"Date of birth - {self.dob}")

    def work_rel_info(self):
        print(f"The position is - {self.occupation}")
        print(f"the dev stack is - {self.stack}")


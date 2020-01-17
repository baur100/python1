class Student:

    def __init__(self, name, major, gpa, is_on_probation):
        self.name = name
        self.major = major
        self.gpa = gpa
        self.is_on_probation = is_on_probation

    def print_info(self):
        print(f"The name is: {self.name} The GPA is {self.gpa}")

    def print_major(self):
        print(f"The major is: {self.major}")
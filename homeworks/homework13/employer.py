class Employer:
    name = ""
    since = 0
    employee_num = 0
    buss_type = ""
    location = []
    headquarters = ""

    def info(self):
        print(f"The name of the company is - {self.name}")
        print(f"{self.name} has been around since {self.since}")
        print(f"{self.name} has a {self.employee_num} number of employees")

    def offices(self):
        print(f"The offices are running in a several locations, including: {self.location}")
        print(f"The headquarter is in {self.location} state")
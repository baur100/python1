from homeworks.homework13.employee import Employee
from homeworks.homework13.employer import Employer

# Employee_1
matt = Employee()
matt.first_name = "Mattias"
matt.last_name = "Austin"
matt.dob = "01/01/1990"
matt.occupation = "Backend Engineer"
matt.stack = ["Scala, Ruby, python"]

matt.print_info()
matt.work_rel_info()
# Employee_2

t = Employee()
t.first_name = "Ty"
t.last_name = "McFarland"
t.dob = "02/10/1970"
t.occupation = "Frontend developer"
t.stack = "JS"

print("\n")

print()
t.print_info()
print()
t.work_rel_info()

print()
# Employer

e = Employer()
e.name = "E Financial"
e.since = 2015
e.employee_num = 115
e.buss_type = "Fintech"
e.location = ["FL", "CA", "NY"]

print()
e.info()
e.offices()

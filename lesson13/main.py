
from lesson13.student import Student
from lesson13.teacher import Teacher

peter = Student()
peter.first_name = "Peter"
peter.last_name = "Ivanoff"
peter.year_of_birth = 2000
peter.major = "math"
peter.list_of_subject = ["math", "biology", "history","french literature"]
peter.change_ballans(-3000)

anny = Student()
anny.first_name = "Anna"
anny.last_name = "Morozoff"
anny.list_of_subject = ["law", "biology", "history","french literature"]
anny.major = "law"
anny.year_of_birth = 2001
anny.change_ballans(2000)

# peter.print_info()
# anny.print_subjects()

print(peter.get_ballans())
print(anny.get_ballans())

mr_jones = Teacher()
mr_jones.first_name = "Jake"
mr_jones.last_name="Jones"
mr_jones.subject="math"
mr_jones.year_of_birth = 1980
mr_jones.hours = 20
mr_jones.pay = 50
mr_jones.print_info()
print(f"salary = {mr_jones.get_salary()}")




from lesson16.student import Student
from lesson16.person import Person
from lesson16.teacher import Teacher
from lesson16.address import Address
from lesson16.doctor import Doctor
from lesson16.hospital import Hospital

# ivan = Student("Ivan","Jones","M",20,"Math")
# print(ivan.getInfo())
# print(ivan.get_my_gender_and_age())
# print(ivan.get_major())
# ivan.gender = "F"
# print(ivan.get_my_gender_and_age())
# pers = Person("John","Davids","M",40)
# mr_calm = Teacher("Mark","Calm", "M",54,"History",55)
# print(mr_calm.getInfo())

hospital_address = Address("122 Main str", "New Yurk", "NY", 10306)
mr_paper = Doctor("James","Paper","M",45,"Phycisian")
mr_stone = Doctor("Halk","Johnson","M",48,"Dantist")

docts = [mr_paper,mr_stone]

st_mary_hospital = Hospital(docts,hospital_address)

print(st_mary_hospital._address._steet_address)



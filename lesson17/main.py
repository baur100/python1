from lesson17.person import Person
from lesson17.student import Student
from lesson17.animal import Animal
from lesson17.college import College


pesrson1 = Person("Haim","Jacob","M",38)
pesrson2 = Person("Alice","Jacob","M",35)
student1 = Student("Jane","Fonda","F",42,"Geography")
college = College("St Mary college")

nn = pesrson1 + pesrson2
print(nn)
print(len(pesrson1))



# tiger = Animal("Tiger",58,"Carnivors")
# tiger.get_info()


# print(pesrson1.getInfo())
print(student1.getInfo())

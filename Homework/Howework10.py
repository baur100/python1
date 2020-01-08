# 1. Создайте функцию greeting - которая принимает некоторое количество аргументов
# если среди агрументов есть слово "python" - выведите 'Hello, Snake'
# если среди агрументов есть слово "qa" - выведите 'Hello, QA Engineer'
# если среди агрументов есть слово "bee" - выведите 'Hello, Maya'
# если среди агрументов есть слово "world" - выведите 'Hello, World'
# //extra во всех остальных случаях - "I don't know you"
#
# если больше одного - выведите все доступные фразы
# прогоните следующие тесткейсы
# greeting("Hi",45,True,"python")
# greeting("bee",1212,True,"python", False,True)
# greeting("world")
# greeting("qa",45,True,"bee","world","python",67,True,"Some words")
# greeting()
# greeting("hummus","tomato soup","wink",True)
# Hint - user if in for

def greeting(*args):
    flag=True
    if "python" in args:
        print ("Hello, Snake")
        flag=False
    if "qa" in args:
        print("Hello, QA Engineer")
        flag = False
    if "bee" in args:
        print("Hello, Maya")
        flag = False
    if "world" in args:
        print("Hello, World")
        flag = False
    if flag:
        print("I don't know you")

greeting("Hi",45,True,"python")
print("")
greeting("bee",1212,True,"python", False,True)
print("")
greeting("world")
print("")
greeting("qa",45,True,"bee","world","python",67,True,"Some words")
print("")
greeting()
print("")
greeting("hummus","tomato soup","wink",True)
print("-------------------------")

# 2. Создайте функцию who_are_you() - которая принимает некоторое количество аргументов
# если среди агрументов есть слово "python" и "pycharm" - выведите 'Hello python'
# если среди агрументов есть слово "java" и "netbeans"- выведите 'Hello, java'
# extra во всех остальных случаях - "I don't know you"
# прогоните следующие тесткейсы
# who_are_you("java",45,True,"python")
# who_are_you("python",1212,True,"python", False,True)
# who_are_you("python",1212,True,"pycharm", False,True)
# who_are_you("world")
# who_are_you("qa",45,True,"java","world","netbeans",67,True,"Some words")
# who_are_you()

def who_are_you(*args):
    fl=True
    if "python" and "pycharm" in args:
        print("Hello python")
        fl=False
    if "Java" and "netbeans" in args:
        print("Hello, java")
        fl=False
    if fl:
        print("I don't know you")

who_are_you("java",45,True,"python")
print("")
who_are_you("python",1212,True,"python", False,True)
print("")
who_are_you("python",1212,True,"pycharm", False,True)
print("")
who_are_you("world")
print("")
who_are_you("qa",45,True,"java","world","netbeans",67,True,"Some words")
print("")
who_are_you()
print("----------------------")


# 3. Создайте функцию favorite_food() - которая принимает некоторое количество именнованых аргументов аргументов
# в следующем виде name = food
# выведите на экран - name loves eat food - для всех аргументов
# favorite_food(john = "pizza", jack = "pumkin", jay = "chicken noodle", ken = "burger")
# favorite_food(john = "pizza", jack = "pumkin")
# favorite_food()

def favorite_food(**kwargs):
    if not len(kwargs):
        print("Nobody is hungry.")
    for name, food in kwargs.items():
        print(f"{name} loves to eat {food}.")

favorite_food(john = "pizza", jack = "pumkin", jay = "chicken noodle", ken = "burger")
print("")
favorite_food(john = "pizza", jack = "pumkin")
print("")
favorite_food()
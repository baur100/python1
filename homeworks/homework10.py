# 1. Создайте функцию greeting - которая принимает некоторое количество аргументов
# если среди агрументов есть слово "python" - выведите 'Hello, Snake'
# если среди агрументов есть слово "qa" - выведите 'Hello, QA Engineer'
# если среди агрументов есть слово "bee" - выведите 'Hello, Maya'
# если среди агрументов есть слово "world" - выведите 'Hello, World'
# //extra во всех остальных случаях - "I don't know you"

# если больше одного - выведите все доступные фразы

# прогоните следующие тесткейсы
# greeting("Hi",45,True,"python")
# greeting("bee",1212,True,"python", False,True)
# greeting("world")
# greeting("qa",45,True,"bee","world","python",67,True,"Some words")
# greeting()
# greeting("hummus","tomato soup","wink",True)
# Hint - user if in for

print("#1...")
print("")
print("First use case:")
print("")


def greeting1(*args):
    print(args)
    if 'python' in args:
        print("Hello, snake")
    elif 'QA' in args:
        print("Hello, Engineer!")
    elif 'bee' in args:
        print(f"Hello, Maya!")
    elif 'world' in args:
        print("Hello, world!")
    else:
        print("I don't know you")


greeting1('Hi', 45, True, 'python')

print("")
print("Second use case:")
print("")


def greeting2(*args):
    print(args)
    if 'python' in args:
        print("Hello, snake")
    elif 'QA' in args:
        print("Hello, Engineer!")
    elif 'bee' in args:
        print(f"Hello, Maya!")
    elif 'world' in args:
        print("Hello, world!")
    else:
        print("I don't know you")


greeting2("bee", 1212, True, "python", False, True)

print("")
print("Third use case:")
print("")


def greeting3(*args):
    print(args)
    if 'python' in args:
        print("Hello, snake")
    elif 'QA' in args:
        print("Hello, Engineer!")
    elif 'bee' in args:
        print(f"Hello, Maya!")
    elif 'world' in args:
        print("Hello, world!")
    else:
        print("I don't know you")


greeting3("world")

print("")
print("Fourth use case:")
print("")


def greeting4(*args):
    print(args)
    if 'python' in args:
        print("Hello, snake")
    elif 'QA' in args:
        print("Hello, Engineer!")
    elif 'bee' in args:
        print(f"Hello, Maya!")
    elif 'world' in args:
        print("Hello, world!")
    else:
        print("I don't know you")


greeting4("qa", 45, True, "bee", "world", "python", 67, "Some words")

print("")
print("Fifth use case:")
print("")


def greeting5(*args):
    print(args)
    if 'python' in args:
        print("Hello, snake")
    elif 'QA' in args:
        print("Hello, Engineer!")
    elif 'bee' in args:
        print(f"Hello, Maya!")
    elif 'world' in args:
        print("Hello, world!")
    else:
        print("I don't know you")


greeting5()
print("")
print("Sixth use case:")
print("")


def greeting6(*args):
    print(args)
    if 'python' in args:
        print("Hello, snake")
    elif 'QA' in args:
        print("Hello, Engineer!")
    elif 'bee' in args:
        print(f"Hello, Maya!")
    elif 'world' in args:
        print("Hello, world!")
    else:
        print("I don't know you")


greeting5("hummus", "tomato soup", "wink", True)

print("end of task #1...")

print("")


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

print("Task #2...")
print("First use case: ")
print("")


def who_are_you1(*args):
    print(args)
    if 'python' and 'pycharm' in args:
        print('Hello python')
    elif 'java' and 'netbeans' in args:
        print('Hello, java')
    else:
        print('I don\'t know you')  # to look for the \ symbol


who_are_you1("python", 1212, True, "python", False, True)

print("")
print("Second use case:")
print("")


def who_are_you2(*args):
    print(args)
    if 'python' and 'pycharm' in args:
        print('Hello python')
    elif 'java' and 'netbeans' in args:
        print('Hello, java')
    else:
        print('I don\'t know you')  # to look for the \ symbol


who_are_you2("python", 1212, True, "pycharm", False, True)

print("")
print("Third use case:")
print("")


def who_are_you3(*args):
    print(args)
    if 'python' and 'pycharm' in args:
        print('Hello python')
    elif 'java' and 'netbeans' in args:
        print('Hello, java')
    else:
        print('I don\'t know you')  # to look for the \ symbol


who_are_you3('world')

print("")
print("Forth use case:")
print("")


def who_are_you4(*args):
     print(args)
     if 'python' and 'pycharm' in args:
         print('Hello python')
     elif 'java' and 'netbeans' in args:
         print('Hello, java')
     else:
         print('I don\'t know you')  # to look for the \ symbol


who_are_you4("qa", 45, True, "java", "world", "netbeans", 67, True, "Some words")

print("")
print("Fifth use case:")
print("")


def who_are_you5(*args):
    print(args)
    if 'python' and 'pycharm' in args:
        print('Hello python')
    elif 'java' and 'netbeans' in args:
        print('Hello, java')
    else:
        print('I don\'t know you')  # to look for the \ symbol


who_are_you5()

print("")

# 3. Создайте функцию favorite_food() - которая принимает некоторое количество именнованых аргументов аргументов
# в следующем виде name = food
# выведите на экран - name loves eat food - для всех аргументов
# favorite_food(john = "pizza", jack = "pumkin", jay = "chicken noodle", ken = "burger")
# favorite_food(john = "pizza", jack = "pumkin")
# favorite_food()


print("Third task...")
print("")


def favorite_food(**kwargs):
    print(kwargs)
    for key, value in kwargs.items():
        print(f"{key} loves to eat {value}")


favorite_food(John='Pizza', Jack='Pumpkin', Jay='Chicken noodle', Ken='Burger')


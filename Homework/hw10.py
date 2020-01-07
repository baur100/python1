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
# 3. Создайте функцию favorite_food() - которая принимает некоторое количество именнованых аргументов аргументов
# в следующем виде name = food
# выведите на экран - name loves eat food - для всех аргументов
# favorite_food(john = "pizza", jack = "pumkin", jay = "chicken noodle", ken = "burger")
# favorite_food(john = "pizza", jack = "pumkin")
# favorite_food()

##########11111111111111111##############

def greeting (*args):
  if "python" in args:
      print ('Hello, Snake')
  if "qa" in args:
      print ('Hello, QA Engineer')
  if "bee" in args:
      print ('Hello, Maya')
  if "world" in args:
      print ('Hello, World')
  else:
      print ("I don't know you")

greeting("Hi",45,True,"python")
greeting("bee",1212,True,"python", False,True)
greeting("world")
greeting("qa",45,True,"bee","world","python",67,True,"Some words")
greeting()
greeting("hummus","tomato soup","wink",True)

###########2222222222222222222#########################


def who_are_you(*args):
  if "python" and "pycharm" in args:
     print ('Hello python')
  if "java" and "netbeans" in args:
     print ('Hello, java')
  else:
     print("I don't know you")
who_are_you("java",45,True,"python")
who_are_you("python",1212,True,"python", False,True)
who_are_you("python",1212,True,"pycharm", False,True)
who_are_you("world")
who_are_you("qa",45,True,"java","world","netbeans",67,True,"Some words")
who_are_you()

###########333333333333333#########################


def favorite_food(**kwargs):
    for key,value in kwargs.items():
      print(f"{key} , {value}")
favorite_food(john="pizza", jack="pumkin", jay="chicken noodle", ken="burger")
favorite_food(john = "pizza", jack = "pumkin")
favorite_food()

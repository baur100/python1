# 1. Создайте функцию greeting - которая принимает некоторое количество аргументов
# если среди агрументов есть слово "python" - выведите 'Hello, Snake'
# если среди агрументов есть слово "qa" - выведите 'Hello, QA Engineer'
# если среди агрументов есть слово "bee" - выведите 'Hello, Maya'
# если среди агрументов есть слово "world" - выведите 'Hello, World'
# //extra во всех остальных случаях - "I don't know you"
#
# если больше одного - выведите все доступные фразы
#
# прогоните следующие тесткейсы
#
# greeting("Hi",45,True,"python")
# greeting("bee",1212,True,"python", False,True)
# greeting("world")
# greeting("qa",45,True,"bee","world","python",67,True,"Some words")
# greeting()
# greeting("hummus","tomato soup","wink",True)

def greeting(*args):
    if "python" in args:
        print("Hello, Snake")
    if "qa" in args:
        print("Hello, QA Engineer")
    if "bee" in args:
        print("Hello, Maya")
    if "world" in args:
        print("Hello, World")

    count = 0
    for el in args:
        if el =="python" or el =="qa" or el =="bee" or el=="world" :
            count = 1

    if count == 0:
        print("I don't know you")



greeting("Hi",45,True,"python")
greeting("bee",1212,True,"python", False,True)
greeting("world")
greeting("qa",45,True,"bee","world","python",67,True,"Some words")
greeting()
greeting("hummus","tomato soup","wink",True)
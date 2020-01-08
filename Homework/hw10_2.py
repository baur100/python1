# 2. Создайте функцию who_are_you() - которая принимает некоторое количество аргументов
# если среди агрументов есть слово "python" и "pycharm" - выведите 'Hello python'
# если среди агрументов есть слово "java" и "netbeans"- выведите 'Hello, java'
# extra во всех остальных случаях - "I don't know you"
# прогоните следующие тесткейсы
#
# who_are_you("java",45,True,"python")
# who_are_you("python",1212,True,"python", False,True)
# who_are_you("python",1212,True,"pycharm", False,True)
# who_are_you("world")
# who_are_you("qa",45,True,"java","world","netbeans",67,True,"Some words")
# who_are_you()

def who_are_you(*args):
    count = 0
    if "python" and "pycharm" in args:
        print("Hello python")
    elif "java" and "netbeans" in args:
        print("Hello, java")
    else:
        print("I don't know you")


who_are_you("java",45,True,"python")
who_are_you("python",1212,True,"python", False,True)
who_are_you("python",1212,True,"pycharm", False,True)
who_are_you("world")
who_are_you("qa",45,True,"java","world","netbeans",67,True,"Some words")
who_are_you()
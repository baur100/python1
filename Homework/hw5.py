#Создайте range из положительных четных чисел от 15 до 27 с шагом 3 -
# выведите его на экран

print("---excercise 1---")
ran1 = range(15,28,3)
print(f"Print positive even elements of {ran1}:")
for el in ran1:
    if el%2 == 0:
        print(el)

# Создайте range из положительных четных чисел от -15 до 27 с шагом 3 -
# выведите его на экран

print("---excercise 2---")
ran2 = range(-15,28,3)
print(f"Print positive elements of {ran2}:")

for el in ran2:
    if el%2 == 0 and el>0:
        print(el)

# Создайте list из 10 элементов со случайными положительными числами от 0 до 100 -
# выведите cамое большое и самое маленькое и сумму всех его элементов

print("---excercise 3---")
lst = [2, 13, -4, 7, 437, 3, 0, -345, 9, 100]
print(f"Print max, min and sum of list elements {lst}:")

min = 0
max = 0
sum = 0

for i in range(len(lst)):
    if lst[i] < min:
        min = lst[i]

    if lst[i] > max:
        max = lst[i]

    sum +=lst[i]

print(f"min element = {min}")
print(f"max element = {max}")
print(f"sum of elements = {sum}")

# Создайте list с элементами типа int и дайте ему следующие значения:
# [10,15,12,7,88,10,6,17,23,10,10,16]
# Выведите на экран все индексы где в массиве хранится 10

print("---excercise 4---")

lll = [10,15,12,7,88,10,6,17,23,10,10,16]
print(f"Print all indexes of element 10 from the list {lll}")
for i in range(len(lll)):
    if lll[i] == 10:
        print(f"index = {i}")


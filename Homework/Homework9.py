# 1. Создайте метод sum_5p - который в качестве аргумента берет 5 целых числел и печатает их результат на экране.
def sum_5p(x1, x2, x3, x4, x5):
    print(f"Sum of {x1}, {x2}, {x3}, {x4}, and {x5} is {x1+x2+x3+x4+x5}.")

sum_5p(11, 4, 13, 5, 12)

# 2. Создайте метод sum_5 - который в качестве аргумента берет 5 целых числел и возвращает их сумму.
# сохраните результат в переменной и выведите результат на экран
def sum_5(x1, x2, x3, x4, x5):
    return x1+x2+x3+x4+x5

a1=4
a2=1
a3=5
a4=10
a5=3
sum=sum_5(a1, a2, a3, a4, a5)
print (f"Sum of {a1}, {a2}, {a3}, {a4}, and {a5} is {sum}.")

# 3. Создайте метод isEven - который в качестве аргумента берет целое число и если оно четное возвращает true
# если нечетное - возвращает false
# Выведите на экран в виде

# ----------
# Число хх является четным
# ----------
def isEven(num):
    if num%2:
        return False
    else:
        return True
b=12
print ("-----------------")
print (f"Число {b} является ", end="")
if isEven(b):
    print("четным.")
else:
    print("не четным.")
print("-----------------")

# 4. Создайте метод min_max - принимает в качнстве аргумента list и возвращает 2 числа - максимальное и минимальное

def min_max(l):
    ma=mi=l[0]
    for i in l:
        if i>ma:
            ma=i
        elif i<mi:
            mi=i
    return ma, mi

l1=[5, 103, -11, -5, 45, 74, -1, 102]
v, w=min_max(l1)
print(f"Max value of the list is {v}.")
print(f"Min value of the list is {w}.")

# 5. 2 примера dictionary выведите его содержимое на экран
print (" ")
d={
    "name":"Peter",
    "age":18,
    "interest":"box",
    "book":"Long Island",
    "car":"Toyota",
}

for item in d.items():
    print(item)

d["car"] ="Honda"
print (f"Dictionary: {d}")

d.pop("age")
print(f"Dictionary after pop(): {d}")

print ("-------------------")

d1={
    "flower": "daisy",
    "color":"blue",
    "number": 126,
    "another_number": 9154,
    "animal": "monkey"
}

print(f" Animal is {d1.get('animal')}")
print(" ")
print("These are key - value in the distionary: ")
for i in d1:
    print(f"{i} - {d1[i]}")
print(" ")
print("And these are just values:")
for h in d1.values():
    print(h)
print(" ")
d1.popitem()
print(f"Dictionary after popitem(): {d1}")
del d1["another_number"]
print(f"Dictionary after del: {d1}")
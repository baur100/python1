#  Создайте метод sum_5p - который в качестве аргумента берет 5 целых числел и печатает их результат на экране.
def sum_5p(a, b, c, d, e):
    print(f"the sum is  {a + b + c + d + e}")


sum_5p(10, 20, 30, 40, 50)
print("")


# 2. Создайте метод sum_5 - который в качестве аргумента берет 5 целых числел и возвращает их сумму.
# сохраните результат в переменной и выведите результат на экран
def sum_5(a, b, c, d, e):
    return a + b + c + d + e


f = sum_5(12, 14, 16, 18, 20)
print("")


# 3. Создайте метод isEven - который в качестве аргумента берет целое число и если оно четное возвращает true
# если нечетное - возвращает false
# Выведите на экран в виде
# ----------
# Число хх является четным
# ----------
def isEven(num):
    if num % 2 == 0:
        return True
    else:
        return False


n = isEven(578)
print(n)
print("")

# # 4. Создайте метод min_max - принимает в качнстве аргумента list и возвращает 2 числа - максимальное и минимальное
# ------------------->>> unable to do this need some help <<<---------------------
print(" :(((((((")
print("")

# 5. 2 примера dictionary выведите его содержимое на экран
# -----------------------------------------------------------------------------------------------------------------------
dict1 = {"County": "USA", "Year": "2020", "Since": "2015"}
for d in dict1:
    print(f"{d} - {dict1[d]}")


print("")
for b in dict1.values():
    print(f"{dict1}")

print("")

print("")
for el in dict1.items():
    print(f"{el}")

print("")

dict2 = {
    "color": "red",
    "car": "Lexus",
    "country":"US",
    "age":"26",
    "exp":"4"
}
for i in dict2:
    print(f"{i} - {dict2[i]}")
print("")
print("finito")
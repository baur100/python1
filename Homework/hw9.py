# Создайте метод sum_5p - который в качестве аргумента берет 5 целых числел и печатает их результат на экране.

def sum_5p(x1,x2,x3,x4,x5):
    s= x1+x2+x3+x4+x5
    print(f"Sum = {s}")


sum_5p(1,2,3,4,5)

# Создайте метод sum_5 - который в качестве аргумента берет 5 целых числел и возвращает их сумму.
# сохраните результат в переменной и выведите результат на экран

def sum_5p(x1,x2,x3,x4,x5):
    return x1+x2+x3+x4+x5

print(f"Sum = {sum_5p(2,4,6,8,10)}")

# Создайте метод isEven - который в качестве аргумента берет целое число и если оно четное возвращает true
# если нечетное - возвращает false
# Выведите на экран в виде

def is_even(i):
    if not type(i) == int:
        return "Number is not an integer!"
    elif i%2 == 0:
        return True
    else:
        return False


print(is_even(10.2))
print(is_even(100))
print(is_even(105))

#Dictionaries

d = {}

d["1"]= "One"
d["2"]= "Two"
d["3"]= "Three"
d["4"] = "Four"
d["5"] = "Five"
print(f"Print dictionary {d}")

for el in d:
    print(f"Key is {el}, value is {d[el]}")

for el in d.values():
    print(f"Only value: {el}")

for el in d.items():
    print(f"Print tuple: {el}")


any_key= '2'
print(f"Print value of a key {any_key}: {d.get(any_key)}")


# Number to text

def number_to_text(num):
    s_num = str(num)
    if s_num in d:
        print(f"Number {s_num} is {d[s_num]}")
    else:
        print(f"Number {s_num} is not in a dictionary!")


num1 = 4
num2 = 10
num3 = 2
number_to_text(num1)
number_to_text(num2)
number_to_text(num3)



a=5
b=10
c=10
d=0

if 1 is True:
    print(True)
else:
    print(False)


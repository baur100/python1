
# 1. Создайте метод sum_5p - который в качестве аргумента берет 5 целых числел и печатает их результат на экране.

def sum_5p(a,b,c,d,f):
    print (a,b,c,d,f)
sum_5p(12,333,21,44,55)

#2. Создайте метод sum_5 - который в качестве аргумента берет 5 целых числел и возвращает их сумму.
#сохраните результат в переменной и выведите результат на экран



def sum_5p(a,b,c,d,f):
    i = a+b+c+d+f
    return i
print (sum_5p(22,33,44,55,66))

#3. Создайте метод isEven - который в качестве аргумента берет целое число и если оно четное возвращает true
#если нечетное - возвращает false
#Выведите на экран в виде

def isEven (a):

    if (a % 2) == 0:
        print ("The number is Even")
    else:
        print("The number is Odd")
isEven(10)


def isEven(num):
    number=(num/2)*2
    if(number==num):
        print(num, "is a even number");
    else:
        print(num, "is a odd number");
isEven(10)

# 5. 2 примера dictionary выведите его содержимое на экран

menu = {"oatmeal": 3, "avocado toast": 6, "carrot juice": 5, "blueberry muffin": 2}
print (menu)

sensors =  {"living room": 21, "kitchen": 23, "bedroom": 20}
print(sensors)
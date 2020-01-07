#
#
#
# # def sum_numbers(num1,num2,num3,num4=0,num5=0,num6=0):
# #     return num1+num2+num3+num4+num5+num6
#
# def sum_numbers(*args):
#     summa = 0
#     for x in args:
#         summa+=x
#     return summa
#
# # print(sum_numbers(1,2,3,3,2))
# # print(sum_numbers(1,2,3))
# # print(sum_numbers())
#
# def find_red(*args):
#     print(args)
#     if "red" in args:
#         print("we have red")
#     else:
#         print("no red")
#
# find_red(True,24,False, 0,"car",)
# find_red()
#
#
#

# def print_me(first_name, last_name,age):
#     print(f"Name: {first_name}, Surname: {last_name}, age: {age}")



# def print_me(**kwargs):
#     for key,value in kwargs.items():
#         print(f"{key} , {value}")
#
# print_me(last_name="Ivanoff", age=32, first_name="Ivan")

# def sum_numbers(*args):
#     print(args)
#     summa = 0
#     for x in args:
#         summa+=x
#         print(summa)
#     return summa
#
# a = [1,4,6,8]
# b=(2,4,6,8,9)
# c = {4,5}
# print(sum_numbers(*a))
# print(sum_numbers(*b))
# print(sum_numbers(*c))

# def print_me(**kwargs):
#     for key,value in kwargs.items():
#         print(f"{key} , {value}")
#
# xx = {"a":"54","n":"vasya"}
#
# print_me(**xx)

a = 50


def isEven(a):
    print(bool(a%2))
    if a%2==1:
        return False
    return True


if isEven(a):
    print(f"{a} is even")
else:
    print(f"{a} is odd")

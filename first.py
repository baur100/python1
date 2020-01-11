#
# numbers = [2,1,3,5,6,7,4,5,8,18,9]
# dict = {"ff":"xx"}
#
# # print (x) NameError
# # print(numbers[100]) IndexError:
# # x = numbers + 'hello' TypeError
# # int("foo") ValueError
# # dict["cc"] KeyError
# # "hello".foo AttributeError
# # 5/0 ZeroDivisionError
#
# def get_birth_year(age):
#     if type(age) is not int:
#         raise TypeError("Argument must be integer")
#     if age<0 or age >125:
#         raise ValueError("Wrong age entered")
#     print(2020-age)
#
#
# try:
#     get_birth_year("gi")
#
# # except TypeError:
# #     print("wrong Type entered")
# except:
#     print("got error")
# # else:
# #     print("we in else")
# # finally:
# #     print("finallyregergergergre")
#
#
# # print("finish")
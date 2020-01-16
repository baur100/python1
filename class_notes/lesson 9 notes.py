
list = [4,"f",78]
tuple = ("d","word",90)
set = {4,67,"34","x"}

dictionary = {
    "car": "toyota",
    "plane":"boing",
    "year":2020
}
# print(dictionary)

# print(dictionary["plane"])
# print(dictionary.get("year"))

# for xx in dictionary:
#     print(xx)
#
# for zz in dictionary:
#     print(dictionary[zz])

# for yy in dictionary.values():
#     print(yy)

# for ssd in dictionary.items():
#     print(ssd)

# print(len(dictionary))

# dictionary["game"]="football"
# # print(dictionary)
# 
# dictionary.pop("plane")
# print(dictionary)
# 
# dictionary.popitem()
# print(dictionary)
# 
# del dictionary["year"]
# print(dictionary)
####################################################
# d=2
#
# def multiple_3_numbers(a1,a2,a3):
#     # global b
#     b=a1*a2*a3*d
#     return b
#
# print(multiple_3_numbers(1,1,3))
# # print(b)

# def some_math(a=1,b=1,c=1,d=1):
#     result = a*b + c*d
#     return result
#
# zz=some_math(1,2,3,4)
# print(zz)
#
# zz=some_math(1,2,3)
# print(zz)
#
# zz=some_math()
# print(zz)

def func(a=3,b=2,c=4,d=False):
    if(d):
        dd=a*b*c
    else:
        dd=a+b+c
    return dd

print(func(3,2,4))
print(func(3,2,4, False))
print(func(3,2,4,True))
print(func(3,2,4,0))
print(func(3,2,4,"word"))
print(func(True))
print(func(d=True))




person_1 = 12
person_2 = 65
person_3 = 2


price = 1000
# if person_1 < 3:
#     print(f"ticket price for person_1  is - {price*0}")
# elif person_1 < 13:
#     print(f"ticket price for person_1  is - {price*0.6}")
# elif person_1 < 66:
#     print(f"ticket price for person_1  is - {price * 1}")
# else:
#     print(f"ticket price for person_1  is - {price * 0.8}")
#
# if person_2 < 3:
#     print(f"ticket price for person_2  is - {price*0}")
# elif person_2 < 13:
#     print(f"ticket price for person_2  is - {price*0.6}")
# elif person_2 < 66:
#     print(f"ticket price for person_2  is - {price * 1}")
# else:
#     print(f"ticket price for person_2  is - {price * 0.8}")
#
# if person_3 < 3:
#     print(f"ticket price for person_3  is - {price*0}")
# elif person_3 < 13:
#     print(f"ticket price for person_3  is - {price*0.6}")
# elif person_3 < 66:
#     print(f"ticket price for person_3  is - {price * 1}")
# else:
#     print(f"ticket price for person_  is - {price * 0.8}")

# def get_ticket_price(age):
#     if age < 3:
#         return f"ticket price for passenger  is - {price *0}"
#     elif age < 13:
#         return f"ticket price for passenger  is - {price *0.6}"
#     elif age < 66:
#         return f"ticket price for passenger  is - {price * 1}"
#     else:
#         return f"ticket price for passenger  is - {price * 0.8}"
#
# print(get_ticket_price(person_1))
# print(get_ticket_price(person_2))
# print(get_ticket_price(person_3))

#
# def sum_3(a,b,c):
#     return a+b+c
#
# a,b,c = 3,6,8
#
# d = sum_3(a,b,c)
# print(d)
#
# print ( sum_3(2,89,6))
#
#
# def multiple_four_numbers(a1,a2,a3,a4):
#     return a1*a2*a3*a4
#
# ss = multiple_four_numbers(a,b,c,a)
# print(ss)
#
# def say_my_name(name):
#     print(f"hello {name}")
#
# me = "Baur"
# say_my_name(me)
# say_my_name("Dima")

def circle_area(radius):
    area = 3.1415 * radius ** 2
    return area

r1 = 10
r2 = 15
r3 = 20

area1 = circle_area(r1)
area2 = circle_area(r2)
area3 = circle_area(r3)

print(f"a1 = {area1} a2 = {area2} a3 = {area3}")


def get_list_max(list):
    if(not len(list)):
        return -1000
    max = list[0]
    for x in list:
        x = int(x)
        if x > max:
            max = x
    return max

a = [10,20,30,40,15,12,7]
b = []
c = [9,15]
d = [1]
e = [10,20,30,40,15,"12",7]

print(get_list_max(a))
print(get_list_max(b))
print(get_list_max(c))
print(get_list_max(d))
print(get_list_max(e))

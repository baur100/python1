# numbers = [2,1,3,5,6,7,4,5,8,18,9]
# colors = ['red', 'green', 'blue', 'pink', 'black', 'brown', 'grey','white','yellow']
# используя
# map
# из numbers создайте новый лист все элементы которого будут numbers в квадрате
# из colors создайте новый лист все элементы которого будут написаны заглавными буквами
# (google how to transfer str to uppercase)
# filter
# из numbers создайте новый лист который содержит только четные и меньше 7
# из colors создайте новый лист который будет в котором будет цвета начинающиеся на 'b' или имеющие 4 буквы


# из numbers создайте новый лист все элементы которого будут numbers в квадрате


numbers = [2,1,3,5,6,7,4,5,8,18,9]

v_kvadrate = list(map(lambda x: x ** 2, numbers))
print (v_kvadrate)


# из colors создайте новый лист все элементы которого будут написаны заглавными буквами


colors = ['red', 'green', 'blue', 'pink', 'black', 'brown', 'grey','white','yellow']
uppercase = list(map(lambda x: x.upper(), colors))
print (uppercase)

# из numbers создайте новый лист который содержит только четные и меньше 7


for x in numbers:
    y=[]
    if x < 7 and x%2==0:
        y.append(x)
    print(y)

# я не знаю как распечатать в таком виде [2,6,4]

# из colors создайте новый лист который будет в котором будет цвета начинающиеся на 'b' или имеющие 4 буквы

colors = ['red', 'green', 'blue', 'pink', 'black', 'brown', 'grey','white','yellow']
new_list = []
for x in colors :
    if x[0] == "b" or len(x) ==4:
     new_list.append(x)

print(new_list)

#i = list(filter(lambda x  : x[0] == "b" or len(x) ==3 , colors))








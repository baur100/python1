# numbers = [2,1,3,5,6,7,4,5,8,18,9]
# colors = ['red', 'green', 'blue', 'pink', 'black', 'brown', 'grey','white','yellow']
# используя map
# из numbers создайте новый лист все элементы которого будут numbers в квадрате
# из colors создайте новый лист все элементы которого будут написаны заглавными буквами

numbers = [2,1,3,5,6,7,4,5,8,18,9]
colors = ['red', 'green', 'blue', 'pink', 'black', 'brown', 'grey','white','yellow']

squared_numbers = list((map(lambda x: x*x, numbers)))
print(squared_numbers)

upper_colors = list(map(lambda x: x.upper(), colors))
print(upper_colors)

# из numbers создайте новый лист который содержит только четные и меньше 7
# из colors создайте новый лист в котором будут цвета начинающиеся на 'b' или имеющие 4 буквы

even_numbers = list(filter(lambda x: x%2 == 0 and x < 7, numbers))
print(even_numbers)

b_colors = list(filter(lambda x: x[0] == 'b' or len(x) == 4, colors))
print(b_colors)



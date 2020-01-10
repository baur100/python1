numbers = [2, 1, 3, 5, 6, 7, 4, 5, 8, 18, 9]
colors = ['red', 'green', 'blue', 'pink', 'black', 'brown', 'grey', 'white', 'yellow']
print()

print('#1...\n из numbers создайте новый лист все элементы которого будут numbers в квадрате')
squared = list(map(lambda s: s ** 2, numbers))
print(squared)
print()

print('#2...\n из colors создайте новый лист все элементы которого будут написаны заглавными буквами')
print(f"unmodified list - {colors}")
upCol = list(map(lambda c: c.upper(), colors))
print(upCol)

print('#3... \n из numbers создайте новый лист который содержит только четные и меньше 7')
evnNums = list(filter(lambda n: (not n%2) and n < 7, numbers))
print(evnNums)


print('#4... \n из colors создайте новый лист который будет в котором будет цвета начинающиеся на \'b\' или имеющие 4 буквы ')
print('The following statements filter values by letter \'b\' ')
b_mapped = list(filter(lambda x: x[0] == 'b', colors))
print(b_mapped)

print('\n the following statement filters values by first four letters')
filteredByFour = list(filter(lambda x: len(x) == 4, colors))
print(filteredByFour)

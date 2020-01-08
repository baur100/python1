# 3. Создайте функцию favorite_food() - которая принимает некоторое количество именнованых аргументов
# в следующем виде name = food
# выведите на экран - name loves eat food - для всех аргументов
# favorite_food(john = "pizza", jack = "pumkin", jay = "chicken noodle", ken = "burger")
# favorite_food(john = "pizza", jack = "pumkin")
# favorite_food()

def favorite_food(**kwargs):
    for key in kwargs:
        print(f"{key} loves food {kwargs[key]}")

favorite_food(john = "pizza", jack = "pumkin", jay = "chicken noodle", ken = "burger")
favorite_food(john = "pizza", jack = "pumkin")
favorite_food()

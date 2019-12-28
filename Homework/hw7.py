# 1 Create tuple with 5 members
# a. print all members (use for loop)
# b. print 2 last members
# c. assign tuple members to 5 variables

print("Excercise 1-----------------------------------")

my_tuple = (3,"red", [2,8], ("car", "plane", "bus"), 2.78)
print(f"Print all elements of the tuple {my_tuple}:")
for el in my_tuple:
    print(f"Element {el} with type {type(el)}")

print(f"First from the end element: {my_tuple[-1]}")
print(f"Second from the end element: {my_tuple[-2]}")

a,b,c,d,e = my_tuple

print(f"variable a = {a}")
print(f"variable b = {b}")
print(f"variable c = {c}")
print(f"variable d = {d}")
print(f"variable e = {e}")


# 2. create set with 5 elements
# a. add "apple" to set
# b. print all elements using for loop
# c. add "mango" to set
# d. remove any element from set

print("Excercise 2-----------------------------------")

my_set = {"pineapple", "cherry", "banana", "pear", "orange"}
print(f"Initial set {my_set}")

my_set.add("apple")
print(f"Set with added 'apple' {my_set}")

for el in my_set:
    print(f"Set element {el}")

my_set.add("mango")
print(f"Set with added 'mango' {my_set}")

my_set.remove("apple")

print(f"Set after removing 'apple' {my_set}")


# 3. make 2 examples using while loop

print("Excercise 3-----------------------------------")

num = 10
while num > 0:
    print(num)
    num -= 1

print()

my_list= ["first", "middle", "last"]
while my_list:
    print(my_list)
    my_list.pop(-1)










print("Homework-7")

print("Create tuple with 5 members--------------------------------------------------")
my_tuple = ("Mon", 2, "Wed", 4.2, "Fri")

print("Print all members (use for loop)---------------------------------------------")
for i in my_tuple:
    print(i)

print("print 2 last members---------------------------------------------------------")
print(f"my last value is {my_tuple[-1]}")
print(f"my previous before last value is {my_tuple[-2]}")


print("assign tuple members to 5 variables------------------------------------------")
a, b, c, d, e = my_tuple


print("create set with 5 elements---------------------------------------------------")
my_set = {"JS", "Python", "scala", "CSS", "nodejs"}
print(my_set)


print("add 'apple' to set-----------------------------------------------------------")
my_set.add("Ruby")
print(f"print {my_set} with added value")


print("print all elements using for loop--------------------------------------------")
for i in my_set:
    print(f"printing all elements using for loop {i}")


print("add 'mango'' to set-----------------------------------------------------------")
my_set.add("mango")
print(f"printing a set with an added value {my_set}")


print("remove any element from set---------------------------------------------------")
my_set.remove("mango")
print(f"removing element with 'remove method {my_set}")
print(f"removing element with discard method {my_set}")

print("make 2 examples using while loop----------------------------------------------")
number = 26
while number > 2:
    print(number)
    number -= 3




# USE print(f"") in exercises

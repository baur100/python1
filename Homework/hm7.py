# 1 Create tuple with 5 members
# a. print all members (use for loop)
# b. print 2 last members
# c. assign tuple members to 5 variables
# 2. create set with 5 elements
# a. add "apple" to set
# b. print all elements using for loop
# c. add "mango" to set
# d. remove any element from set
# 3. make 2 examples using while loop
# USE print(f"") in exercises

# 1 Create tuple with 5 members


tuple_1 = (1, 4, 7, "car", "plane")
for i in tuple_1:
# a. print all members (use for loop)
    print(i)

# b. print 2 last members
print (tuple_1[-2])

# c. assign tuple members to 5 variables
var_1 = tuple_1[0]
var_2 = tuple_1[1]
var_3 = tuple_1[2]
var_4 = tuple_1[3]
var_5 = tuple_1[4]

# 2. create set with 5 elements
set_1 = {"grape", "cherry", "peach", "plum", 10 }

# a. add "apple" to set
set_1.add("apple")

# b. print all elements using for loop
for x in set_1:
    print(x)

# c. add "mango" to set
set_1.add("mango")
print(set_1)

# d. remove any element from set
set_1.remove(10)
print(set_1)


# 3. make 2 examples using while loop

x = 1
while x < 10:
    print(x)
    x +=1

while True:
    print("infinity")

# USE print(f"") in exercises

name = "Vladimir"
country = "Russia"
print ( f"My name is  {name}. I am from {country}" )












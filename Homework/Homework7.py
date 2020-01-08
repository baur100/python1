# 1. Create tuple with 5 numbers
my_tuple=(3,7,5,8,1)

# a. print all members (use for loop)
for i in my_tuple:
    print(i)

# b. print 2 last members
print(f"The last two members are {my_tuple[-2]} and {my_tuple[-1]}")

# c. assign tuple members to 5 variables
z,y,x,v,w=my_tuple

#  2. create set with 5 elements
my_set={"car","toy","jewelry", "purse", "watch"}

#  a. add "apple" to set
my_set.add("apple")

#  b. print all elements using for loop
for el in my_set:
    print(el)

#  c. add "mango" to set
my_set.add("mango")

#  d. remove any element from set
my_set.discard("jewelry")

print(f"The set looks right now: {my_set}")

#  3. make 2 examples using while loop
#  Use print(f"") in exercises
print("Multiplication by 3:")
ind=1
while ind<=10:
    print(f"3 * {ind} = {ind*3}")
    ind+=1

i=1
while i<9:
    print("*  ", end="")
    j=2
    while j<8:
        if i==1 or i==8:
            print("*  ", end="")
        else:
            print("   ", end="")
        j+=1
    print("*")
    i+=1

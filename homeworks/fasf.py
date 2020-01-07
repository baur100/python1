d1={
    "flower": "daisy",
    "color":"blue",
    "number": 126,
    "another_number": 9154,
    "animal": "monkey"
}

print(f" Animal is {d1.get('animal')}")
print(" ")
print("These are key - value in the distionary: ")
for i in d1:
    print(f"{i} - {d1[i]}")
print(" ")
print("And these are just values:")
for h in d1.values():
    print(h)
print(" ")
d1.popitem()
print(f"Dictionary after popitem(): {d1}")
del d1["another_number"]
print(f"Dictionary after del: {d1}")
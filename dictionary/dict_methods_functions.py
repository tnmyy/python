d = {
    "John": 1,
    "Jacob": 2,
    "Donald": 3,
    "Georgia": 4,
    "Joe": 6,
    "Ben": 5,
}

# 1. len()
print("# 1. len()")
print(len(d))

d["Steve"] = 7
print(len(d))

# Accessing Items, Keys and Values: get(), items(), keys,(), values()

# 2. get(key, [callback])
# to get value of the given key
print("\n# 2. get()")
print(d.get("John"))
print(d.get("travis"))  # key not found => None
print(d.get("john", "Oh No!! man, key not found"))

# 3. items()
# it returns a list of tuples
# get all the items (key:value) of a dictionary in a tuple
print("\n# 3. items()")
di = d.items()
print(di)
print(type(di), len(di))

di = list(di)
print(di)

for x in di:
    print(x)

for a, b in di:
    print(a, b)

# 4. keys()
# to get all the keys of the dictionary in a list
print("\n# 4. keys()")
print(d.keys())
dk = list(d.keys())
print(dk)

# 5. values()
# to get all the values of the dictionary
print("\n# 5. values()")
print(d.values())
dv = list(d.values())
print(dv)

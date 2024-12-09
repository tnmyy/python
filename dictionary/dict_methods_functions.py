# d = {
#     "John": 1,
#     # "Jacob": 2,
#     # "Donald": 3,
#     # "Georgia": 4,
#     # "Joe": 6,
#     # "Ben": 5,
# }

# # 1. len()
# print("# 1. len()")
# print(len(d))

# d["Steve"] = 7
# print(len(d))

# # Accessing Items, Keys and Values: get(), items(), keys,(), values()

# # 2. get(key, [callback]) == dict[key]
# # to get value of the given key
# print("\n# 2. get()")
# print(d.get("John"))
# print(d.get("travis"))  # key not found => None
# print(d.get("john", "Oh No!! man, key not found"))

# # print(d["Jarvis"]) #RETURNS Error

# # 3. items()
# # it returns a list of tuples
# # get all the items (key:value) of a dictionary in a tuple
# print("\n# 3. items()")
# di = d.items()
# print(di)
# print(type(di), len(di))

# di = list(di)
# print(di)

# for x in di:
#     print(x)

# for a, b in di:
#     print(a, b)

# # 4. keys()
# # to get all the keys of the dictionary in a list
# print("\n# 4. keys()")
# print(d.keys())
# dk = list(d.keys())
# print(dk)

# # 5. values()
# # to get all the values of the dictionary
# print("\n# 5. values()")
# print(d.values())
# dv = list(d.values())
# print(dv)

# # Creating dictionary from fromkeys() method
# # creates a dictionary with same value but different keys
# # dict.fromkeys(<key_sequence>, <value>)
# # 6. fromkeys()
# print("\n# 6. fromkeys()")
# d = dict.fromkeys(["Amar", "Akbar", "Anthony"], 1000)
# print(d)

# d = dict.fromkeys(("He", "She", "It"))
# print(d)

# key_sequence it must be iterable
# d = dict.fromkeys(1)
# d = dict.fromkeys(
#     1,
# )
# print(d)

# Extend/Update dictionary with new key:value pairs via update() and setdefault() methods

# 7. setdefault()
# dict_name.setdefault(key, value)
# to insert a new key:value pair
# inserts new pairs IFF the key does not exists before else it returns the pre existing key's value
print("\n# 7. setdefault()")
d = dict(zip((1, 2, 3), (4, 5, 6)))
print(d)
x = d.setdefault(7, 9)
print(d)
print(x)  # returns the new inserted value
d.setdefault(18)
print(d)  # stores value as None

x = d.setdefault(2, 10)
print(x)  # returned previous value

# 8. update()
# to update or add key:value pairs
# merges the pairs from the new dictionary into the original dictionary, adding or replacing as needed. IF same keys than the value of the appended dictionary is used
# <d>.update(<d'>)
print("\n# 8. update()")
d = dict(zip((1, 2, 3), (4, 5, 6)))
d1 = dict(zip((3, 14, 15), (10, 11, 12)))
print(d, d1)
d.update(d1)
print(d)

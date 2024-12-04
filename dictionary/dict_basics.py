# Adding elements to dictionary
d = dict(name="tanmay", age=16)
print(d)
d["surname"] = "Upreti"
print(d)
# nesting dictionary
d = {"Bill": {"age": 25, "male": True}, "Sanya": {"age": 23, "male": False}}
print(d)

# Updating/Modifying existing element in a dictionary
# the key must be in the dict otherwise new entry will be made
emp = {"name": "John", "salary": 150, "male": True}
print(emp)
emp["salary"] = 69
print(emp)

# Deleting elements from a dictionary
emp = {"name": "John", "salary": 150, "male": True}
print(emp)
del emp["name"]
print(emp)

# del emp["name"] # key error
del emp
# print(emp) # emp is not defined now

# Checking for the existence of a key in a dictionary
emp = {"name": "John", "salary": 150, "male": True}
print("job" in emp)  # only checks for keys
print("name" in emp)
print("age" not in emp)

# Pretty printing a dictionary
# just to make it more readable
name = ("John", "Jacob", "Donald", "Georgia", "Joe", "Ben")
rank = (1, 2, 3, 4, 6, 5)
dict_rank = dict(zip(name, rank))
import json

print(dict_rank)
print(json.dumps(dict_rank, indent=2))

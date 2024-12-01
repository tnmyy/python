# DICTIONARIES = Key-Value Pairs
# MUTABLE
# AKA Associative arrays, Mappings or Hashes

# Making a dictionary

# Empty Dictionary
d = dict()
print(d, type(d))
# OR
d = {}
print(d, type(d))

# SYNTAX: {key: value, key: value}
# key = immutable type i.e. string, number or tuple(with immutable entries)

d = {"key": "value", 1: "value1"}
print(d)

# d = {[1,2]:'value'} ==> Give ERROR
# d = {"key": "value", "key": "value1"}

d = dict(a=1, b=2, c=3)
print(d)
# d =dict('a'=1, 'b'=2) # ERROR IDK why

# deep copy of dictionary
d1 = {"a": 1, "b": 2, "c": 3}
d2 = dict(d1)
print(d2)
d1["a"] = 123
print(d1)
print(d2)

# not a copy of dictionary
d3 = d1
d1["b"] = True
print(d1)
print(d3)

d = dict([("a", True), ("b", "123"), ("c", 1.9029)], x="Yo man")
print(d)

d = dict([("a", True), ("b", "123"), ("c", 1.9029)])
print(d)
d = dict([["a", True], ["b", "123"], ["c", 1.9029]])
print(d)
d = dict((("a", True), ("b", "123"), ("c", 1.9029)))
print(d)

# zip()
# The zip() function in Python combines multiple iterables such as lists, tuples, strings, dict etc, into a single iterator of tuples. Each tuple contains elements from the input iterables that are at the same position.
names = ["John", "Alice", "Bob", "Lucy"]
scores = [85, 90, 78, 92]

res = zip(names, scores)
d = dict(res)
print(d)

# ACCESSING THE ELEMENTS OF A DICTIONARY
# index => key
d = {"Rohit": 45, "Virat": 18, "Gill": 77, "Jaiwal": 64}
print(d)
print(d["Virat"])  # >> accessing items with keys
# print(d[1]) >> INDEXING not working
d = {45: "Rohit", 18: "Virat", 17: "ABD", 45: "Gayle", 17: "Rishabh"}
print(d[45])
d = {45: "Rohit", 18: "Virat", 17: "ABD"}
print(d[45])

# Traversing a dictionary
d = {45: "Rohit", 18: "Virat", 17: "ABD", 45: "Gayle", 17: "Rishabh"}
for i in d:  # returns the keys
    print(i, d[i])

random_dict = {
    "name": "Alex",
    "age": 25,
    "is_student": True,
    "skills": ["Python", "Data Analysis", "Machine Learning"],
    "grades": {"Math": 90, "Science": 85, "History": 88},
    "hobbies": ["reading", "gaming", "hiking"],
    "preferences": {
        "favorite_color": "blue",
        "likes_coffee": True,
        "preferred_os": "Linux",
    },
    "id": 1023,
    "is_active": False,
}

print(random_dict)

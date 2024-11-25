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

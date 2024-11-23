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
d = {"Rohit"}

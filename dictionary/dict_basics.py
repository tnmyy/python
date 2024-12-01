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

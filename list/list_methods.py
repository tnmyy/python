# LIST METHODS

# 1. len()
print("# 1. len()")
l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(len(l1))

# 2. list()
# returns a list formed from a sequential data type
print("# 2. list()")
print(list("This is a list"))  # from a string
print(list((1, 2, 3, 4)))  # from a tuple
print(list({"a": 1, "b": 2}))  # from keys of a dict

# 3. index()
print("# 3. index()")
l1 = ["This", "is", "a", "list"]
print(l1.index("is"))
# print(l1.index("i")) # Value error exception

# 4. append()
print("# 4. append()")
# adds and item to the END of the list
# does not returns new list
l1 = [1, 2, 3, 4]
l2 = l1.append(5)
print(l1)
print(
    l2
)  # no new list formed as append does not returns any value, it only updates the pre-existing list

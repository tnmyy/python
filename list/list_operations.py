# # LIST OPERATIONS
# # List Comparison (compares similar data types on the respective index)

# l1 = [1, 2, 3, 4]
# l2 = [1, 2, 3, 3.5]
# print(l1 < l2)  # compares on the basis of 3rd index

# l3 = [1, 2, 3, 4, 5, 6]
# l4 = [1, 2, 3, 5, 4, 6]
# print(l3 < l4)  # since 4 < 5

# l5 = ["a", "b"]
# l6 = ["a", "B"]
# print(l5 < l6)  # since ord(b) > ord(B)

# # l7 = [1, [2, 3]]
# # l8 = [1, 2, 3]
# # print(l7 < l8) # ERROR: Since not of comparable type

# # CONCATENATION (list + list OR list += iterable)
# l1 = [1, 2, 3, 4]
# l2 = [4, 5, 6]
# l3 = [7, 8, 9]
# print(l1 + l2 + l3)

# l1 += "abc"
# print(l1)

# # l2 += 2
# # print(l2) # since 2 is not an iterable

# l2 += [2]
# print(l2)

# # REPLICATION
# l1 = ["l", "i", "s", "t"]
# print(l1 * 4)

# MODIFYING LIST ELEMENTS
l = ["one", "two", "three"]
print(l)
l[0:2] = [1, 2]
print(l)

l = ["one", "two", "three"]
print(l)
l[0:2] = ["A"]
print(l)
# OR
l[0:2] = "A"
print(l)

# COPYING A LIST
a = [1, 2, 3]
b = a  # this is not a copy

b = list(a)
# OR
b = a.copy()
# OR
b = a[:]

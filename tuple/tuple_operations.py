# TUPLE OPERATIONS

# Joining tuples
t1 = (1, 2, 3)
t2 = (1, 4, 5, 6)
print(t1 + t2)

t1 = (1, 2, 3, 4)
# print(t1 + (3)) ERROR
print(t1 + (3,))

# Replicating tuples
t1 = (1, 2, 3, 4)
n = 3
print(t1 * n)

# Slicing
t1 = (1, 2, 3, 4, 5, 6, 7, 8, 9)
print(t1[::2])

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

# PACKING OF TUPLES
# creating a tuple from a set of values is called packing. therefore, creating individual elements from the tuple's elements is called unpacking

t = (1, 2, True, "Hey")
print(t)
a, b, c, d = t  # number of variables == number of elements
print(a, type(a))
print(b, type(b))
print(c, type(c))
print(d, type(d))

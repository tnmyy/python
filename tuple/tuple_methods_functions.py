# TUPLE METHODS AND FUNCTIONS

# 1. len()
print("# 1. len()")
t = (1, 2, 3, 4, 5, 6)
print(len(t))

# 2. max() # complete tuple must contain the elements of same data types
print("# 2. max()")
t = ("a", "B", "c")
print(max(t))

# 3. min() # complete tuple must contain the elements of same data types
print("# 3. min()")
t = ("a", "B", "c")
print(min(t))

# 4. sum()
print("# 4. sum()")
t = (23, 4, 56, 32, 413, 23, 43)
print(sum(t))

# 5. index()
print("# 5. index()")
t = (1, 2, 3, 4, 5)
print(t.index(4))

# 6. count()
print("# 6. count()")
t = (1, 4, 2, 2, 5, 6, 8, 2, 3, 4, 2, 33, 3, 3, 1, 2, 4)
print(t.count(2))

# 7. sorted(), can take any seq data type but always returns a sorted list
print("# 7. sorted()")
t = (5, 1, 4, 2, 3, 8, 3, 0, 4)
print(sorted(t, reverse=True))
print(sorted(t, reverse=False))
x = sorted(t)
print(x)

# 8. tuple()
print("# 8. tuple()")
a = tuple("python ".strip())
print(a)
a = tuple("python ")
print(a)


# INDIRECTLY MODIFYING TUPLES
print("# INDIRECTLY MODIFYING TUPLES")

# 1. using tuple unpacking
print("# 1. using tuple unpacking")
t = (1, 2, 3, 4)
a, b, c, d = t  # unpacking
print(t)
c = 0
t = (a, b, c, d)  # repacking
print(t)

# 2. using list() and tuple()
print("# 2. using list() and tuple()")
t = (1, 2, 3, 4)
print(t)
t = list(t)
t[3] = 0
t = tuple(t)
print(t)

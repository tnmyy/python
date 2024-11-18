# # TUPLE INTRODUCTION

# # Creating tuples
# t = (1, 2, 3, 4)
# print(t, type(t))

# # Empty tuple
# t = ()
# print(t)
# # or
# t = tuple()
# print(t)

# # single element tuple
# t = (1,)
# print(t)
# # OR
# # t = 2,
# # print(t)

# # long tuples
# t = (
#     1,
#     2,
#     3,
#     4,
# )
# print(t)
# # or
# # t = 1,2,3,4,
# # print(t)

# # nested tuple
# t = (1, 2, 3, (4, 5, 6))
# print(t)

# # mixed value tuple
# t = (True, False, 1, 2, 3.14, "pi", [12, 34])
# print(t)

# # MAKING TUPLE FROM EXISTING SEQUENTIAL DATA TYPE
# t = tuple("Hello")
# print(t)
# t = tuple([1, 2, 3, 4, 5, 6])
# print(t)

# # INPUTTING TUPLE
# it = tuple(input("Enter the tuple: "))
# # only beneficial for integers as typecasts string to tuple
# print(it, type(it))

# it = eval(input("Enter the tuple: "))
# print(it, type(it))

# THODI SI HARKATE
# immutables cannot be changed, but if there is any mutable inside an immutable; the individual elements of the mutable can be changed
t = ([1, 2, 3], [4, 5, 6])
print(t)
# t[0] = [1]
# print(t)
# It gives error

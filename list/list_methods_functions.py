# # LIST METHODS

# # 1. len()
# print("# 1. len()")
# l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(len(l1))

# # 2. list()
# # returns a list formed from a sequential data type
# print("# 2. list()")
# print(list("This is a list"))  # from a string
# print(list((1, 2, 3, 4)))  # from a tuple
# print(list({"a": 1, "b": 2}))  # from keys of a dict

# # 3. index()
# print("# 3. index()")
# l1 = ["This", "is", "a", "list"]
# print(l1.index("is"))
# # print(l1.index("i")) # Value error exception

# # 4. append()
# print("# 4. append()")
# # adds and item to the END of the list
# # does not returns any value
# l1 = [1, 2, 3, 4]
# l3 = [12.3, 543]
# l2 = l1.append(5)
# print(l1)
# l1.append(l3)
# print(l1)
# print(
#     l2
# )  # no new list formed as append does not returns any value, it only updates the pre-existing list

# # 5. extend()
# # extends a list by adding a LIST to end of a list
# # does not returns any value
# print("# 5. extend()")
# l1 = [1, 3, 4, 5]
# l2 = [7, 8, 9, 10]
# l1.extend(l2)
# print(l1)

# l1.extend([13, 14, 15])
# print(l1)

# # 6. insert(index, item)
# # index = index before you wanna insert the element
# # this allows us to add an item to the list at custom position
# print("# 6. insert()")
# l1 = [0, 1, 3, 4, 5, 6]
# l1.insert(2, 2)
# print(l1)

# l1.insert(-2, "A")
# print(l1)

# l1.insert(len(l1) + 10, "test")  # index >= len(<list>) => inserted at last
# print(l1)

# l1.insert(0 - len(l1) - 10, "test2")  # index <= -index ==> prepend as first element
# print(l1)

# # 7. pop(index)
# # used to remove an item from the list
# # pop() ==> last item removed
# # returns the removed element
# print("# 7. pop(index)")
# l = [1, 2, 3, 4, 5]
# l.pop(-5)
# print(l)

# l.insert(0, 1)
# l.pop()
# print(l)
# l.pop()
# print(l)

# # 8. remove(value)
# # removes the first occurrence of the value in the list
# # returns ValueError if the value is not in the list
# # does not returns any value
# print("# 8. remove(value)")
# l = [1, 2, 3, 2, 3, 4, 1, 3, 4, 5]
# print(l)
# l.remove(1)
# print(l)

# # 9. clear()
# # clears whole list by removing every element from it
# # returns empty list
# print("# 9. clear()")
# l = ["q", "w", "e", "r", "t", "y", "u", "i", "o", "p"]
# print(l)
# l.clear()
# print(l)

# # 10. count(value)
# # counts the occurrence of an item in a list
# print("# 10. count(value)")
# l = [1, 2, 3, 2, 3, 4, 1, 3, 4, 5]
# print(l.count(1))
# print(l.count(2))
# print(l.count(3))
# print(l.count(-3))

# 11. reverse()
# reverses the index of a list
# does not returns anything
print("# 11. reverse()")
l = list("aeiou")
print(l)
l.reverse()
print(l)

# 12. sort(reverse = True/False)
# does not create new list
# default = increasing order (False)
# cannot sort complex numbers
# can only sort comparable data types
print("# 12. sort()")
l = [1, 2, 3, 2, 3, 4, 1, 3, 4, 5]
print(l)
l.sort()
print(l)

l.sort(reverse=True)
print(l)

l.sort(reverse=False)
print(l)

l = list("acbdfgehilkj")
print(l)
l.sort()
print(l)

# 13. sorted() function
# returns a new sorted list irrespective of the iterable data type given to it
print("# 13. sorted() function")
l = [1, 2, 3, 2, 3, 4, 1, 3, 4, 5]
l2 = sorted(l)
print(l2)
l = [1, 2, 3, 2, 3, 4, 1, 3, 4, 5]
print(sorted("acbdfgehilkj", reverse=True))

# 14. min(), max(), sum() function
print("# 14. min(), max(), sum() function")
l = [1, 2, 3, 2, 3, 4, 1, 3, 4, 5]
print(min(l))
print(max(l))
print(sum(l))

# 15. del list[start:stop] OR [index] STATEMENT
print("# 15. del list[]")
l = [1, 2, 3, 2, 3, 4, 1, 3, 4, 5]
print(l)
del l[4]
print(l)
del l[:1]
print(l)

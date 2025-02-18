# REVISION


# # Looping Questions
# # 1. Write a program to print all the prime numbers between 1 and 100.
# primeNum = []
# for x in range(2, 101):
#     primeNum.append(x)
#     for y in range(2, x):
#         if x % y == 0:
#             if x in primeNum:
#                 primeNum.remove(x)
# print(primeNum)

# # Using a while loop, print the Fibonacci series up to 10 terms.
# a = 0
# b = 1
# n = 10
# i = 0
# fibo = [a, b]
# while i < n:
#     c = b + a
#     fibo.append(c)
#     a = b
#     b = c
#     i += 1
# print(fibo)

# # Write a program to find the sum of all multiples of 3 or 5 below 50.
# total = 0
# for x in range(50):
#     if x % 3 == 0 or x % 5 == 0:
#         total += x
# print("Sum:", total)

# # Use a for loop to print the reverse of a number entered by the user.
# num = 1923
# num2 = num
# rev = []
# for x in range(len(str(num))):
#     a = num2 % 10
#     num2 = num2 // 10
#     rev.append(a)
# print(rev)


# # Write a program that prints a pyramid pattern like this:
# #  ...*
# #    ***
# #   *****
# #  *******
# n = 4
# for x in range(n):
#     for y in range(n - (x + 1)):
#         print(" ", end="")
#     for z in range(1 + x):
#         print("*", end="")
#     for b in range(x):
#         print("*", end="")

#     print()

#! Strings Questions
# # Write a program to check if a given string is a palindrome.
# s = "naman"
# s = s.lower()
# rev = s[::-1]
# if s == rev:
#     print("Palindrome!")
# else:
#     print("Nah!")

# # Count the number of vowels and consonants in a string entered by the user.
# s = "this is the string entered by the user"
# vow = "aeiou"
# vCount = 0
# cCount = 0

# s = s.lower()
# for x in s:
#     if x.isalpha():
#         if x in vow:
#             vCount += 1
#         else:
#             cCount += 1

# # Take a string input and reverse every word in the string while maintaining their positions.
# # Input: "Hello Python Programming"
# # Output: "olleH nohtyP gnimmargorP"
# s = "Hello Python Programming"
# s = s.split()
# rev = []
# reverse = ""
# for x in s:
#     revWord = x[::-1]
#     rev.append(revWord)
# for y in rev:
#     reverse += y + " "
# print(reverse)

# # Write a program to check if two strings are anagrams of each other.
# s1 = "Dormitory"
# s2 = "Dirty room"
# s1 = s1.replace(" ", "").lower()
# s2 = s2.replace(" ", "").lower()

# if len(s1) == len(s2):
#     w1 = []
#     for i in s1:
#         w1.append(i)
#     w2 = []
#     for i in s2:
#         w2.append(i)
#     w1.sort()
#     w2.sort()
# if w1 == w2:
#     print("Both the strings are anagrams")
# else:
#     print("Both the strings are NOT anagrams")

# # Replace all spaces in a string with - without using the replace method.
# s = "this is a string"
# space = " "
# newS = ""
# for i in s:
#     if i == space:
#         newS += "-"
#     else:
#         newS += i

# print(newS)

#!Lists Questions
# # Write a program to find the largest and smallest elements in a list.
# l = [1, 3, 4, 5, 5, 6, 6, 2, 44, 1, 3, 4, 134, 21]
# print("Min: ", min(l))
# print("Max: ", max(l))

# # Create a list of integers and print the sum of its elements using a for loop.
# l = [1, 3, 4, 5, 5, 6, 6, 2, 44, 1, 3, 4, 134, 21]
# total = 0
# for x in l:
#     total += x
# print("Sum: ", total)

# # Write a program to remove all duplicates from a list.
# l = [1, 3, 4, 5, 5, 6, 6, 2, 4, 4, 1, 3, 4, 1, 3, 4, 2, 1]
# newL = []
# for x in l:
#     if x not in newL:
#         newL.append(x)
# print(newL)

# # Rotate a list to the right by 3 positions.
# # Input: [1, 2, 3, 4, 5]
# # Output: [3, 4, 5, 1, 2]
# l = [1, 2, 3, 4, 5]
# newL = []
# for i in range(len(l)):
#     newL.append(l[i - 3])
# print(newL)

#! Tuples Questions
# # Write a program to convert a list of tuples into a list of strings.
# # Input: [(1, 2), (3, 4)]
# # Output: ['12', '34']
# l = [(1, 2), (3, 4)]
# new_lis = []
# elem_str = ""
# for tup in l:
#     elem_str = ""
#     for elem in tup:
#         elem_str += str(elem)
#     new_lis.append(elem_str)
# print(new_lis)

# # Find the index of the first occurrence of a user-provided value in a tuple.
# tup = (1, 2, 3, 4, 5, 1, 2, 3, 1, 3, 1, 2, 3, 4, 5, 6)
# val = 3
# if val in tup:
#     print("The first index of:", val, "is", tup.index(val))
# else:
#     print('The given value does not exists in the tuple')

# # Write a program to check if a tuple contains duplicate elements.
# tup = (1, 2, 3, 4, 5, 1, 2, 3, 1, 3, 1, 2, 3, 4, 5, 6)
# new_lis = []
# dup_lis = []
# for x in tup:
#     if x not in new_lis:
#         new_lis.append(x)
#     else:
#         dup_lis.append(x)
# if len(tup) > len(new_lis):
#     print("The tuple contains duplicate elements", dup_lis)

# # Convert a tuple of integers to a single integer.
# # Input: (1, 2, 3)
# # Output: 123
# tup = (1, 2, 3, 4, 5, 1, 2, 3, 1, 3, 1, 2, 3, 4, 5, 6)
# new_str = ""
# for elem in tup:
#     new_str += str(elem)
# print("single integer:", int(new_str))

# # Write a program to merge two tuples and sort the resulting tuple.
# tup1 = (1, 2, 3, 4, 5, 1, 2, 3, 1, 3, 1, 2, 3, 4, 5, 6)
# tup2 = (3, 4, 5, 1, 2)
# new_lis = list(tup1) + list(tup2)
# sorted_lis = sorted(new_lis)
# print("Sorted tuple:", tuple(sorted_lis))

#! Combined Topics
# # Take a list of numbers as input and create a tuple containing only the odd numbers from the list.
# lis = [1, 1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6]
# odd_lis = []
# for i in lis:
#     if i % 2 != 0:
#         odd_lis.append(i)
# print(odd_lis)

# # Write a program to count how many times each word appears in a string (store results in a list of tuples).
# string = "this is a string which I am going to use"
# unique_char = []
# for x in string:
#     if x not in unique_char:
#         unique_char.append(x)

# occurrence = []
# for i in unique_char:
#     occurrence.append(string.count(i))

# combined = []
# for j in range(len(unique_char)):
#     tup = tuple()
#     tup = (unique_char[j], occurrence[j])
#     combined.append(tup)
# print(combined)


# # Take a string as input and create a list of all unique characters in the string.
# s = "this is the string which going to be used"
# uni_lis = []
# for i in s:
#     if i not in uni_lis:
#         uni_lis.append(i)
# print(uni_lis)


# # Write a program to reverse all elements in a list of strings.
# # Input: ['python', 'is', 'fun']
# # Output: ['nohtyp', 'si', 'nuf']
# l = ["python", "is", "fun"]
# nL = []
# for i in l:
#     n = i[::-1]
#     nL.append(n)
# print(nL)

# Sorts the list by marks in descending order and prints the result.
# Example Input: [('Alice', 85), ('Bob', 70), ('Charlie', 95)]
# Example Output: [('Charlie', 95), ('Alice', 85), ('Bob', 70)]

##! Tricky Combined Questions
# # Write a program to check if a string can be rearranged to form a palindrome. Use lists and tuples if needed for intermediate processing.
# s = "nnmaafdafadsfads"
# s = s.lower()
# d = {}
# for char in s:
#     elem = char
#     if elem not in d:
#         d[elem] = s.count(elem)
# count = 0
# for i in d.values():
#     if i % 2 != 0:
#         count += 1
#     if count >= 2:
#         break
# if count == 2:
#     print("A palindrome cannot be formed")
# else:
#     print("A palindrome can be formed")


# # Create a function that:
# # Accepts a list of integers.
# # Returns a tuple with the maximum, minimum, and average of the list.


# def lis_fun(lis):
#     if type(lis) == type([]):
#         mx = max(lis)
#         mn = min(lis)
#         avg = sum(lis)
#         tup = (mx, mn, avg)
#     print(tup)


# lis_fun([1, 2, 3, 5, 6, 4, 12, 2, 8])


# # Create a program that converts a string into a list of tuples, where each tuple contains a character and its frequency.
# # Input: "banana"
# # Output: [('b', 1), ('a', 3), ('n', 2)]
# s = "banana"
# d = {}
# lis = []
# for i in s:
#     elem = i
#     if elem not in d:
#         d[elem] = s.count(elem)
# for x in d:
#     lis += [(x, d[x])]
# print(lis)

# # Take a string input, create a list of words, and check if all the words are palindromes.
# s = "This is the string"
# s = s.split()
# pali = False
# for i in s:
#     if i == i[::-1]:
#         pali = True
#     else:
#         pali = False
#         break
# if pali:
#     print("Yes all the words are palindromes")
# else:
#     print("Not all words are palindrome")

# Write a program to merge two lists into a list of tuples (pairing elements by their index) and then sort them by the second element of each tuple.
l1 = "this is the first list".split()
l2 = "2 3 4 1 5".split()
index_of_l2 = []
combined = []
if len(l1) == len(l2):
    l2_ = sorted(l2)
    for x in l2_:
        index_of_l2 += [l2.index(x)]

    for i in index_of_l2:
        combined.append((l1[i], l2[i]))
print(combined)

# # 1. WAPP to print the elements of a list along with their positive and negative indexes

# l = ["q", "w", "e", "r", "t", "y"]
# for i in range(len(l)):
#     print(l[i], i, i - len(l))

# # 2. WAPP which extracts two list slices out of a given list of numbers. Display and print the sum of elements of first list-slice which contains every other element of the list between indexes 5 to 15. Program should also display the average of elements in second list slice that contains every fourth element of the list. The given list contains elements form 1 to 20.

# lis = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

# lis1 = lis[5:15:2]
# lis2 = lis[::4]
# sum1 = 0
# avg = 0
# for i in lis1:
#     sum1 += i
# for j in lis2:
#     avg += j
# avg /= len(lis2)

# print(f"slice 1: {lis1}\nSum: {sum1}\nSlice 2: {lis2}\nAverage: {avg}")

# # 3. WAPP to create a copy of a list. In the list's copy, add 10 to its first and last elements. Then display the lists
# l1 = [11, 2, 3, 5, 1, 212, 20, 35, 63, 45, 20, 36]
# l2 = l1.copy()

# l2[0] += 10
# l2[-1] += 10

# print(l2)

# # 4. WAPP the inputs a list, replicates it twice and then prints the sorted list in ascending and descending orders

# n = int(input("Enter the number of elements you want in the list: "))
# i = 0
# lis = []
# while i < n:
#     elem = int(input("Enter the integral list elements: "))
#     lis.append(elem)
#     i += 1

# lis1 = lis.copy()
# lis1.sort()
# lis2 = lis.copy()
# lis1.sort(reverse=True)

# print(lis1)
# print(lis2)

# # 5. WAPP to find the minimum element from a list of numbers and also print it's index
# elem = eval(input("Enter a list of numbers: "))

# if type(elem) == type([]):
#     minimum = min(elem)
#     ind = elem.index(minimum)
#     print("List: ", elem)
#     print("Minimum element is: ", minimum, "it's index is: ", ind)
# else:
#     print("Enter a valid list!")

# # 6. WAPP to calculate the mean of a given list of numbers
# lis = [11, 2, 3, 5, 1, 212, 20, 35, 63, 45, 20, 36]
# avg = sum(lis) / len(lis)
# print("Average of list: ", lis, "is: ", avg)

# # 7. WAPP to search for an element in a given list
# lis = eval(input("Enter your list: "))
# search = eval(input("Enter what do you want to search: "))
# ind = -1
# if type(lis) == type([]):
#     for i in lis:
#         if i == search:
#             ind = lis.index(i)

# else:
#     print("Enter a valid list please!!")
# if ind >= 0:
#     print(search, "is found at", ind, "index")
# else:
#     print("Cannot find", search, "in", lis)

# # 8. WAPP to count the frequency of a given element in a list
# lis = eval(input("Enter a list: "))
# elem = eval(input("Enter the element to be searched: "))
# count = 0
# if type(lis) == type([]):
#     for i in lis:
#         if i == elem:
#             count += 1
# else:
#     print("Enter a valid list! ")

# if count > 0:
#     print(elem, "occurred", count, "times in the list: ", lis)
# else:
#     print("Cannot find", elem, "in", lis)

# # 9. WAPP to check whether the numerically maximum element lies either in the first half or in the second half or in the middle of the list
# lis = [0, 1, 1, 7, 2, 3, 1, 2]
# len_lis = len(lis) / 2
# max_elem = max(lis)
# ind_max = lis.index(max_elem)

# if type(len_lis) == type(1):
#     if ind_max < len_lis:
#         print("First Half")
#     elif ind_max >= len_lis:
#         print("Second Half")
# else:
#     len_lis = (len(lis) - 1) / 2
#     if ind_max < len_lis:
#         print("First Half")
#     elif ind_max > len_lis:
#         print("Second Half")
#     else:
#         print("Middle")

# # 10. WAPP that displays the maximum elements along with it's index and the list from which it is
# l1 = [1, 2, 3, 1, 2, 2, 2, 9, 4]
# l2 = [6, 7, 8, 9]
# max_l1 = max(l1)
# i_max_l1 = l1.index(max_l1)
# max_l2 = max(l2)
# i_max_l2 = l2.index(max_l2)

# if max_l1 > max_l2:
#     max_elem = max_l1
#     print(f"The maximum element is from the list {l1} and its index is {i_max_l1}")
# elif max_l2 > max_l1:
#     max_elem = max_l2
#     print(f"The maximum element is from the list {l2} and its index is {i_max_l2}")
# else:
#     print(
#         f"The maximum element is common in both the lists.\nIt's index in {l1} is {i_max_l1}\nand it's index in {l2} is {i_max_l2}"
#     )

# # 11. WAPP to swap the even and odd elements of a list with each other
# lis = [1, 2, 3, 4, 5, 6]
# n_lis = []
# for i in range(0, len(lis), 2):
#     temp_lis = [lis[i + 1], lis[i]]
#     n_lis.extend(temp_lis)
# print(n_lis)

# # 12. WAPP to print the frequencies of all the elements in a list and then print the unique and duplicate elements of the list as a list
# lis = [1, 2, 3, 12, 2]
# uni_lis = []
# dup_lis = []

# parsed_elem = []
# for x in lis:
#     count = lis.count(x)
#     if x not in parsed_elem:
#         print("Frequency of", x, "is", count)
#         parsed_elem.append(x)

#     if count > 1 and x not in dup_lis:
#         dup_lis.append(x)
#     else:
#         uni_lis.append(x)
# print("Duplicate elements: ", dup_lis)
# print("Unique elements: ", uni_lis)
# # lis_copy = lis.copy()
# # lis_copy = lis
# # for x in lis_copy:
# #     if lis_copy.count(x) > 1 and x not in dup_lis:
# #         dup_lis.append(x)
# #     elif lis_copy.count(x) == 1:
# #         uni_lis.append(x)
# # print("Duplicate elements: ", dup_lis)
# # print("Unique elements: ", uni_lis)

# # 13. WAPP to test if a number in a list is equal to the sum of the cubes of its digits. Find the smallest and largest such number from the given list of numbers
# lis = [153, 407, 456, 508, 342, 3413, 370, 9878]
# cub_lis = []

# for i in lis:
#     num = str(i)
#     total = 0
#     for j in num:
#         j = int(j)
#         total += j**3
#     if total == i:
#         cub_lis.append(i)
# print(cub_lis)
# print("Max num:", max(cub_lis))
# print("Min num:", min(cub_lis))

# # 14. WAPP to find the second largest number of a list of numbers
# lis = [153, 407, 456, 508, 342, 3413, 370, 9878]
# first_max = max(lis)
# lis.remove(first_max)
# second_max = max(lis)
# print("The second largest number in:", lis.append(first_max), "is", second_max)

# 15. WAPP to remove all the occurrence of an element in a list
lis = [1, 2, 3, 4, 5, 6, 2, 3, 4, 2, 4, 3, 2]
i = 0
rem = 2
print("Before", lis)
x = lis.count(rem)
while i < x:
    lis.remove(rem)
    i += 1
print("After", lis)

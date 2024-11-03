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


# 9. WAPP to check whether the numerically maximum element lies either in the first half or in the second half or in the middle of the list
lis = [0, 1, 1, 7, 2, 3, 1, 2]
len_lis = len(lis) / 2
max_elem = max(lis)
ind_max = lis.index(max_elem)

if type(len_lis) == type(1):
    if ind_max < len_lis:
        print("First Half")
    elif ind_max >= len_lis:
        print("Second Half")
else:
    len_lis = (len(lis) - 1) / 2
    if ind_max < len_lis:
        print("First Half")
    elif ind_max > len_lis:
        print("Second Half")
    else:
        print("Middle")


"""# # 9. WAPP to print the frequencies of all the elements in a list and then print the unique and duplicate elements of the list as a list
# lis = [1, 2, 3, 1, 2, 4]
# lis_copy = lis
# uni_lis = []
# dup_lis = []

# for i in range(len(lis_copy)):
#     for j in range(len(lis_copy)):
#         if lis_copy[j] == lis_copy[i]:
#             print(f"{lis_copy[i]},{lis_copy[j]}, {i},{j}")
"""

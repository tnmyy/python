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

# 3. WAPP to create a copy of a list. In the list's copy, add 10 to its first and last elements. Then display the lists
l1 = [11, 2, 3, 5, 1, 212, 20, 35, 63, 45, 20, 36]
l2 = l1.copy()

l2[0] += 10
l2[-1] += 10

print(l2)

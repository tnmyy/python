# # 1. WAPP to result the second largest element from a tuple
# t = (1, 34, 123, 12, 455, 23, 413, 513, 34, 313, 433, 234)
# s = sorted(t)
# print("Second largest element is: ", s[-2])

# # 2. WAPP to find whether there are multiple maximum elements in a tuple or not
# t = (1, 34, 123, 12, 455, 23, 413, 513, 34, 313, 433, 234, 312, 513, 312)
# if t.count(max(t)) > 1:
#     print(
#         "The maximum element:", max(t), "occurs", t.count(max(t)), "times in the tuple"
#     )

# # 3. WAP to check whether a tuple contains duplicate elements
# t = (1, 2, 3, 4, 5, 5, 3, 2, 2, 1)
# for i in t:
#     if t.count(i) > 1:
#         print("Duplicate elements")
#         break
#     else:
#         print("All unique")

# 4. WAP to check whether the minimum element of the tuples lies in the middle position of tuple

t = (6, 7, 8, 5, 8, 9, 10)
mn = min(t)
if t.count(mn) > 1:
    print("There is no single minimum element, hence position cannot be determined")
else:
    ind = t.index(mn)
    ln = len(t)
    if ln % 2 == 0:
        if (ind == ln / 2) or (ind == ln / 2 + 1):
            print("Yess it lies in the middle")
        else:
            print("NOOOO!")
    else:
        if ind == ln // 2:
            print("Yess it lies in the middle")
        else:
            print("NOOOO!")

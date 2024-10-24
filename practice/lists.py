# 1. WAPP to print the elements of a list along with their positive and negative indexes

l = ["q", "w", "e", "r", "t", "y"]
for i in range(len(l)):
    print(l[i], i, i - len(l))

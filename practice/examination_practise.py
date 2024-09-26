# print("Examination Practice")

# # 1.
# n = 10
# total = 0
# for x in range(1, n, 2):
#     total += x
# print(total)
# # 2.
# i = 0
# while i <= 10:
#     n1 = float(input("Num 1: "))
#     n2 = float(input("Num 2: "))
#     n3 = float(input("Num 3: "))

#     largest = smallest = None

#     if n1 == n2 == n3:
#         print("all are equal")
#     else:
#         if n1 > n2 and n1 > n3:
#             largest = n1
#             if n2 > n3:
#                 smallest = n3
#             else:
#                 smallest = n2
#         elif n2 > n1 and n2 > n3:
#             largest = n2
#             if n1 > n3:
#                 smallest = n3
#             else:
#                 smallest = n1
#         else:
#             largest = n3
#             if n1 > n2:
#                 smallest = n2
#             else:
#                 smallest = n1

#     i += 1
#     print(largest, smallest)

# # 3.
# n = 123456
# num = n
# while True:
#     digit = num % 100
#     num = num // 100
#     print(digit, end="")
#     if num == 0:
#         break

# # 4.
# small = smallest = 0
# for x in range(10):
#     n = float(input("Enter your number: "))

#     if x == 0:
#         small = n
#     elif x == 1:
#         if small < n:
#             smallest = small
#             small = n
#         else:
#             smallest = n
#     else:
#         if n < smallest:
#             small = smallest
#             smallest = n
#         elif n < small:
#             small = n
# print("smallest: ", smallest)
# print("small: ", small)

# # 5.
# first = 0
# second = 1
# n = 10
# i = 0
# print(first, ",", second, end=", ")
# while i < 10:
#     nxt = first + second
#     print(nxt, end=", 1")
#     first = second
#     second = nxt
#     i += 1

# # 6.
# n = int(input("Enter a number: "))
# if n < 1000:
#     print("Enter a valid number")
# else:
#     num = n
#     while num != 0:
#         digit = num % 10
#         num = num // 10
#         print(digit, end="")

# # 7.
# n = 100
# i = 1
# while i <= n:
#     if n % i == 0:
#         print(i, end="` ")
#     i += 1

# # 8
# n = int(input("Enter the number for double factorial: "))
# fct = 1
# if n % 2 == 0:
#     print("even number")
#     for x in range(2, n + 1, 2):
#         fct *= x
# else:
#     print("odd number")
#     for x in range(1, n + 1, 2):
#         fct *= x
# print(fct)

# # 9 MERSENNE numbers
# n = int(input("Enter the number of terms: "))
# for x in range(1, n + 1):
#     num = 2**x - 1
#     print(num, end=" ")

# # 10
# n = 5
# for x in range(1, n + 1):
#     for y in range(1, 2 * x, 2):
#         print(y, end=" ")
#     print()

# # 11 MERSENNE numbers
# # n = int(input('Enter the number of terms: '))
# n = 10
# for x in range(1, n + 1):
#     num = 2**x - 1
#     count = 0
#     for y in range(1, num):
#         if num % y == 0:
#             count += 1

#     if count != 1:
#         print(num)
#     else:
#         print(num, "prime")

# # 12 PERFECT NUMBER
# # n = 28
# for n in range(1, 1000):
#     s = 0
#     for x in range(1, n):
#         if n % x == 0:
#             s += x
#     if s == n:
#         print(n, "Perfect number")

# # 13 LCM HCF
# a = int(input("Enter a: "))
# b = int(input("Enter b: "))
# if a > b:
#     smaller = b
# else:
#     smaller = a

# for x in range(1, smaller + 1):
#     if (a % x == 0) and (b % x == 0):
#         hcf = x
# lcm = int((a * b) / hcf)

# print(f"LCM and HCF of {a} and {b} are: {lcm} and {hcf}")

# # 14
# n = 10
# total = 0
# for x in range(1, n + 1):
#     for y in range(1, x + 1):
#         total += y
# print(total)

# 15
# #      *
# #     * *
# #    * * *
# #   * * * *
# #  * * * * *
# n = 5
# for x in range(n):
#     for y in range(x + 1, n):
#         print(" ", end=" ")
#     for z in range(0, x + 1):
#         print("*", end=" ")
#     for a in range(0, x):
#         print("*", end=" ")

#     print()

# # 16
# #     *
# #   * * *
# # * * * * *
# #   * * *
# #     *
# n = 4
# k = round(n / 2) + 1
# for x in range(k):
#     for y in range(x, k - 1):
#         print(" ", end=" ")
#     for z in range(0, x + 1):
#         print("*", end=" ")
#     for a in range(x):
#         print("*", end=" ")

#     print()
# # LOWER PART
# i = n - k
# for x in range(i):
#     for y in range(0, x + 1):
#         print(" ", end=" ")
#     for z in range(x, 2):
#         print("*", end=" ")
#     for a in range(x, 1):
#         print("*", end=" ")
#     print()

a = 15
b = 18
small = None
if a < b:
    small = a
else:
    small = b
hcf = 1
for x in range(1, small + 1):
    if a % small == 0 and b % small == 0:
        hcf = x
lcm = (a * b) / hcf
print(lcm, hcf)

if (3 > 2) > 1:
    print("True")
else:
    print("False")

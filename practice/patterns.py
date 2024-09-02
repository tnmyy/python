# PATTERN 1
# 1 
# 2 2
# 3 3 3
# 4 4 4 4
# 5 5 5 5 5

print('# PATTERN 1')

n = 5
for row in range(1, n+1):
    for col in range(1, row+1):
        print(row, end=' ')
    print()

print()

# PATTERN 2
# 1
# 1 2
# 1 2 3
# 1 2 3 4 
# 1 2 3 4 5

print('# PATTERN 2')

n = 5
for row in range(1, n+1):
    for col in range(1, row+1):
        print(col, end=' ')
    print()

print()

# PATTERN 3
# 1
# 1 3
# 1 3 5
# 1 3 5 7 
# 1 3 5 7 9

print('# PATTERN 3')

n = 5
for row in range(1, n+1):
    for col in range(1, row+1):
        p = 2*col - 1
        print(p, end=' ')
    print()

print()

# PATTERN 4
# 1
# 2 3
# 4 5 6
# 7 8 9 10
# 11 12 13 14 15

print('# PATTERN 4')

n = 5
i = 1
for row in range(1, n+1):
    for col in range(1, row+1):
        print(i, end=' ')
        i += 1
    print()

print()

# TRIANGULAR PATTERNS

# PATTERN 5
# *
# * * 
# * * *
# * * * *
# * * * * *
print('# PATTERN 5')
n = 5
for row in range(n):
    for col in range(row+1):
        print('*', end=' ')
    print()

print()

# PATTERN 6
# * * * * *
# * * * *
# * * *
# * *
# *

print('# PATTERN 6')
n = 5
for row in range(n):
    for col in range(row, 5):
        print('*', end=' ')
    print()

print()

# PATTERN 7
# * * * * *
#   * * * *
#     * * *
#       * *
#         *
print('# PATTERN 7')
n = 5
for row in range(n):
    for emp in range(row):
        print(' ', end=' ')
    for col in range(row, 5):
        print('*', end=' ')
    print()

print()

# PATTERN 8

print('# PATTERN 8')
n = 5
for row in range(n):
    for emp in range(row, 4):
        print(' ', end=' ')
    for col in range(row+1):
        print('*', end=' ')
    print()

print()
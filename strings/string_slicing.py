# String Slicing
print('# String Slicing')

# 1. String indexing in python
print('# 1. String indexing in python')

# 1.1 Positive indexing
print('# 1.1 Positive indexing')

a = 'python'
print(a[0])

# printing the characters of string a via for loop
for x in range(0, 6):
    print(a[x])

# 1.2 Negative indexing
print('# 1.2 Negative indexing')

a = 'python'
print(a[-1])
print(a[-2])
print(a[-3])
print(a[-4])
print(a[-5])
print(a[-6])

# 2. String Slicing
print('# 2. String Slicing')

# string[n:m]
# slicing starts from 'n', 'n+1', 'n+2', .... till 'm-1'
a = 'amazing'
print(a[0])
print(a[1])
print(a[2])
print(a[3])
print(a[4])
print(a[5])
print(a[6])

print(a[0:7])
print(a[0:3])
print(a[2:5])
print(a[-7:-3])
print(a[-5:-1])
# missing index slicing
print('# missing index slicing')
print(a[:5])
print(a[3:])
# getting the original string "str = str[:n] + str[n:]"
print('# getting the original string')
print(a[:4]+a[4:])

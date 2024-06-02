#STRINGS IN PYTHON

# 1. Traversing a string
# Iterating through elements of a string (character by character)
print('# 1. Traversing a string')
name = 'python'
for x in name:
    print(x, '-', end=' ')
print()

# 2. String Operators
print('\n# 2. String Operators')
# 2.1 Basic Operators
print('# 2.1 Basic Operators')
# 2.1.1 Concatenation operator (+)
print('# 2.1.1 Concatenation operator (+)')

a, b= 'tea', 'pot'
print(a+b)

a, b = '1', '1'
print(a+b)

a, b = 'a', '0'
print(a+b)

a, b = '3', 'xyz'
print(a+b)

# NOTE: Addition != Concatenation
# ERROR-
##a, b = '1', 3
##print(a+b)

# 2.1.1 Replication operator (*)
print('# 2.1.1 Replication operator (*)')

a, b = 'hey', 10
print(a*b)

a, b = '2', 3
print(a*b)

a, b = 10, 'hey'
print(a*b)

a, b = 3, '2'
print(a*b)

# ERROR-
##a, b = '1', '3'
##print(a*b)
# NOTE: Multiplication != Replication

# 2.2 Membership Operators
print('\n# 2.2 Membership Operators')
# 2.2.1 'in' operator
# Returns true if a character/substring exists in the given string; otherwise false
# SYNTAX: <string> in <string>
print('# 2.2.1 \'in\' operator')

print('12' in '1029572213312')
print('an' in 'Tanmay')
print('ta' in 'Tanmay')
s1 = 'help'
s2 = 'helping hand'
print(s1 in s2)
#ERROR:
#print(12 in '123')

# 2.2.2 'not in' operator
print('# 2.2.2 \'not in\' operator')
# Returns true if a character/substring does not exists in the given string; otherwise false
# SYNTAX: <string> not in <string>
print('12' not in '1029572213312')
print('an' not in 'Tanmay')
print('ta' not in 'Tanmay')

# 2.3 Comparison Operators
print('\n# 2.3 Comparison Operators')

# 2.3.1 Equality and Non-Equality (==, !=)
print('# 2.3.1 Equality and Non-Equality (==, !=)')

print('a' == 'a')
print('A' == 'a')
print('Abc' == 'abc') # Letter case is different
print('a' != 'a')
print('A' != 'a')
print('Abc' != 'abc')

# 2.3.2 Comparison (<, >, >=, <=)
print('# 2.3.2 Comparison (<, >, >=, <=)')
# Comparing strings is done by comparing the "ORDINAL VALUES" (ASCII/Unicode values [for most of the common characters, these two values are same)]
print('a' < 'A')
print('a' > 'A')
print('ABC' > 'AB')
print('abc' <= 'ABCD')

# Determining Ordinal Value of a character
print('# Determining Ordinal Value of a character')
print(ord('a'))
print(ord('A'))
print(ord('1'))

# Converting Oridinal Value to Character
print('# Converting Oridinal Value to Character')
print(chr(97))
print(chr(65))
print(chr(49))

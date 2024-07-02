# STRING FUNCTIONS AND METHODS
print('# STRING FUNCTIONS AND METHODS')

# 1. len() function
# returns the length of a strings
print('# 1. len() function')
a = 'Tanmay upreti'
print(len(a))
print(len('Python is an impressive language'))

# 2. capitalize() method
# capitalizes the first character of a string
print('# 2. capitalize() method')
a = 'python'
print(a.capitalize())
print('i love my india'.capitalize())

# 3. count() method
# returns the number of times a specified value appears in a string
# SYNTAX: string.count(sub_str, start_index, end_index)
print('# 3. count() method')
a = 'Waake up a to a reality'
print(a.count('a'))
print(a[:3])
print(a.count('a', 0, 3))
print(a.count('a', 3)) # returns the occurance of 'a' after the 3rd index

# 4. find() method
# returns the lowest index, where the sub string searched is found
# returns '-1' if the sub string searched is not found
# SYNTAX: string.find(sub_str, start_index, end_index) 
print('# 4. find() method')
a = 'twinkle twinkle little star'
b = 'little'
print(a.find(b))
b = 'little  '
print(a.find(b))

# 5. index() method
# returns the lowest index, where the sub string searched is found (same as find())
# throws error when the searched substring is not found
# SYNTAX: string.index(sub_str, start_index, end_index) 
print('# 5. index() method')
a = 'twinkle twinkle little star'
b = 'little'
print(a.index(b))
b = 'little  '
# print(a.index(b)) it thows error



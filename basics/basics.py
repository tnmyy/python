# Checks the version of python in the code editor
import sys
print(sys.version)
print('Hello World')

# Indentation
if 5 > 3:
	print('5 is greater than 3')

# Comments
# This is a single line comment

# This is
# a multi line
# comment

'''
This is also
a multi line
comment
'''

"""
This is also
a multi line
comment
"""

# Variables

a = 10 #integer
b = 'Namaste Duniya!!!' #string

print(a)
print(b)

# Casting - to specify the data type of the variable
x = str(10)		#'3'
y = int(10) 	#10
z = float(10)	#10.0
print(x,y,z, sep=", ")

print(f'Data type of {x}: {type(x)}')
print(f'Data type of {y}: {type(y)}')
print(f'Data type of {z}: {type(z)}')
#The f-string formatting method is used to directly insert the variable values and their data types into the print statements.

X = str(93)		#'3'
Y = int(18) 	#10
Z = float(45)	#10.0
print(X,Y,Z, sep=", ")
print(f'Data type of {X}: {type(X)}')
print(f'Data type of {Y}: {type(Y)}')
print(f'Data type of {Z}: {type(Z)}')

thisIsVariableInCamelCase = 77
ThisIsVariableInPascelCase = 77
this_is_variable_in_snake_case = 77

# Assign Multiple Values

a,b,c = 'AAP','BJP','CONGRESS'
print(a)
print(b)
print(c)

# One Value to Multiple Variables

a=b=c= "Political Parties"
print(a)
print(b)
print(c)

# Unpack a Collection 
# is list mai 3 indexes tak values hai. x,y,z variables ko 0,1,2 indexes ki values milegi

political_parties = ["AAP","BJP","CONGRESS"]
print(political_parties)
x,y,z = political_parties
print(x)
print(y)
print(z)

# DATA TYPES
data = 'Namaste Duniya!!'
print(f'The data type of "{data}" is: {type(data)}')

data = 20
print(f'The data type of "{data}" is: {type(data)}')

data = 20.1
print(f'The data type of "{data}" is: {type(data)}')

data = 10j
print(f'The data type of "{data}" is: {type(data)}')

data = ['a','b','c']
print(f'The data type of "{data}" is: {type(data)}')

data = ('a','b','c')
print(f'The data type of "{data}" is: {type(data)}')

data = range(6)
print(f'The data type of "{data}" is: {type(data)}')

data = {"name":"Tanmay", "age":15}
print(f'The data type of "{data}" is: {type(data)}')

data = {'a','b','c'}
print(f'The data type of "{data}" is: {type(data)}')

data = frozenset({'a','b','c'})
print(f'The data type of "{data}" is: {type(data)}')

data = True
print(f'The data type of "{data}" is: {type(data)}')

data = b"Hello"
print(f'The data type of "{data}" is: {type(data)}')

data = bytearray(10)
print(f'The data type of "{data}" is: {type(data)}')

data = None
print(f'The data type of "{data}" is: {type(data)}')

data = memoryview(bytes(10))
print(f'The data type of "{data}" is: {type(data)}')

# Setting Own data type

data = str('Namaste Duniya!!')
print(f'The data type of "{data}" is: {type(data)}')

data = int(20)
print(f'The data type of "{data}" is: {type(data)}')

data = float(20.1)
print(f'The data type of "{data}" is: {type(data)}')

data = complex(10j)
print(f'The data type of "{data}" is: {type(data)}')

data = list(['a','b','c'])
print(f'The data type of "{data}" is: {type(data)}')

data = tuple(('a','b','c'))
print(f'The data type of "{data}" is: {type(data)}')

data = range(6)
print(f'The data type of "{data}" is: {type(data)}')

data = dict({"name":"Tanmay", "age":15})
print(f'The data type of "{data}" is: {type(data)}')

data = set({'a','b','c'})
print(f'The data type of "{data}" is: {type(data)}')

data = frozenset(frozenset({'a','b','c'}))
print(f'The data type of "{data}" is: {type(data)}')

data = bool(True)
print(f'The data type of "{data}" is: {type(data)}')

data = bytes(b"Hello")
print(f'The data type of "{data}" is: {type(data)}')

data = bytearray(bytearray(10))
print(f'The data type of "{data}" is: {type(data)}')


data = memoryview(memoryview(bytes(10)))
print(f'The data type of "{data}" is: {type(data)}')

# Importing Random number

import random
print(random.randrange(1,10))
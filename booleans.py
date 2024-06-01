print('Booleans in Python')

print(10==9)
print(10>9)
print(10>=10)

a = 100
b=10

if(a>b):
	print('a is greater than b')
else:
	print('a is not greater than b')

# TRUE Values
print(bool("abc"))
print(bool(["apple", "cherry", "banana"]))
print(bool(123))

# FALSE Values
print(bool(False))
print(bool(None))
print(bool(0))
print(bool(""))
print(bool(()))
print(bool([]))
print(bool({}))
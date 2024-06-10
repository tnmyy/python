# FOR LOOP
print('# FOR LOOP')

# BASIC
# 1. Print Numbers from 1 to 10
print('\n1. Print Numbers from 1 to 10')
for x in range(1,11):
    print(x)

# 2. Sum of Numbers from 1 to 100
print('\n2. Sum of Numbers from 1 to 100')
summation = 0
for x in range(1, 101):
    summation += x
print('Sum of first 100 natural numbers is: ', summation)

# 3. Print Each Character in a String
print('\n3. Print Each Character in a String')
string = 'Python'
for x in string:
    print(x)

# INTERMEDIATE
# 4. Skip Multiples of 5
print('\n4. Skip Multiples of 5')
for x in range(1,50):
    if x%5==0:
        continue
    print(x)

# 5. Print Prime Numbers between 1 and 50
print('\n5. Print Prime Numbers between 1 and 50')
for num in range(2, 51):
    is_prime = True
    for i in range(2, num):
        if num%i==0:
            is_prime = False
            break
    if is_prime:
        print(num)

# ADVANCE
# 6. Nested Loops to Print a Multiplication Table
print('\n6. Nested Loops to Print a Multiplication Table')

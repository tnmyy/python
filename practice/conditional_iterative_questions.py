# # Conditional and Iterative Statement Questions
# print('# Conditional and Iterative Statement Questions')

# # 1. WAPP to add all the odd numbers upto N(included)
# print('#1. Add all the odd numbers')
# N = int(input('Enter a number to be added: '))
# total = 0
# i = 1
# while i<=N:
#     total+=i
#     i += 2
# print('The sum of all the odd numbers till',N,'is: ',total)
    
# # 2. WAPP to find the factorial of a N
# N = int(input('Enter a number to get the factorial: '))
# fct = 1
# i = 1
# while i<N:
#     fct *= i
#     i+=1
# print('The factoral of',N,'is: ', fct)

# # 3. WAPP to input 3 numbers from the user and display the maximum and the minimum number among them
# n1 = int(input('Enter the first number: '))
# n2 = int(input('Enter the second number: '))
# n3 = int(input('Enter the third number: '))

# max_num = min_num = None

# if n1>n2 and n1>n3:
#     max_num = n1
#     if n2>n3:
#         min_num = n3
#     else:
#         min_num = n2
# elif n2>n1 and n2>n3:
#     max_num = n2
#     if n1>n3:
#         min_num = n3
#     else:
#         min_num = n1
# elif n3>n1 and n3>n2:
#     max_num = n3
#     if n1>n2:
#         min_num = n2
#     else:
#         min_num = n1
# else:
#     print('All are equal')
        
    
# print('Largest number: ', max_num)
# print('Smallest number: ', min_num)

# # 4. WAPP to input three sides of a right angle triangle and check whether they are pythagorean triplets
# print('\ns#4. Pythagorean triplets')
# s1 = int(input('Enter the first side: '))
# s2 = int(input('Enter the second side: '))
# s3 = int(input('Enter the third side: '))

# if s1**2 == s2**2 + s3**2:
#     print('The entered sides are pythagorean triplets\nHypotenuse:', s1)
# elif s2**2 == s1**2 + s3**2:
#     print('The entered sides are pythagorean triplets\nHypotenuse:', s2)
# elif s3**2 == s1**2 + s2**2:
#     print('The entered sides are pythagorean triplets\nHypotenuse:', s3)
# else:
#     print('No they are not pythagorean triplets')

# # 5. WAPP to make a BMI Calculator
# print('\n#5. BMI Calculator')

# weight = int(input('Enter your weight (in kg): '))
# height = int(input('Enter your height (in cm): '))
# height = height / 100
# bmi = (weight) / (height*height)
# print(bmi)
# if bmi < 18.5 :
#     print('You are Underweight, BMI:', bmi)
# elif bmi < 25:
#     print('You are Normal, BMI:', bmi)
# elif bmi < 30:
#     print('You are Overweight, BMI:', bmi)
# else:
#     print('You are Obese, BMI:', bmi)

# # 6. WAPP to find the sum of series: 1 + x^1 + x^2 + x^3 + .... + x^n
# print('\n#6. Sum of series: 1 + x^1 + x^2 + x^3 + .... + x^n')
# n = 4
# x = 20
# total = 0
# print('Sum of series: ')
# for e in range(n+1):
#     num = x**e
#     print(f'{num},', end=' ')
#     total += num
# print('is:', total)

# # 7. WAPP to find whether a number entered is prime or not
# print('\n# 7. WAPP to find whether a number entered is prime or not')
# num = int(input('Enter the number: '))

# prime = 'Ya ya ya'

# if num <= 1:
#    prime = 'No'
# else:
#    for i in range(2, num):
#        if num % i == 0:
#            prime = 'No'
#            break

# if prime == 'No':
#    print(num, 'is not a prime number')
# else:
#    print(num, 'is a prime number')

# 8. WAPP to count the number of vowels and consonants in a given string.
vowels = 'aeiou'
consonants = 'bcdfghjklmnpqrstvqxyz'
v_count = 0
c_count = 0
string = input('Enter you string: ')
i = 0
while i < len(string):
    if string[i] in vowels:
        v_count += 1
    elif string[i] in consonants:
        c_count += 1
    else:
        pass
    i += 1
print(v_count)
print(c_count)

print(c_count)

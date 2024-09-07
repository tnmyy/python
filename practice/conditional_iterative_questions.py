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
##<<<<<<< ALTER >>>>>>>>>
# n = 6
# count = 0
# for x in range(1,n):
#     if n%x == 0:
#         count += 1
# if count == 1:
#     print('Prime number')
# else:
#     print('Composite number')

# # 8. WAPP to count the number of vowels and consonants in a given string.
# vowels = 'aeiou'
# consonants = 'bcdfghjklmnpqrstvqxyz'
# v_count = 0
# c_count = 0
# string = input('Enter you string: ')
# i = 0
# while i < len(string):
#     if string[i] in vowels:
#         v_count += 1
#     elif string[i] in consonants:
#         c_count += 1
#     else:
#         pass
#     i += 1
# print(v_count)
# print(c_count)

# print(c_count)

# # 9. x + (x^2)/2! - (x^3)/3! .... (x^n)/n!
# x = 4
# n = 5
# sign = -1
# sum_series = x
# i = 2
# while i<=n:
#     fct = 1
#     for f in range(1, i+1):
#         fct *= f
#     nr = x**i * sign**i
#     dr = fct
#     fraction = nr/dr
#     sum_series += fraction
    
#     i += 1
# print(sum_series)

# # 10. WAPP to check for a Armstrong number (a number equivalent to the sum of the cubes of its digits)
# n = 407
# num_sum = 0
# for x in str(n):
#     x = int(x)
#     cube = x**3
#     num_sum += cube
    
# if num_sum == n:
#     print('Yes')
# else:
#     print('No')

# # 11. WAPP to print Fibonacci series up to n terms
# n = 6
# first = 0
# second = 1
# print(first, ',', second, end=', ')

# for x in range(2, n):
#     next = first + second
#     print(next, end=', ')
#     first = second
#     second = next
# print()

# # 12. WAPP to write the LCM and HCF of two integers
# a = 10
# b = 20
# if a > b:
#     small = b
# else:
#     small = a

# lcm = hcf = 0

# for x in range(1, small+1):
#     if (a%x == 0) and (b%x==0):
#         hcf = x
#     lcm = (a*b)/hcf
# print('HCF', hcf)
# print('LCM', lcm)

# # 13. WAPP to break a 6 digit number into three 2 digit numbers
# n = 123456
# if 100000 < n > 999999:
#     print('Valid number please')
# else:
#     num1 = n%100
#     print('n1', num1)
#     int1 = n//100
#     print('i1', int1)

#     num2 = int1%100
#     print('n2', num2)
#     int2 = int1//100
#     print('int2', int2)

#     num3 = int2
# print('given number =', n)
# print('new numbers', num3, num2, num1)

# # 14. Real Armstrong numbers
# n = 1634
# n_str = str(n)
# len_str = len(n_str)
# check = 0

# for x in n_str:
#     x = int(x)
#     power = x**len_str
#     check += power
# if check == n:
#     print('Yess')
# else:
#     print('No')

# n = 5
# for i in range(n):
#     number = 1
#     for j in range(i + 1):
#         print(number, end=" ")
#         number = number * (i - j) // (j + 1)
#     print()

# # 15. WAPP to read an integer > 1000 and reverse the number
# n = 12345
# if n<1000 or type(n)!=type(1):
#     print('Enter an integer>1000')
# digit = n
# num = None
# print('New num =', end=' ')
# while True:
#     num = digit%10
#     digit = digit//10
#     if num == 0:
#         break
#     print(num, end='')

# # 16. WAPP to input a number and then raise the first and the last digit of the number to the number of digits in the number

# n = 19892
# n = str(n)
# ln = len(n)

# first = int(n[0])**ln
# last = int(n[ln-1])**ln
# print(first, '\t', last)

# # 17. WAPP to find the smallest and second smallest from the 10 numbers input

# chhota = sabsechhota = 0
# for x in range(5):
#     n = float(input('Enter the number: '))
    
#     if x == 0: # to initialise the first value and then compare accordingly
#         chhota = n
#     elif x == 1: # to initialise the second input
#         if n <= chhota:
#             sabsechhota = n
#         else:
#             sabsechhota = chhota
#             chhota = n
#     else:
#         if n < sabsechhota:
#             chhota = sabsechhota
#             sabsechhota = n
#         elif n < chhota:
#             sabsechhota = n
            
# print('Smaller: ', chhota)
# print('Smallest: ', sabsechhota)

# 18. WAPP to print divisors of a number
n = 10
print('divisors of', n, 'are: ')
for x in range(1, n+1):
    if n%x==0:
        print(x, end=' ')

# Conditional and Iterative Statement Questions
print('# Conditional and Iterative Statement Questions')

# 1. WAPP to add all the odd numbers upto N(included)
print('#1. Add all the odd numbers')
N = int(input('Enter a number to be added: '))
total = 0
i = 1
while i<=N:
    total+=i
    i += 2
print('The sum of all the odd numbers till',N,'is: ',total)
    
# 2. WAPP to find the factorial of a N
N = int(input('Enter a number to get the factorial: '))
fct = 1
i = 1
while i<N:
    fct *= i
    i+=1
print('The factoral of',N,'is: ', fct)

# 3. WAPP to input 3 numbers from the user and display the maximum and the minimum number among them
n1 = int(input('Enter the first number: '))
n2 = int(input('Enter the second number: '))
n3 = int(input('Enter the third number: '))

max_num = min_num = None

if n1>n2 and n1>n3:
    max_num = n1
    if n2>n3:
        min_num = n3
    else:
        min_num = n2
elif n2>n1 and n2>n3:
    max_num = n2
    if n1>n3:
        min_num = n3
    else:
        min_num = n1
elif n3>n1 and n3>n2:
    max_num = n3
    if n1>n2:
        min_num = n2
    else:
        min_num = n1
else:
    print('All are equal')
        
    
print('Largest number: ', max_num)
print('Smallest number: ', min_num)


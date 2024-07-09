# STRING PRACTICE QUESTIONS
print('# STRING PRACTICE QUESTIONS')

# BASED ON PYTHON STRING OPERATORS
print('# BASED ON PYTHON STRING OPERATORS')
### 1. WAPP to input a an integer and check if it contains 0 in it.
##print('# 1. WAPP to input a an integer and check if it contains 0 in it.')
##n = int(input('Enter the integer: '))
##n = str(n)
##if '0' in n:
##    print('Yes, there is 0 in',n)
##else:
##    print('No, there is no 0 in',n)

# 2. WAPP which asks the user to enter the username and a code. Check that username is not present in code
'''print('# 2. WAPP which asks the user to enter the username and a code. Check that username is not present in code')
user_name = input("Enter the user name: ")
code = input("Enter the code: ")
if user_name not in code:
    print('The user name: ', user_name, '\nThe code:', code)
else:
    print("You have entered the user name in your code!")'''

# 3. WAPP to find the number of vowels, consonants, numbers, spaces in a string
print('# 3. WAPP to find the number of vowels, consonants, numbers, spaces in a string')
vow = 'aeiou'
conso = 'bcdfghjklmnpqrstvwxyz'
num = '0123456789'
spc = ' '
string = input('Enter your string: ')
string = string.lower()

vow_count = conso_count = num_count = spc_count = special_count = 0
for i in range(len(string)):
    if string[i] in vow:
        vow_count+=1
    elif string[i] in conso:
        conso_count +=1
    elif string[i] in num:
        num_count +=1
    elif string[i] in spc:
        spc_count += 1
    else:
        special_count+=1

print('Vowels: ', vow_count)
print('Consonants: ', conso_count)
print('Numbers: ', num_count)
print('Spaces: ', spc_count)
print('Special Characters: ', special_count)

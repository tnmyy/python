# STRING PRACTICE QUESTIONS
##print('# STRING PRACTICE QUESTIONS')
##
### BASED ON PYTHON STRING OPERATORS
##print('# BASED ON PYTHON STRING OPERATORS')
### 1. WAPP to input a an integer and check if it contains 0 in it.
##print('# 1. WAPP to input a an integer and check if it contains 0 in it.')
##n = int(input('Enter the integer: '))
##n = str(n)
##if '0' in n:
##    print('Yes, there is 0 in',n)
##else:
##    print('No, there is no 0 in',n)

# 2. WAPP which asks the user to enter the username and a code. Check that username is not present in code
"""print('# 2. WAPP which asks the user to enter the username and a code. Check that username is not present in code')
user_name = input("Enter the user name: ")
code = input("Enter the code: ")
if user_name not in code:
    print('The user name: ', user_name, '\nThe code:', code)
else:
    print("You have entered the user name in your code!")"""

# 3. WAPP to find the number of vowels, consonants, numbers, spaces in a string
"""print('# 3. WAPP to find the number of vowels, consonants, numbers, spaces in a string')
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
print('Special Characters: ', special_count)"""

# # 4. WAPP to check whether a entered string is palindrome or not

# s = input('Enter the string: ')
# s = s.lower()
# s_ = s[::-1]
# if s == s_:
#     print('Yes it is a palindrome')
# else:
#     print('No it is not a palindrome')

# # 5. WAPP to count the number of alphabets in a string only if there are unique alphabets

# s = 'python 21'
# count = 0
# char_str = 'qwertyuiopasdfghjklzxcvbnm'
# s = s.lower()
# for i in range(len(s)):
#     demo_char = s[i]
#     new_str = s[:i] + s[i+1:]
#     # Making logic for filtering out
#     if demo_char in new_str:
#         print('Characters are being repeated')
#         break
#     elif demo_char not in char_str:
#         count = count
#     elif demo_char not in new_str:
#         count += 1
#     else:
#         pass

# print('Number of characters: ', count)

# # 6. WAPP that reads a line a substring. It should then display the number of occurrences of the given substring in the given line.

# line = input('Enter the line: ')
# substr = input('Enter the substring: ')

# count = 0
# end_ind = len(line)
# start_ind = 0

# while True:
#     check = line.find(substr, start_ind, end_ind)
#     if check != -1:
#         count += 1
#         start_ind = check + len(substr)
#         print(line[start_ind:])
#     else:
#         break
#     if start_ind >= end_ind:
#         break
# print(count)

# # 7. WAPP that prints the fractional(decimal) part of a number
# num = input('Enter the number with decimal part: ')
# decimal = num.partition('.')[2]
# print(decimal)

# # 8. WAPP that counts the number of distinct alphabets in a string
# s = 'Naman'
# s = s.lower()
# dis_s = ''

# for char in s:
#     print(char)

#     if char.isalpha() and char not in dis_s:
#         dis_s+=char

# count = len(dis_s)
# print('Distinct Characters: ', count)
# '''new_str = ''
# for x in s:
#     new_str += x
#     # for y in new_str:
#     #     print(y, end = '')
#     # print(new_str)
#     if x.isalpha():
#         count += 1
#     # print(new_str)
# print(count)'''

# '''new_str = ''
# for char in range(len(s)):
#     # print(s[char])

#     new_str += s[char]

#     # for new_chr in range(len(new_str)):
#     #     print(new_chr, end='')
#     # print()
#     print(new_str)

#     if s[char].isalpha()
#         count += 1'''
# number = int(input("Enter a number: "))
# for i in range(number, number + 10):
#     print(f"\nMultiplication table for {i}:")
#     j = 1
#     while j <= 10:
#         print(f"{i} x {j} = {i * j}")
#         j+=1

# # 9. WAPP that takes a string with multiple words and then capitalizes the first letter of each word and forms a new string out of it.
# string = "this is a string made for just testing purposes, so just simply do not take it seriously"
# sep_str = string.split(" ")
# new_str = ""
# for x in range(len(sep_str)):
#     new_str += sep_str[x][0].upper()
# print(new_str)

# # 10. WAPP that whether reads a string and checks whether it is a palindrome string or not
# # WITHOUT USING SLICING
# string = "NAMAN"
# string = string.lower()
# rev = -1
# start = 0

# for x in range(len(string)):
#     if string[start] == string[rev]:
#         start += 1
#         rev -= 1
#     else:
#         print(string, "is not a palindrome")
#         break
# print(string, "is a palindrome")

# # 11. WAPP that reads a string and then makes every other letter capital and then print the string
# a = "programming"
# new_str = ""
# for x in range(len(a)):
#     if x % 2 == 0:
#         new_str += a[x]
#     else:
#         new_str += a[x].upper()
# print(new_str)

# # 12. WAPP that reads a email address and then prints the domain name i.e. '@xyz.abc'
# email = "google@google.com"
# index = None
# for x in range(len(email)):
#     if email[x] == "@":
#         index = x
#         break
# print(email[index + 1 :])

# # 13. WAPP that reads a string 's' and any character 'c' and then prints the location of every occurrence of 'c' in 's'
# s = "This is the string which I am going to use."
# c = "i"
# for i in range(len(s)):
#     if s[i] == c:
#         print(i, end=" ")

# # 14. WAPP that removes all the special characters from a string
# s = "“rybIk*T! aFhiJ+e$g &n}R2<wu_X 3f(:lQ)W;M#O ?Y,[-m.Po%L_4 DZ@#-%:  (>B=^).Lz|<wW guke}h K12fq6 8A0PiFm] x?XHlY,54M 78rZQnyY._ q@*"
# new_s = ""
# for i in range(len(s)):
#     if s[i].isalnum() or s[i].isspace():
#         new_s += s[i]
# print(new_s)

# # 15. WAPP that prints each word of a sentence in new line and also prints the number of words in the sentence
# s = "This is the sentence which I am going to use"
# s = s.split()
# for x in s:
#     print(x)
# print("The number of characters in the sentence is: ", len(s))

# # 16. WAPP that prints each word of a sentence along it's individual length
# s = "This is the sentence which I am going to use"
# s = s.split()
# for x in s:
#     print(x, "(", len(x), ")")

# 17. WAPP that reads a string a displays the longest substring of the given string having just the consonants

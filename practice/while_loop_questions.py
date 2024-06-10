### LOOP QUESTIONS
##print('# LOOP QUESTIONS')
##
### WHILW LOOP
##print('WHILE LOOP')
### 1. Print number from 0 to 10 (while loop)
##print('# 1. Print number from 0 to 10 (while loop)')
##x = 0
##while x<=10:
##    print(x)
##    x+=1
##print()
### OR
##x = 10
##while x>=0:
##    print(x)
##    x-=1
##
### 2. Print table of any number (from 1 to 10)
##print('\n# 2. Print table of any number (from 1 to 10)')
##i = 1
##n = 17
##while i<=10:
##    print(n,'x',i,'=',n*i)
##    i+=1
##
### 3. Write a while loop that calculates the sum of numbers from 1 to 100.
##print('\n# 3. Write a while loop that calculates the sum of numbers from 1 to 100.')
##i = 0
##summation = 0
##while i<=100:
##    summation += i
##    i+=1
##print('The sum of first 100 natural numbers is: ',summation)
##
### 4. Write a while loop for a number guessing game. The loop should continue until the user guesses the correct number. Use break to exit the loop when the correct number is guessed.
##print('\n# 4. Guess the number (जुआ)')
##import random
##rdm_num = random.randint(1,100)
##score = 100
##while True:
##    usr_num = int(input('Enter a number between 1-100: '))
##    if usr_num == rdm_num:
##        print('Miracle! Miracle! Miracle!\nYou guessed the correct number\nSCORE: ', score)
##        break
##    elif usr_num > rdm_num:
##        print('The number entered in more than the actual number')
##        score -= 1
##    elif usr_num < rdm_num:
##        print('The number entered in less than the actual number')
##        score -= 1
##    else:
##        print('Are you mad!! Enter the number in between the given range(1-100)')
##
### 5. Write a while loop that finds and prints the first number greater than 1548 that is divisible by 13. Use break to exit the loop once the number is found.
##print('\n# 5. First multiple of 13 which is greater than 1548')
##number = 1548
##while True:
##    if number % 13 == 0:
##        print('First multiple of 13 which is greater than 1548 is: ', number)
##        break
##    number += 1
##
### 6. Write a while loop that prints all odd numbers between 1 and 20. Use continue to skip even numbers.
##print('\n# 6. Skipping the even numbers')
##i = 0
##while i<=20:
##    if i%2==0:
##        i+=1
##        continue
##    print(i)
##    i+=1
##
### 7. Write a while loop that prints numbers from 1 to 30, but skips multiples of 3. Use continue to skip these numbers.
##print('\n# 7. Skipping multiples of 2')
##i = 0
##while i<=30:
##    if i%3==0:
##        i+=1
##        continue
##    print(i)
##    i+=1
##
### 8. Write a program that repeatedly asks the user to enter a word. If the user enters "bhaago", the program should exit. Use break to terminate the loop.
##print('\n# 8. Quit only on entering "bhaago"')
##usr_input = None
##while True:
##    usr_input = input('Enter you input: ')
##    if usr_input == 'bhaago':
##        break
##
### 9. Write a while loop that asks the user to enter a number. If the number is negative, use continue to skip printing the number. If the number is zero, use break to end the loop. Otherwise, print the number.
##print('\n# 9. Skipping negative numbers')
##while True:
##    n = int(input('Enter you input number: '))
##    if n<0:
##        continue
##    elif n==0:
##        break
##    print('You entered: ', n)


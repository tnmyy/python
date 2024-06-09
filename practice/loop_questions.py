### LOOP QUESTIONS
##print('# LOOP QUESTIONS')
##
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

# 4. Write a while loop for a number guessing game. The loop should continue until the user guesses the correct number. Use break to exit the loop when the correct number is guessed.
print('\nGuess the number (जुआ)')
import random
rdm_num = random.randint(1,100)
score = 100
while True:
    usr_num = int(input('Enter a number between 1-100: '))
    if usr_num == rdm_num:
        print('Miracle! Miracle! Miracle!\nYou guessed the correct number\nSCORE: ', score)
        break
    elif usr_num > rdm_num:
        print('The number entered in more than the actual number')
        score -= 1
    elif usr_num < rdm_num:
        print('The number entered in less than the actual number')
        score -= 1
    else:
        print('Are you mad!! Enter the number in between the given range(1-100)')

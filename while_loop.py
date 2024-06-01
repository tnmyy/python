print('While Loops in Python')

## Runs as long as the condition is true
i = 0
while i<=10:
    print(i*i)
    i+=1

#With the break statement we can stop the loop even if the while condition is true:
# Ques: Exit the loop when i is 3:
print('Exit the loop when i is 3:')
i = 1
while i<10:
    print(i)
    if i == 3:
        break
    i+=1

# With the continue statement we can stop the current iteration, and continue with the next:
# Ques: Continue to the next iteration if i is 3:
print('Continue to the next iteration if i is 3')
i = 1
while i<10:
    i+=1
    if i == 3:
        continue
    print(i)

#With the else statement we can run a block of code once when the condition no longer is true:
# Print a message once the condition is false:
print('Print a message once the condition is false:')
i = 1
while i<10:
    print(i)
    i+=1
else:
    print('i is no longer smaller than 10')

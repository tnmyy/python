##print('For Loop')
##
### Looping through list
##fruits = ["apple", "banana", "cherry"]
##for x in fruits:
##  print(x)
##
###Looping Through a String
##for x in "banana":
##  print(x)
##
###The break statement
###With the break statement we can stop the loop before it has looped through all the items:
##
###example 1: Exit the loop when fruit is "banana":
##fruits = ['apple','banana','mango']
##print(fruits)
##
##for fruit in fruits:
##	print(fruit)
##	if fruit == 'banana':
##		break
##
###example 2: Exit the loop when fruit is "banana", but this time the break comes before the print:
##print(2)
##fruits = ['apple','banana','mango']
##for fruit in fruits:
## 	if fruit == 'banana':
## 		break
## 	print(fruit)
##
### The continue Statement
### With the continue statement we can stop the current iteration of the loop, and continue with the next:
##
### Example 3: Do not print banana:
##print(3)
##fruits = ["apple", "banana", "cherry"]
##for x in fruits:
##  if x == "banana":
##    continue
##  print(x)
##
##num = input('number')
##num = int(num)
##for x in range(1,11,1):
##    print(num, 'x', x, '=', num*x)

### NESTED LOOPS
##for i in range(1, 6):
##  for j in range(1, i):
##    print('*', end=' ')
##  print( )
##
##adj = ["red", "big", "tasty"]
##fruits = ["apple", "banana", "cherry"]
##
##for x in adj:
##  for y in fruits:
##    print(x, y)
##
### PASS Statement
###for loops cannot be empty, but if you for some reason have a for loop with no content, put in the pass statement to avoid getting an error.
##for x in [1,2,3,4,5]:
##  
##  pass # only of use when the loop body is empty
##  print(x)

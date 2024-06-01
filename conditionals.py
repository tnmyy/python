print('Conditional Statements')

#if
a = 23
b = 100
if b > a : 
	print(f'{b} is greater than {a}')

#elif
x = 30
y = 30
if x > y:
	print('x is greater than y')
elif x == y:
	print('x is equal to y')

#else
a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")

 #and
 #The and keyword is a logical operator, and is used to combine conditional statements:

a = 300
b = 40
c = 500
if a>b and c>a:
 	print('Both are true')

a = 300
b = 40
c = 500
if a>b and c<a:
 	print('Both are true 2.0')

#or
#The or keyword is a logical operator, and is used to combine conditional statements:
a = 200
b = 33
c = 500
if a > b or a > c:
  print("At least one of the conditions is True")

#not
#The not keyword is a logical operator, and is used to reverse the result of the conditional statement:
a = 33
b = 200
if not a > b:
  print("a is NOT greater than b")

#The pass Statement
#if statements cannot be empty, but if you for some reason have an if statement with no content, put in the pass statement to avoid getting an error.
a = 33
b = 200

if b > a:
  pass

#Nested If
#You can have if statements inside if statements, this is called nested if statements.

x = 10.1

if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")
else:
	print('Below 10')
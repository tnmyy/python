print("Functions in Python")


# SYNTAX
# parameter: the variable to store data
# argument: the value to store in variable
# def function_name(param1, parm2):
#     statements
#     return abc
# function_name(arg1, arg2)

# FUNCTION TYPES
# 1. built in functions
# int(), print(), type()

# 2. functions defined in modules
# sin(), random(), abs()

# 3. user defined functions


# eg: write a python function to return fibonacci sequence upto n numbers
def fibo(n):
    a = 0
    b = 1
    lis = [a, b]
    for i in range(n - 2):
        c = a + b
        lis.append(c)
        a, b = b, c
    return lis


print(fibo(10))


# eg: write a python function to print fibonacci sequence upto n numbers
def fibo(n):
    a = 0
    b = 1
    lis = [a, b]
    for i in range(n - 2):
        c = a + b
        lis.append(c)
        a, b = b, c
    print(lis)


fibo(10)


# STRUCTURE OF A PYTHON PROGRAM
# top level statement: not in a function i.e. bina indentation wali
# represented by: _main_
# def f1():
#     :
# def f2():
#     :
# def f3():
#     :
# statement1 ======>>>>> top level statements
# phle top level ko padhega aur agar function call kiya hoga to hi function ke andar taka jhaki karega


# MULTIPLE RETURN VALUES
def multi(x, y, z):
    return x * x, y * y, z * z


c = multi(2, 3, 4)
print(type(c), c)

# OR

a, b, c = multi(2, 3, 4)  # unpacking
print(a, b, c)

# SCOPE OF VARIABLES
# if two variables of same name then follow LEGB rule
# Local, Enclosing(type of nested fun. finds in parent function), Global, Built-in


# Using global scope variable inside local scope
def f1():
    c = 1
    global a  # is se isne global scope wale a ko hi local scope mai use kar liya
    print(a)


a = 20
print(a)
f1()


# question: WAF to find the cube of a number, if no number is entered then return the cube of 2
def cube(a=2):
    return a**3


print(cube(12))
print(cube())


# WAF which receive two strings as arguments and check whether they are of same length or not
def len_str(a, b):
    return True if len(a) == len(b) else False


print(len_str("Hey", "Yoo"))
print(len_str("Hey", "Yo"))


# WAF which takes two numbers and return the one which have the least one's digit
def min_ones(a, b):
    x, y = str(a), str(b)
    return a if x[-1] < y[-1] else b


print(min_ones(12, 323))
print(min_ones(12, 3231))


def min_ones(a, b):
    x = a % 10
    y = b % 10
    return a if x < y else b


print(min_ones(12, 323))
print(min_ones(12, 3231))

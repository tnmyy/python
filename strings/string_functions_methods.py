# STRING FUNCTIONS AND METHODS
print("# STRING FUNCTIONS AND METHODS")

# 1. len() function
# returns the length of a strings
print("# 1. len() function")
a = "Tanmay Upreti"
print(len(a))
print(len("Python is an impressive language"))

# 2. capitalize() method
# capitalizes the first character of a string
print("# 2. capitalize() method")
a = "python"
print(a.capitalize())
print("i love my india".capitalize())

# 3. count() method
# returns the number of times a specified value appears in a string
# SYNTAX: string.count(sub_str, start_index, end_index)
print("# 3. count() method")
a = "Wake up a to a reality"
print(a.count("a"))
print(a[:3])
print(a.count("a", 0, 3))
print(a.count("a", 3))  # returns the occurrence of 'a' after the 3rd index

# 4. find() method
# returns the lowest index, where the sub string searched is found
# returns '-1' if the sub string searched is not found
# SYNTAX: string.find(sub_str, start_index, end_index)
print("# 4. find() method")
a = "twinkle twinkle little star"
b = "little"
print(a.find(b))
b = "little  "
print(a.find(b))

# 5. index() method
# returns the lowest index, where the sub string searched is found (same as find())
# throws error when the searched substring is not found
# SYNTAX: string.index(sub_str, start_index, end_index)
print("# 5. index() method")
a = "twinkle twinkle little star"
b = "little"
print(a.index(b))
b = "little  "
# print(a.index(b)) it thows error

# 6. isalnum() method
# returns True if the characters of a string are alphanumeric (alphabets and numbers). If at least one character is non-alphanumeric, it returns False
# ' ' (empty string) is not considered as alphanumeric
print("# 6. isalnum() method")
a = "abc"
b = "123"
c = "Hey Bro"
print(a.isalnum())
print(b.isalnum())
print(c.isalnum())

# 7. isalpha() method
# Returns True only if there are alphabets in a string, else False
print("# 7. isalpha() method")
a = "abc"
b = "123"
c = "Hey Bro"
print(a.isalpha())
print(b.isalpha())
print(c.isalpha())

# 8. isdigit() method
# Returns True is all the characters in a string are digits, else False
print("# 8. isdigit() method")
a = "abc"
b = "123"
c = "Hey Bro"
print(a.isdigit())
print(b.isdigit())
print(c.isdigit())

# 9. islower()
# Returns True is all the string characters are in lower case
print("# 9. islower()")
a = "abc"
b = " a"
c = "123"
print(a.islower())
print(b.islower())
print(c.islower())

# 10. isspace()
# Returns True if there are only whitespaces in a string. And False if there is at least 1 characters
print("# 10. isspace()")
a = "   "
b = ""
c = "H "
print(a.isspace())
print(b.isspace())
print(c.isspace())

# 11. isupper()
# Returns True is all the string characters are in upper case
print("# 11. isupper()")
a = "ABC"
b = " A"
c = "123"
print(a.isupper())
print(b.isupper())
print(c.isupper())

# 12. lower()
# Converts all the alphabets of a string to lowercase
print("# 12. lower()")
a = "Hey EvEryOne"
b = "Hey EverBodY 123"
print(a.lower())
print(b.lower())

# 13. upper()
# Converts all the alphabets of a string to uppercase
print("# 13. upper()")
a = "Hey EvEryOne"
b = "Hey EverBodY 123"
print(a.upper())
print(b.upper())

# 14.1 lstrip()
# Removes all the leading whitespaces in a string(Left most)
print("# 14.1 lstrip()")
a = "       Hey"
b = "   Hey     "
print(a.lstrip())
print(len(a.lstrip()))
print(b.lstrip())
print(len(b.lstrip()))

# 14.2 rstrip()
# Removes all the trailing whitespaces in a string(Right most)
print("# 14.2 rstrip()")
a = "Hey    "
b = "   Hey     "
print(a.rstrip())
print(len(a.rstrip()))
print(b.rstrip())
print(len(b.rstrip()))

# 14.3 strip()
# Removes whitespaces of both LEADING and TRAILING sides
print("# 14.3 strip()")
a = "   Hey     "
print(a.strip())
print(len(a.strip()))

# 15.1 startswith()
# Returns True if a given string starts with a given substring
print("# 15.1 startswith()")
a = "jkl"
print(a.startswith("j"))

# 15.1 endswith()
# Returns True if a given string ends with a given substring
print("# 15.2 endswith()")
a = "jkl"
print(a.endswith("l"))

# 16. title()
# Returns a title cased version of the string
print("# 16. title()")
a = "PYTHON IS A PROGRAMMING LANGUAGE"
print(a.title())
a = "python is a programming language"
print(a.title())

# 17. istitle()
# Returns True if a given string follows title case
print("# 17. istitle()")
a = "I am writing This text to Check istitle()"
print(a.istitle())
print(a.title().istitle())

# 18. replace()
# Replace the copy of the string, with the new replaced characters
print("# 18. replace()")
a = "python"
print(a.replace("p", "J"))
b = "Python is a awesome coding language"
print(b.replace("coding", "programming"))

# 19. join()
# It joins a string/character after each member of the string iterator.
print("# 19. join()")
a = "1845"
print("p".join(a))

print("HEY".join(a))
print(a.join("*******"))

print(a.join(["Hey", "Bro", "Wasss", "Up"]))

# 20. split()
# It splits a string based on given string or character and returns a list containing split strings as members
print("# 20. split()")
# If no argument is given, it splits the given string on the basis of whitespaces
a = "I love python programming language"
print(a.split())
print(a.split(" "))
print(a.split("p"))

# 21. partition() // not in course
# Splits the string at the first occurrence of separator and returns a TUPLE
print("# 21. partition()")
a = "I love python programming language"
print(a.partition("python"))
print(a.partition("p"))

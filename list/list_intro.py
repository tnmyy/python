# # LISTS : mutable

# print("List Basics")

# # EXAMPLES OF LIST
# empty_list = list()
# print(empty_list)
# empty_list = []
# print(empty_list)

# int_list = [1, 2, 3, 4, 5, 6]
# print(int_list)
# int_list = list((1, 2, 3, 4, 5, 6))
# print(int_list)

# num_list = [1, 2.5545, 12.2, 1.02, 1.00]
# print(num_list)

# al_list = ["a", "b", "c"]
# print(al_list)

# mix_list = ["Python", 132453, None, 12.025]
# print(mix_list)

# multi_line_list = [
#     "This",
#     "is",
#     "a",
#     "long",
#     "list,",
#     "which",
#     "I",
#     "am",
#     "going",
#     "to",
#     "break",
#     "to",
#     "multiple",
#     "lines",
#     "in",
#     "order",
#     "to",
#     "maintain",
#     "the",
#     "consistent",
#     "code",
#     "readability",
# ]
# print(multi_line_list)

# # NESTED LIST
# nested_list = ["example", ["of", "nested", "list"]]
# print(nested_list)

# # Accessing a nested list's elements
# print(nested_list[0])
# print(nested_list[1])
# print(nested_list[1][0])
# print(nested_list[1][1])
# print(nested_list[1][2])

# # CREATING LIST FROM EXISTING SEQUENCES
# l_str = list("python")
# print(l_str)

# l_tuple = list(("1", "2", "3"))
# print(l_tuple)

# # l_via_input = list(input("Enter list elements: "))
# # print(l_via_input)

# # l_via_input_2 = eval(input("Enter your list: "))
# # print(l_via_input_2, type(l_via_input_2))

# ACCESSING INDIVIDUAL ELEMENTS
vowels = ["a", "e", "i", "o", "u"]
print(vowels[0])
print(vowels[-1])
## print(vowels[10]) ERROR

#! Lists are MUTABLE
vowels = ["a", "e", "i", "o", "u"]
print(vowels[2])
vowels[2] = "E"
print(vowels)
print(vowels[2])

# LIST TRAVERSING
l = [1, 2, 3, 4, 5, 6, 7, 8]
for x in l:
    print(x)
print()
for x in range(len(l)):
    print(l[x])

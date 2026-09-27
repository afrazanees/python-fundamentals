# ==============================================================================
# Python Interview Questions, Core Concepts & Practice Exercises
# ==============================================================================

# ------------------------------------------------------------------------------
# 1. LISTS
# ------------------------------------------------------------------------------
# fruits = ["apple", "banana", "orange"]
# print(fruits)
# print(fruits[0])
# print(fruits.append("grape"))
# print(fruits)
# print(fruits.reverse())
# print(fruits)
# print(fruits[0] == "Strawberry")
# fruits[0] = "Peach"
# print(fruits)
# values = ["ABC", 10, True, 1.1]
# print(values)
# numbers = [1, 2, -0, 3]
# print(numbers[-1])
# print(numbers[0:3])
# numbers.sort()
# print(numbers)
# numbers.append("Last Index")
# print(numbers)
# numbers.remove(3)
# print(numbers)
# numbers.pop()
# numbers.pop(2)
# print(numbers)
# print(len(numbers))
# print(0 in numbers)
# print(2 in numbers)
# numbers[0] = "hello"
# print(numbers)


# ------------------------------------------------------------------------------
# 2. TUPLES
# ------------------------------------------------------------------------------
# fruit = ("apple", "banana")
# print(fruit)
# print(fruit[0])
# fruit[0] = "peach"
# fruit[2] = "peach"
# print(fruit)


# ------------------------------------------------------------------------------
# 3. DICTIONARIES
# ------------------------------------------------------------------------------
# data = {
#     "name": "ABC",
#     "Age": 10,
#     "city": "Lahore"
# }
# print(data)
# print(data["name"])
# data["university"] = "XYZ"
# data["CGPA"] = 3.0
# print(data)
# data["CGPA"] = 4.0
# print(data)
# print("name" in data)
# print(data.keys())
# print(data.values())
# print(data.items())
# print(data)


# ------------------------------------------------------------------------------
# 4. FREQUENCY COUNTER
# ------------------------------------------------------------------------------
# Q. Given a list of numbers, count how many times each number appears.
# numbers = [1, 2, 2, 3, 3, 3]
# frequency = {}
# for number in numbers:
#     if number not in frequency:
#         frequency[number] = 1
#     else:
#         frequency[number] += 1
# print(frequency)


# ------------------------------------------------------------------------------
# 5. SETS
# Deduplicates and stores unique values in an unordered collection
# ------------------------------------------------------------------------------
# numbers = {1, 2, 3, 1, 2, 0}
# print(numbers)
# numbers = {1, 2, 3, 1, 2, "0"}
# print(numbers)
# numbers = {1, 2, -13, 1, 2, "0"}
# print(numbers)
# values = [1, 2, 3, 4, 2]
# print(set(values))


# ------------------------------------------------------------------------------
# 6. TYPE CONVERSION
# ------------------------------------------------------------------------------
# print(10 // 3)
# What happens with int("hello")? -> Raises ValueError
# text = "Hello"
# print(int(text))


# ------------------------------------------------------------------------------
# 7. EQUALITY (==) VS IDENTITY (is)
# ------------------------------------------------------------------------------
# a = [1, 2]
# b = [1, 2]
# print(a == b)   # True (same values)
# print(a is b)   # False (different memory addresses)
# print(a is a)   # True (same object)


# ------------------------------------------------------------------------------
# 8. LOOP CONTROL: CONTINUE
# ------------------------------------------------------------------------------
# numbers = [1, 2, 3, 4]
# for i in numbers:
#     if i == 3:
#         continue
#     print(i)
# print(i)


# ------------------------------------------------------------------------------
# 9. STRING METHODS
# ------------------------------------------------------------------------------
# sentence = "Python is useful"
# words = sentence.split()
# print(words)
# text = "   hello world   "
# print(text)
# print(text.strip())
# text = "xxxyyyHello Worldyyyxxx"
# print(text)
# print(text.strip("xy"))
# text = "www.example.com"
# print(text.strip(".com"))
# print(text.strip("w.com"))


# ------------------------------------------------------------------------------
# 10. DEFAULT ARGUMENTS
# ------------------------------------------------------------------------------
# def greet(name="User"):
#     return f"Hello {name}"
# print(greet())
# print(greet(name="ABC"))


# ------------------------------------------------------------------------------
# 11. VARIABLE SCOPE (LEGB RULE)
# ------------------------------------------------------------------------------
# LOCAL SCOPE - A variable created inside a function.
# def myFunc():
#     x = 10
#     print(x)
# myFunc()
# # print(x) # Throws NameError

# ENCLOSING SCOPE - Occurs when you have a nested function.
# def outer():
#     x = 10
#     def inner():
#         print(x)
#     inner()
# outer()

# GLOBAL SCOPE - A variable defined outside all functions.
# x = 10
# def myFunc():
#     print(x)
# myFunc()

# BUILT-IN SCOPE - Built-in names provided automatically by Python.
# word = "Hello"
# print(word)
# print(len(word))


# Scope Challenge Question:
# x = "global"
# def outer():
#     x = "enclosing"
#     def inner():
#         x = "local"
#         print(x)
#     inner()
# outer()


# ------------------------------------------------------------------------------
# 12. EXCEPTION HANDLING
# ------------------------------------------------------------------------------
# x = 10
# y = 0
# print(x / y)

# try-except - ZeroDivisionError
# x = 10
# y = 0
# try:
#     print(x / y)
# except ZeroDivisionError:
#     print("Divisor cannot be zero")

# Multiple exceptions - ValueError & ZeroDivisionError
# try:
#     number = int(input("Enter a number: "))
#     divisor = int(input("Enter a divisor: "))
#     result = number / divisor
#     print(result)
# except ValueError:
#     print("Invalid number!")
# except ZeroDivisionError:
#     print("Divisor cannot be zero!")

# Else - Runs only when no exception occurs
# try:
#     result = 10 / 2
# except ZeroDivisionError:
#     print("Divisor cannot be zero!")
# else:
#     print("Result: ", result)

# Finally - Runs whether an exception occurs or not
# try:
#     result = 10 / 0
# except ZeroDivisionError:
#     print("Divisor cannot be zero!")
# finally:
#     print("Finished!")

# try:
#     result = 10 / 2
#     print(result)
# except ZeroDivisionError:
#     print("Divisor cannot be zero!")
# finally:
#     print("Finished!")


# ------------------------------------------------------------------------------
# 13. LIST COMPREHENSIONS
# Short and convenient way to create a new list from an existing iterable
# ------------------------------------------------------------------------------
# Standard approach:
# numbers = [1, 2, 3, 4]
# square = []
# for number in numbers:
#     square.append(number ** 2)
# print(square)

# Using List Comprehension: [expression for item in iterable]
# square = [number ** 2 for number in numbers]
# print(square)


# ------------------------------------------------------------------------------
# 14. PRACTICE QUESTIONS & PROBLEMS
# ------------------------------------------------------------------------------

# Q. Write a Python function that takes a list of numbers and returns the largest number.
# def find_largest(numbers):
#     if not numbers: # Handles empty list
#         return None
#     largest = numbers[0] # Assume value at starting index is largest
#     for number in numbers:
#         if number > largest:
#             largest = number
#     return largest
# number = [10, 20, 100, 30, 40]
# result = find_largest(number)
# print(result)


# Q. How would you count how many times each number occurs?
# numbers = [1, 2, 2, 3, 3, 3, 4]
# frequency = {}
# for number in numbers:
#     if number not in frequency:
#         frequency[number] = 1
#     else:
#         frequency[number] += 1
# print(frequency)


# ------------------------------------------------------------------------------
# 15. MUTABLE VS IMMUTABLE OBJECTS
# ------------------------------------------------------------------------------
# Mutable (e.g., list, dict, set)
# number_list = [10, 20, 30]
# print(id(number_list))
# number_list[1] = 30
# print(id(number_list))

# Immutable (e.g., int, float, str, tuple)
# x = 10
# print(id(x))
# x = 20
# print(id(x))


# ------------------------------------------------------------------------------
# 16. ENUMERATE
# ------------------------------------------------------------------------------
# Standard approach:
# i = 0
# items = ["apple", "mango", "oranges"]
# for item in items:
#     print(i, items[i])
#     i += 1

# Using enumerate:
# items = ["apple", "mango", "oranges"]
# for i, item in enumerate(items):
#     print(i, item)


# ------------------------------------------------------------------------------
# 17. ZIP FUNCTION
# Pairs corresponding indexed elements together
# ------------------------------------------------------------------------------
# names = ["ABC", "XYZ", "PQR"]
# ages = [20, 30, 10]
# for names, ages in zip(names, ages):
#     print(names, ages)
# names = ["ABC", "XYZ", "PQR", "LMN"]
# ages = [20, 30, 10]
# for names, ages in zip(names, ages):
#     print(names, ages)


# ------------------------------------------------------------------------------
# 18. *ARGS & **KWARGS
# ------------------------------------------------------------------------------
# *args - Allows passing multiple positional arguments (packed as a tuple)
# def args(*args):
#     print(args)
#     print(sum(args))
# args(1,2,3,4)

# **kwargs - Allows passing multiple keyword arguments (packed as a dictionary)
# def krwargs(**kwargs):
#     print(kwargs)
# krwargs(name="ABC", age = 10)


# ------------------------------------------------------------------------------
# 19. SHALLOW COPY VS DEEP COPY
# ------------------------------------------------------------------------------
# Shallow Copy - Copies only the outer container, but shares nested references.
# Example:
# a = [1, 2, 3]
# b = a
# print(b)
# b[1] = 10
# print(a)

# Deep Copy - Copies the outer container and makes brand-new duplicates of all nested objects.
# Example:
# import copy
# box1 = [["Apple"]]
# box2 = copy.copy(box1)
# box3 = copy.deepcopy(box1)
# # box1[0] = "Orange" # This only changes the outer container
# box1[0][0] = "Oranges"
# print(box2)
# print(box3)


# ------------------------------------------------------------------------------
# 20. OUTPUT PREDICTION QUESTIONS
# ------------------------------------------------------------------------------
# Q. What does this output?
# x = [1, 2, 3]
# y = x
# y.append(4)
# print(x)

# Q. What happens here?
# def change(items):
#     items.append(10)
# numbers = [1, 2, 3]
# change(numbers)
# print(numbers) # It will append 10 to the list, because lists are mutable.

# def change(items):
#     items.append(10)
# numbers = (1, 2, 3)
# change(numbers)
# print(numbers) # Will raise an AttributeError because tuples are immutable.


# Q. Create a list containing only even numbers - using List Comprehension
# numbers = [1, 2, 3, 4, 5]
# result = [item for item in numbers if item % 2 == 0]
# print(result)


# Q. Write a function that returns the largest number in a list.
# def find_largest(numbers):
#     largest = numbers[0]
#     for number in numbers:
#         if number > largest:
#             largest = number
#     return largest
# list = [4, 2, 9, 1, 7]
# result = find_largest(list)
# print(result)


# Q. Write a function to count vowels in a string.
# def count_vowels(string):
#     count = 0
#     for char in string.lower():
#         if char == "a":
#             count += 1
#         elif char == "e":
#             count += 1
#         elif char == "i":
#             count += 1
#         elif char == "o":
#             count += 1
#         elif char == "u":
#             count += 1
#     return count
# string = "Hello World"
# result = count_vowels(string)
# print(result)

# OR:
# def count_vowels(string):
#     vowels = "aeiou"
#     count = 0
#     for char in string.lower():
#         if char in vowels:
#             count += 1
#     return count
# string = "Hello World"
# result = count_vowels(string)
# print(result)


# Q. Write a function to reverse a string.
# Slicing syntax: [start:end:step].
# Leaving start and end blank with a step of -1 traverses backwards from the last letter to the first.
# text = "Hello"
# print(text[::-1])

# OR:
# def reverse_string(string):
#     reversed_string = ""
#     for char in string:
#         reversed_string = char + reversed_string
#     print(reversed_string)
# reverse_string("Hello")


# Q. Write a function to find duplicates in a list.
# num_list = [10, 11, 10, 30, 20, 11]
# set = {}
# for num in num_list:
#     if num not in set:
#         set[num] = 1
#     else:
#         set[num] += 1
# for num in set:
#     if set[num] > 1:
#         print(f"Number", num, "is duplicate")

# OR:
# def find_dup(numbers):
#     duplicates = []
#     for num in numbers:
#         if numbers.count(num) > 1 and num not in duplicates:
#             duplicates.append(num)
#     return duplicates
# print(find_dup([10, 11, 10, 30, 11]))


# Q. Write a function to find two numbers in an array that add up to the target.
# def two_sum(numbers, target):
#     for i in numbers:
#         for j in numbers:
#             if i + j == target:
#                 return [i, j]
# print(two_sum([2, 11, 7, 15], 9))


# Q. Write a function that returns the first character that appears only once.
# def first_non_repeating(text):
#     for char in text:
#         if text.count(char) == 1:   
#             return char
# print(first_non_repeating("aabbcdd"))
# print(first_non_repeating("swiss"))
# print(first_non_repeating("aabbcc"))

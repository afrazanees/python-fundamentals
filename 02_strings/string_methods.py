# In python we have multiple built-in functions that are specific to strings
# We refer to functions as "Methods"
# In python, everything is Object. And "Objects" in Python have functions called "Methods".
# To Use/Call those functions, we use the "DOT NOTAtION".

# Here "Course" is an "object".
course = "Python Programming"

# 1. To convert string to uppercase
print(course.upper())
# Another way to represent it
course_uppercase = course.upper()
print(course_uppercase)
# Functions does not change original string, rather it creates a copy of Original string and modifies that string.
print(course)

# 2. To convert string to lowercase
print(course.lower())

# 3. To "Capitalize" the first Letter of each word in a string
print(course.title())

# 4. To strip extra spaces from start and end
course1 = " Hello World! "
print(course1)
print(course1.strip())
# To strip extra space only from left
print(course1.lstrip())
# To strip extra space from right
print(course1.rstrip())

# 5. To find "Index of Character" OR "Index of Sequence of Characters" in a string
course2 = "Hello World!"
print(course2.find('W'))
# If chracter is not in a string, it will return "-1"
print(course2.find("P"))
# To find "Sequence of chracter"
print(course2.find("ld"))

# 6. To replace any "Chracter" Or "Sequence of Character" with another "Chracter/Sequence of Character"
print(course2.replace("l", "X"))
print(course2.replace("Hello", "Hi"))
print(course2.replace("lo", "looooo"))

# 7. To check if "Character or Sequence of Characters" exists in a String,
# we have "IN OPERATOR"
course3 = "Hello Python"
print("Python" in course3)
print("World" in course3)

# The difference b/w "Find Method/function" and "Expression (i.e., Python in course) is that
# "Find Method" returns the index while the expression with "IN Operator" returns "Boolean Value"
# to tell whether specified chracter exists in strng or not."

# 8. To check if "Character or Sequence of Characters" does not exists in a String
print("Hello" not in course3)
print("True" not in course3)

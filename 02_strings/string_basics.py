name1 = "This is a comment"

name2 = 'This is a comment'

name3 = "Hello World!"

name = """
Hello!
This is a multiple-line comment
"""

# Built in Functions for strings
count = len(name1)
print(count)

# Second way
print(len(name))

# stringInput = input("Enter a string: ")
# print(stringInput)

# Print specific chracter
print(name3[0])

# We can also use a negative index
# It will return end of string
print(name3[-1])


# We can also slice a string
# SYNTAX:
# string_name [ starting_index : Ending Index ]
# Where ending index is not included

# This will print "Hello"
print(name3[0:5])

# This will print "Hell".
print(name3[0:4])

# To display full string starting from specified index i.e., 0
print(name3[0:])

# To display index upto certain index, without mentioning start index
print(name3[:5])  # Python will automatically consider starting index as "0"

# To display exact copy of original string
print(name[:])

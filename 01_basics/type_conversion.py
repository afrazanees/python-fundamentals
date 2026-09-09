# Input function - To get input from the user
# int = input("Enter a input: ") # Input function always treat USER-INPUT AS STRING
# print(int)

# Problem
# x = input("X: ")
# y = x + 1
# print (y)
# It will throw a "TypeError", which basically means you can not add values of different 
# data types. 
# i.e., "1" + 1 
# where "1" is a string and 1 is an integer.

# Solution
# To resolve this issue, python provides "TypeConversion" which converts data from one type to another.

# In python, we have few built-in "TypeConversion Funtions". i.e.,
# int(x)     # Convert value to an integer
# float(x)   # Convert value to an floating pointing number
# bool(x)    # Convert value to an bool
# str(x)     # Convert value to an string


# To find type of value/data
# z = input("Enter a value: ")
# print(type(z))


# EXAMPLE to ABOVE PROBLEM
# First 
# x = int(input("x: "))
# print(type(x))

# Second 
# x = input("x: ")
# y = int(x) + 1
# print(y)

# Printing x and y using "Formatted String"
# x = input("x: ")
# y = int(x) + 1
# print(f"x: {x}, y = {y}")




# All built-in "TypeConversions Methods" are self-explanatory, except bool(x)
# In python, we have concept of "Truthy" and "Falsy" values.
# These are values that are not exactly the boolean "TRUE OR FALSE" but they can be interpreted 
# as a Boolean "TRUE OR FALSE"

# FALSY VALUES IN PYTHON
# 1. Empty Strings - ""
# 2. Zero - 0
# 3. None - It's an object which represents an absence of a value.

# Whenever we use above "FALSY" values in context of boolean, we will always get "FALSE"
# All other values are "TRUTHY".

# EXAMPLES
# 1.
print(bool(""))            # It will give "FALSE"

# 2.
print(bool(0))             # It will give "FALSE"

# 3.
print(bool(None))          # It will give "FALSE"
# NOTE THAT "None" is case-sensitive. 

# Everything else will result in "TRUE"
# 4. 
print(bool(-1))
print(bool(5))
print(bool("FALSE"))
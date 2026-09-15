# Types of functions in Python

# 1. Functions that perform a specifc task. For example, print() function which performs a task of printing something on the terminal.
# def greet(name):
#     print(f"Hi {name}")
# greet("John Doe")


# 2. Functions that calculate and return a value. For example, round() function which returns a value.
# def greet(name):
#     return f"Hi {name}"
# returnValue = greet("John Doe")
# print(returnValue)
# After getting "return value", we can do whatever we want with this value such as "printing to the terminal" or "writing returned value to the file".


# NOTE that, by default all functions returns a "None" value. "None" is an object that represents the absence
# of the value. But if you specifically "returns a value", "None" will not be returned as default-value.
# None Value:
# def greet(name):
#     print(f"Hi {name}")
# greet("John Doe")           # This will print the actual statement defined in a function
# print(greet("John Doe"))    # This will print the actual statement PLUS "None" because no
#                             # no "reutrn type" is specified in the function.

# Return Value:
def greet(name):
    return name
print(greet("John Doe"))
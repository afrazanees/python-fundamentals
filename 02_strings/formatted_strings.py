first = "Hello"
last = "World!"

# To Format a string there are two ways

# 1. Concatenation
full = first + last
print(full)
# To add a space between both words
full1 = first + " " + last
print(full1)
# NOTE THAT TWO OBJECTS CAN ONLY BE CANCATENATED IF THEY ARE OF SAME TYPE

# 2. Formatted strings - BETTER AND NEWER APPROACH
# Formatted strings does not have any constant values (like "first" or "last")
# Formatted strings is an expression that will be evaluated at runtime.
full3 = f"{first} {last}"
print(full3)
# You can add any valid expressions inside curly-braces i.e., {}
full4 = f"{len(first)} {last}"
print(full4)
# OR
full5 = f"{first} {2+2}"
print(full5)
# OR
full6 = f"{2+2} + {10+2}"
print(full6)

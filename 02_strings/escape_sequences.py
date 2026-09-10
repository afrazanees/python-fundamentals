# \ is a Escape Chracter. It's a special chracter in Python.
# Common Escape Sequence:
# \"
# \'
# \\
# \n

name = "Python Programming"
print(name)

# If we want to add double-quotes(" ") in a string, python interpretor classify this as invalid syntax.
# Un-Comment below expression to see
# name = "Python " Programming"
# print(name)

# To avoid this issue, we use "Escape Sequences"

# 1. To dispaly double-quotes in a string
name1 = "Python \"Programming"
print(name1)

# 2. To display a single-quote in a string
name2 = "Python \'Programming"
print(name2)

# 3. To display a backslash in a string
name3 = "Python \\Programming"
print(name3)

# 4. To add a new line
name4 = "Python \nProgramming"
print(name4)

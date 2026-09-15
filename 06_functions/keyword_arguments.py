def increment(number, by):
    return number + by

# Ways to represent function calls
# 1.
result = increment(10, 1)
print(result)

# 2.
print(increment(20, 1))

# 3. 
# Sometimes there can be multiple arguments in function call, so for better understanding what
# each arguments do, we can write as following:
print(increment(30, by=1))       
print(increment(number = 40, by = 1))       
# In this case, "by = 1" or "number = 40" is a "KEYWORD ARGUMENT"
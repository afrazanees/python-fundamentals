# All the parameters that you defined for a function are required by "DEFAULT".
# We can make parameters "OPTIONAL".

# ALL PARAMETERS REQURED:
# def increment(number, by):
#     return number + by

# print(increment(10, by = 1))


# Making "by argument" OPTIONAL:
# def increment(number, by=1):
#     return number + by

# print(increment(10))
# In this case, we are not passing any value of "by" as an argument. So python interpreter will
# execute this function with default value of "by=1".

# Another case: If we also pass value of "by" as argument, then Python interpreter treat "by value"
# that is provided as argument and not default value.
def increment(number, by=1):
    return number + by

print(increment(10, by = 10))


# # NOTE that all "optional parameters" should come after "required parameters".
# i.e.,
# increment(number, by=1)                   is correct
# increment(number, by=1, another_pram)     is wrong
# increment(by=1, number)                   is wrong

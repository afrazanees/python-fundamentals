# for x in range(5):
#     print(x)
# In above example, range() is a function that returns an object of data type "range". And range
# is iterable, which means we can iterate over it or use it in a for loop.
# In other words, range() function returns an iterable object.

# More Iterbles objects in Python:
# 1. range objects
# 2. Strings
# 3. List


# Example:

# # 1. Range Object
# for x in range(4):
#     print(x)
# In each iteration, x will have a different value (i.e., 1, 2, 3..)


# # 2. String Iterable
# for x in "PYTHON":
#     print(x)
# In each iteration, x will hold one character at a time.


# 2. List
# It is used to store a list of objects. 
# Here Square-Bracket ( i.e., [] ) indicates a list. 
# It can have list of numbers or strings etc.
for x in [1, 2, 3, 4]:
    print(x)
# In each iteration, x will have one object in the list.

# OR EMPTY-LIST
for x in []:
    print(x)
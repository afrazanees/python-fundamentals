# A data structure is a way of organizing and storing data in memory so that it can be efficiently
# accessed and manipulated.
# Stack is a linear data structure.
# It works on a LIFO (Last In, First Out) basis.

# In Python, to implement a stack, we can use a list.
stack = []

# Way to "append (or push)" data onto the stack
stack.append(10)
stack.append(20)
stack.append(30)
stack.append(40)
print(stack)

# Way to "pop (or remove)" data from the stack
stack.pop()
print(stack)
stack.pop(1)
print(stack)

item = stack.pop()
print(stack)
print(item)

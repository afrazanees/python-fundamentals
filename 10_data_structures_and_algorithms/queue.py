# Queue follows FIFO (First In, First Out)
# For an efficient queue in Python, we use "collections.deque"

from collections import deque

queueName = deque()

queueName.append("A")
queueName.append("B")
queueName.append("C")
queueName.append("D")
queueName.append("E")

print(queueName)

queueName.pop()
print(queueName)

queueName.popleft()
print(queueName)


# We can use a list as a queue because appending is similar to using a list as a stack.
# But to pop an element from the front of a list, we must call list.pop(0). This requires shifting
# all remaining elements in memory, which is O(n).
# However, using collections.deque, popleft() is O(1).

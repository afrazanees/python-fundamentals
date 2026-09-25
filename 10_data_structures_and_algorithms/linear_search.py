# Linear Search
# Searches sequentially through an iterable until the target element is found.

def linearSearch(numbers, target):
    for i, num in enumerate(numbers):
        if num == target:
            return i
    return None

print(linearSearch([1, 2, 3, 5, 10], 5))
print(linearSearch([1, 2, 3, 5, 10], 11))

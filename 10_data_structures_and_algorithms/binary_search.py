# Binary Search
# Finds the index of a target value within a sorted array using divide-and-conquer.

def BinarySearch(numbers, target):
    start = 0
    end = len(numbers) - 1

    while start <= end:
        mid = (start + end) // 2

        if numbers[mid] == target:
            return mid
        elif target > numbers[mid]:
            start = mid + 1
        else:
            end = mid - 1

    return -1


print(BinarySearch([1, 2, 3, 5, 10], 5))

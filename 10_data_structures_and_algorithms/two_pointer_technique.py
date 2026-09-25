# The two-pointer technique is an optimization pattern where you use two index variables ('pointers')
# to traverse an array or string at the same time—usually to avoid nested loops and bring an 
# O(n^2) solution down to O(n).

# # Example 1: Check if a Word is a Palindrome
# def is_palindrome(string):
#     left = 0
#     right = len(string) - 1

#     while left < right:
#         if string[left] != string[right]:
#             return False
#         left += 1
#         right -= 1

#     return True

# print(is_palindrome("radar"))
# print(is_palindrome("Hello"))



# Example 2: Two Sum on a Sorted Array
def two_sum_sorted(numbers, target):
    left = 0
    right = len(numbers) - 1

    while left < right:
        sum = numbers[left] + numbers[right]
        if sum == target:
            # return [left, right]                      # For displaying index
            return [numbers[left], numbers[right]]      # For displaying values
        elif target > sum:
            left += 1
        else:
            right -= 1
    
print(two_sum_sorted([1, 2, 4, 6, 8, 9], 10))

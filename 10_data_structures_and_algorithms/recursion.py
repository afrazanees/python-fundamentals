# A recursive function calls itself.
def countdown(n):
    # Base case - Stops recursion
    if n == 0:
        return
    
    print(n)
    # Recursive case - Calls itself
    countdown(n - 1)

countdown(3)

# Without a base case, recursion will continue until Python raises a RecursionError (stack overflow).

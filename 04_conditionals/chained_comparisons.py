# Example: Implement a rule that says "age" should be between 18 and 65.

# Basic Way
age = int(input("Enter your age: "))
if age >= 18 and age <= 65:
    print("Eligible")
else:
    print("Not Eligible")

# Way to write this comparison in "MATH"
# 18 <= age <= 65
# We can write this exaclty same in python


# Below method is called "Chaining Comparison Operator":
# It's a Simpler and more Cleaner way to write same expressions.
age = int(input("Enter your age: "))
if 18 <= age <= 65:
    print("Eligible")
else:
    print("Not Eligible")

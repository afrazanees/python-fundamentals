# Example: Get age from user and find out if user is eligible or not.

# age = int(input("Enter your age: "))
# if age >= 18:
#     print("Eligible")
# else:
#     print("Not Eligible")


# Another way to write it.
# age = int(input("Enter your age: "))
# if age >= 18:
#     message = "Eligible"
# else:
#     message = "Not Eligible"
# print(message)
# When we have above scenario, in which you are assigning a value to a variable, there's a cleaner
# and more simpler way to write it.


# Ternary Operator
age = int(input("Enter your age: "))
message = "Eligible" if age >= 18 else "Not Eligible"
print(message)
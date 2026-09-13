# We use "Conditional Statements" when we have to make decisions.
# Example

# If - Statment
# temperature = 35
# if temperature > 30:            # After if, we add Boolean Expression/Statement, which is simply an expression which gives Boolean value (i.e., True or False)
#     print("It's Warm")
#     print("Drink Water!")
# print("Conditional Statement Executed")

# Else-If Statement - Represented by "elif"
# Its used when we need to add more than one condition
# temperature = 25
# if temperature > 30:
#     print("It's Warm")
#     print("Drink Water!")
# elif temperature > 20:
#     print("Weather is nice.")
# print("Conditional Statement Executed")


# Else Statment - If none of previous conditions are executed, this will execute.
# Its used when we need to add more than one condition
temperature = 15
if temperature > 30:
    print("It's Warm")
    print("Drink Water!")
elif temperature > 20:
    print("Weather is nice.")
else:
    print("It's Cold!")
print("Conditional Statement Executed")
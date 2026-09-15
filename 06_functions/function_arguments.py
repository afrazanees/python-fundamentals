# Example: Sample Funtion
# def greet():
#     print("Hi there!")
#     print("Welcome aboard!")

# greet()

# Q. What's the difference between print() and greet() functions?
# A. print() is a built-in function and gret() is a custom-function. Another difference is that
#    print() function can take an input but greet() function does not take an input.

# To pass input to "greet()" function, we defined "parameters" when creating a function.
# And to pass input values to greet() function, we supply input values as "arguments."

# Q. Difference between between parameter and argument?
# A. A "parameter" is the input that you define for your function. Whereas an "argument" is the actual
#    value for the defined/given "parameter".

# # Example with arguments
# def greet(first_name, last_name):
#     print(f"Hi {first_name} {last_name}")
#     print("Welcome aboard!")

# greet("John", "Doe")
# greet("Jane", "Doe")

# Another way
def greet(first_name, last_name):
    print(f"Hi {first_name} {last_name}")
    print("Welcome aboard!")

firstName = input("Enter first name: ")
lastName = input("Enter last name: ")
greet(firstName, lastName)
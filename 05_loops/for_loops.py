# Loops
# We use loops to create repetition. Or in another words, loops are used to execute tasks that 
# require repitition

# Examples
# 1. Print word "Attempt" 3 times using for loop
for number in range(3):
    print("Attempt")
# Where "range()" is a built-in function. It's used to specify how many times we want to repeat this task.
# Where "numbers" is a variable of type integer. The intial value of number is 0. And with each iteration, its value gets incremented by 1.

# 2. 
for number in range(3):
    print(number)

# 3. 
for number in range(3):
    print("Attempt", number)

# 4. More user-friendly way to represent number, starting from 1 instead of defaut-0.
for number in range(3):
    print(number+1)
# Another way
for number in range(1, 4):          # It will start from 1 and finish before 4 (i.e., 1,2,3s)
    print(number)

# 5. Adding third-argument in range() as a "Step"
for number in range(1, 10, 2):
    print(number)

# 6.
for number in range(3):
    print((number + 1) * ".")
# In this example, the "string" is multiplied by a number. The result will be that 
# "string" repeated specified "numbers of time".


# 7.
for x in range(1, 11):
    print(2 * x)
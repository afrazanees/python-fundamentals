# WHILE LOOP - It is used to iterate/repeat a block of code as long as the condition is true.

# Example 1:
# number = 100
# while number > 0:
#     print(number)
#     # number = number // 2
#     number //= 2


# Example 2:
# command = ""
# while command != "quit":
#     command = input(">")
#     print("ECHO", command)

# For case to handle if user enter different type of "quit" such as "QUIT" or "Quit"
command = ""
while command.lower() != "quit":
    command = input(">")
    print("ECHO", command)

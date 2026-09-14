# for number in range(3):
#     print("Attempt")

# Example: Consider the scenario where after attempt, message is sent successfully. So in this case,
# we want to jump out of loop without repeating another attempt message.
# successful = True
# for number in range(3):
#     print("Attempt")
#     if successful:
#         print("Successful")
#         break
# This will break to for-loop when successful = True.
# OR
# successful = False
# for number in range(3):
#     print("Attempt")
#     if successful:
#         print("Successful")
#         break


# For-Else Loop
# Consider the scenario in which even afte all attempts, the status of successful is "False".
# In such a case, we want to display a different message to user.
# successful = False
# for number in range(3):
#     print("Attempt")
#     if successful:
#         print("Successful")
#         break
# else:
#     print("Attempted 3 times but failed!")
# NOTE that the statments in "else block" will only be executed if "for loop" completes without an
# early termination. So, if "break" is never executed, the "else - statement" will be executed.

# OR
successful = True
for number in range(3):
    print("Attempt")
    if successful:
        print("Successful")
        break
else:
    print("Attempted 3 times but failed!")
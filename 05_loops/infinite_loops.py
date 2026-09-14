# Infinite Loop - It's a loop which runs forever

while True:
    command = input(">")
    print("ECHO", command)
    if command.lower() == "quit":
        break
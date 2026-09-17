# Write a program to display even numbers from 1 to 10.
# Output should be:
# 2
# 4
# 6
# 8
# We have 4 even numbers

# CODE:
count = 0
for x in range(1, 10):
    if (x % 2 == 0):
        count += 1
        print(x)
print(f"We have {count} even numbers")
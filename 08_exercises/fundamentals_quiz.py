# PRIMITIVE DATA TYPES
# 1. Strings
# 2. Numbers - It can be Integers, Floats, Complex
# 3. Boolean

# COMPLEX DATA TYPES
# 1. range - range() function returns the object of "range data type".
# 2. lists

# Q. 1
fruits = "Apple"
print(fruits[1])        # It will show "p" in terminal
print(fruits[0:-1])     # It will slice the string. Starting index is 0 which represents first 
                        # chracter which is 'A' and last index is -1 which represents last 
                        # chracter of string i.e., 'e'. 
                        # NOTE that chracter at ending index is not included in sliced string.
                        # So, it will slice string staring from 'A' to 'l'

# Q. 2
print(ord("a"))
print(ord("b"))
print(ord("c"))


# Q. 3
if 10 == "10":
    print("a")
elif "bag" > "apple" and "bag" > "cat":
    print("b")
else:
    print("c")
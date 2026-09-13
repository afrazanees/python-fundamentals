# In python we have three "Logical Operators". We use these operators to handle more complex conditions:
# 1. and
# 2. or
# 3. not

# And - Will be ture, if all conditions are ture
# Example: Consider an application to grant loan. Laon will be given if user has high_income and good credit score.
# high_income = True
# good_credit = True

# if high_income and good_credit:
#     print("Eligible")
# else:
#     print("Not Eligible")


# Or - Will be ture, if any single condition is ture
# Example: Consider an application to grant loan. Laon will be given if user has high_income and good credit score.
# high_income = True
# good_credit = False
# if high_income or good_credit:
#     print("Eligible")
# else:
#     print("Not Eligible")

# high_income = False
# good_credit = False
# if high_income or good_credit:
#     print("Eligible")
# else:
#     print("Not Eligible")


# Not - Reverse the Boolean value of condition
# Example: Loan will not be granted if user is "Student".
# student = True
# if student:
#     print("Not Eligible")
# else:
#     print("Eligible")


# Multiple Conditions
# Example: Loan will be granted only if user has either "Good Credit" OR "High Income" and is "Not a Student".
high_income = True
good_credit = False
student = False
if (high_income or good_credit) and not student:
    print("Eligible")
else:
    print("Not Eligible")

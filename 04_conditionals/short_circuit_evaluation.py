# Example: Loan will be granted only if user has "Good Credit" and "High Income" and is "Not a Student".

# Case - 1: 
high_income = False
good_credit = True
student = True
if high_income and good_credit and not student:
    print("Eligible")
else:
    print("Not Eligible")


# NOTE that, in Python, Short Circuiting is a concept in which interpreter stops evaluating
# as soon as one of the arguments/conditions evaluates to "False".
# i.e, high_income = False results in interpreter to stop evaluating remaining conditions because
# it's evaluated to "False".



# CASE - 2:
high_income = False
good_credit = True
student = True
if high_income or good_credit or not student:
    print("Eligible")
else:
    print("Not Eligible")

# NOTE that, in Python, Short Circuiting is a concept in which interpreter stops evaluating
# as soon as one of the arguments/conditions evaluates to "True".
# i.e, good_credit = True results in interpreter to stop evaluating remaining conditions because
# it's evaluated to "True".


# NOTE THAT IN PYTHON, LOGICAL OPERATORS ARE "SHORT-CIRCUIT".
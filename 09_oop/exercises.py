# Exercise: Predict the Output
# Q. What will this code print?

class Person:
    species = "Human"

    def __init__(self, name):
        self.name = name

    def greet(self):
        return f"Hello, {self.name}"


p1 = Person("Ali")
p2 = Person("Sara")

print(p1.name)
print(p2.name)
print(p1.species)
print(p1.greet())
